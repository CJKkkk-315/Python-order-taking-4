import pdfplumber
import os
import re

def remove_cid(text):
    cleaned_text = re.sub(r'\(cid:\d+\)', '', text)
    return cleaned_text


def extract_text_from_pdf(pdf_path, txt_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    text = page.extract_text()
                    cleaned_text = remove_cid(text)
                    txt_file.write(cleaned_text)

        print(f"文本已成功提取并保存到 {txt_path}")
    except Exception as e:
        print(f"提取文本时出错: {str(e)}")


files = os.listdir()

for file in files[1:]:
    pdf_file_path = file
    txt_file_path = '神华txt/' + file.replace('.pdf','.txt')
    print(file)
    # 调用函数进行文本提取
    extract_text_from_pdf(pdf_file_path, txt_file_path)
