import os
import argparse
import json
import PyPDF2

def extract_text_from_pdf(pdf_path):
    pdf_file_obj = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

def main(directory):
    files = os.listdir(directory)
    pdf_files = [file for file in files if file.endswith('.pdf')]
    data = []
    for pdf_file in pdf_files:
        content = extract_text_from_pdf(os.path.join(directory, pdf_file))
        data.append({
            "filename": pdf_file,
            "content": content
        })
    with open('result.json', 'w') as f:
        json.dump(data, f,ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str)
    args = parser.parse_args()
    main(args.directory)
