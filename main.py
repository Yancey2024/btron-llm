# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import datetime
import uuid
import utils.clean_image
import utils.extract_blue
import utils.extract_files
import utils.init
import utils.rename
import utils.segment
import utils.detect_peak
import utils.calculate

app = Flask(__name__)
CORS(app)  # 解决跨域问题

# 配置上传参数
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB

files_dir = "original_files"  # 电机报告存放的文件夹
text_dir = "extracted_text"  # 解析出文本输出的文件夹
pics_dir = "extracted_pics"  # 解析出图片保存的文件夹
segmented_dir = "segmented_pics"  # 切割后的图片保存的文件夹
extract_blue_dir = "extracted_blue"  # 提取出的蓝色频谱曲线保存的文件夹
peak_blue_dir = "peak_blue"  # 检测出的蓝色频谱曲线峰值保存的文件夹
final_result_dir = "final_result"  # 最终结果保存的文件夹

init_folder_paths = [
    files_dir,
    text_dir,
    pics_dir,
    segmented_dir,
    extract_blue_dir,
    peak_blue_dir,
    final_result_dir
]  # 需要清空的文件夹路径列表

# 文件上传处理
@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "未选择文件"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "文件名为空"}), 400
    
    if file and allowed_file(file.filename):
        original_filename = file.filename
        filename = random_filename(file.filename)
        file_path = os.path.join(files_dir, filename)
        utils.init.delete_all_files_in_folders(init_folder_paths)  # 清空调试过程所产生的文件
        file.save(file_path)
        
        # 这里可以添加PDF处理逻辑（如解析内容、生成报告等）
        utils.extract_files.batch_process_pdfs(files_dir, text_dir, pics_dir)  # 将电机报告解析为文本和图片
        utils.clean_image.delete_small_images(pics_dir)  # 删除无关图片，保留频谱曲线
        utils.rename.rename_images(pics_dir)  # 重命名图片
        utils.segment.extract_rectangle(pics_dir, segmented_dir)  # 切割图片，只保留频谱曲线部分
        utils.extract_blue.process_folder(segmented_dir, extract_blue_dir)  # 提取蓝色频谱曲线
        utils.detect_peak.process_multiple_csv_files(extract_blue_dir, peak_blue_dir)  # 检测频谱曲线的峰值
        result = utils.calculate.process_directory(peak_blue_dir, final_result_dir)  # 计算峰值的频率和幅值，结果保存到final_result文件夹里

        processed_data = {
            "fileName": original_filename,
            "fileSize": os.path.getsize(file_path),
            "timestamp": datetime.datetime.now().isoformat(),
            "message": "文件处理成功",
            "result": result,
            "success": True
        }
        return jsonify(processed_data), 201
    
    return jsonify({"error": "文件类型不正确"}), 400

# 文件类型验证
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 对上传文件随机重新命名
def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

if __name__ == '__main__':
    app.run(debug=True, port=5000)