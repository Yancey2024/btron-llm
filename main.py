import utils.clean_image
import utils.extract_blue
import utils.extract_files
import utils.init
import utils.rename
import utils.segment
import utils.detect_peak
import utils.calculate

files_dir = "original_files"  # 电机报告存放的文件夹
text_dir = "extracted_text"  # 解析出文本输出的文件夹
pics_dir = "extracted_pics"  # 解析出图片保存的文件夹
segmented_dir = "segmented_pics"  # 切割后的图片保存的文件夹
extract_blue_dir = "extracted_blue"  # 提取出的蓝色频谱曲线保存的文件夹
peak_blue_dir = "peak_blue"  # 检测出的蓝色频谱曲线峰值保存的文件夹
final_result_dir = "final_result"  # 最终结果保存的文件夹

init_folder_paths = [
    text_dir,
    pics_dir,
    segmented_dir,
    extract_blue_dir,
    peak_blue_dir,
    final_result_dir
]  # 需要清空的文件夹路径列表

utils.init.delete_all_files_in_folders(init_folder_paths)  # 清空调试过程所产生的文件
utils.extract_files.batch_process_pdfs(files_dir, text_dir, pics_dir)  # 将电机报告解析为文本和图片
utils.clean_image.delete_small_images(pics_dir)  # 删除无关图片，保留频谱曲线
utils.rename.rename_images(pics_dir)  # 重命名图片
utils.segment.extract_rectangle(pics_dir, segmented_dir)  # 切割图片，只保留频谱曲线部分
utils.extract_blue.process_folder(segmented_dir, extract_blue_dir)  # 提取蓝色频谱曲线
utils.detect_peak.process_multiple_csv_files(extract_blue_dir, peak_blue_dir)  # 检测频谱曲线的峰值
print("-" * 50)  # 分隔线
utils.calculate.process_directory(peak_blue_dir, final_result_dir)  # 计算峰值的频率和幅值，结果保存到final_result文件夹里