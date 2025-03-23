import utils.clean_image
import utils.extract_blue
import utils.extract_files
import utils.rename
import utils.segment

files_dir = "original_files"  # 电机报告存放的文件夹
text_dir = "extracted_text"  # 解析出文本输出的文件夹
pics_dir = "extracted_pics"  # 解析出图片保存的文件夹
segmented_dir = "segmented_pics"  # 切割后的图片保存的文件夹
extract_blue_dir = "extracted_blue"  # 提取出的蓝色频谱曲线保存的文件夹

utils.extract_files.batch_process_pdfs(files_dir, text_dir, pics_dir)  # 将电机报告解析为文本和图片
utils.rename.rename_images(pics_dir)  # 重命名图片
utils.clean_image.delete_small_images(pics_dir)  # 删除无关图片，保留频谱曲线
utils.segment.extract_rectangle(pics_dir, segmented_dir)  # 切割图片，只保留频谱曲线部分
utils.extract_blue.process_images_in_folder(segmented_dir, extract_blue_dir)
