import fitz  # PyMuPDF
import os

def extract_text_and_images(pdf_path, text_output_path, pics_dir, pdf_basename):
    # 打开 PDF 文件
    doc = fitz.open(pdf_path)
    all_text = ""
    
    # 遍历所有页面
    for page_number in range(len(doc)):
        page = doc[page_number]
        
        # 提取文本
        text = page.get_text()
        all_text += f"------ Page {page_number + 1} ------\n"
        all_text += text + "\n"
        
        # 提取图片
        image_list = page.get_images(full=True)
        if image_list:
            all_text += f"该页包含 {len(image_list)} 张图片。\n"
            for img_index, img in enumerate(image_list, start=1):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                # 构造图片文件名：原pdf文件名 + 页码 + 图片序号
                image_filename = f"{pdf_basename}_page{page_number + 1}_img{img_index}.{image_ext}"
                image_full_path = os.path.join(pics_dir, image_filename)
                # 保存图片
                with open(image_full_path, "wb") as image_file:
                    image_file.write(image_bytes)
                all_text += f"保存图片：{image_filename}\n"
        else:
            all_text += "该页无图片。\n"
        
        all_text += "\n"  # 分隔各页内容
    
    # 将文本信息保存到文件中
    with open(text_output_path, "w", encoding="utf-8") as f:
        f.write(all_text)
    print(f"处理 {pdf_path} 成功，文本保存到 {text_output_path}")

def batch_process_pdfs(files_dir, text_dir, pics_dir):
    # 如果输出目录不存在，则创建
    if not os.path.exists(text_dir):
        os.makedirs(text_dir)
    if not os.path.exists(pics_dir):
        os.makedirs(pics_dir)
    
    # 遍历 files 目录下的所有文件
    for filename in os.listdir(files_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(files_dir, filename)
            pdf_basename = os.path.splitext(filename)[0]
            text_output_path = os.path.join(text_dir, f"{pdf_basename}.txt")
            extract_text_and_images(pdf_path, text_output_path, pics_dir, pdf_basename)