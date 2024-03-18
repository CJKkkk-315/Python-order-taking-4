
from PyPDF2 import PdfReader
import pandas as pd


def split_into_sentences(text):
    text = text.replace('?', '.').replace(';', '.').replace('!', '.')
    sentences = text.split('.')
    return sentences


# 打开你的pdf文件
with open("The Ballad of the Sad Café - Carson McCullers.pdf", "rb") as file:
    reader = PdfReader(file)
    print("开始处理PDF...")

    # 读取pdf的每一页
    sentences_with_dash = []
    for i, page in enumerate(reader.pages):
        now_page_s = []
        print(f"处理第 {i + 1} 页...")
        text = page.extract_text()

        # 分句
        sentences = split_into_sentences(text)

        # 寻找带有破折号的句子
        for sentence in sentences:
            if '—' in sentence:
                sentences_with_dash.append(sentence)
                now_page_s.append(sentence)
        print(f'当前页面带有对应符号的句子：',now_page_s)
print("PDF处理完成，开始写入Excel...")

# 使用pandas库写入Excel
df = pd.DataFrame(sentences_with_dash, columns=['Sentences'])
df.to_excel("sentences_with_dash.xlsx", index=False)

print("完成! 带有对应符号的句子已经被写入 'sentences_with_dash.xlsx'.")

