import ssl
import smtplib
from email.message import EmailMessage
import time
import tkinter as tk
import threading
import os
import tkinter.messagebox
def send_email(EMAIL_ADDRESS,EMAIL_PASSWORD,receiver,title):
    context = ssl.create_default_context()
    sender = EMAIL_ADDRESS
    body = ''
    msg = EmailMessage()
    msg['subject'] = title
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# 标记变量
stop_flag = 0
all_count = 0

def cycle_main():
    global stop_flag, all_count
    # key = 'jxcnynszlgnzhejh'
    # EMAIL_ADDRESS = '1121033787@qq.com'
    key = password_entry.get()
    EMAIL_ADDRESS = username_entry.get()
    receiver_content = content_text.get("1.0","end-1c")
    receiver_info = {}
    print(receiver_content.split('\n'))
    for line in receiver_content.split('\n'):
        receiver_info[line.split()[0]] = line.split()[1].split(',')
    with open('SignalOut.txt') as f:
        old_records = f.read().split('\n')
        old_records = [i for i in old_records if i]
    while True:
        time.sleep(1)
        print("运行中...")
        if stop_flag:
            break
        with open('SignalOut.txt') as f:
            records = f.read().split('\n')
            records = [i for i in records if i]
        if len(records) > len(old_records):
            new_count = len(records) - len(old_records)
            new_records = records[-new_count:]
            for r in new_records:
                sr = r.split('|')
                title = '|'.join(r.split('|')[1:5]) + ' ' + r.split('|')[-1] + '    ' + r.split('|')[-2]
                for u in receiver_info:
                    if sr[1] in receiver_info[u]:
                        send_email(EMAIL_ADDRESS,key,u,title)
                        all_count += 1
        old_records = records

        root.update()





def start():
    state_now.config(text='启动中...')
    global stop_flag, all_count
    all_count = 0
    stop_flag = 0
    threading.Thread(target=cycle_main).start()

def stop():
    state_now.config(text='未启动')
    global stop_flag,all_count
    stop_flag = 1
    tkinter.messagebox.showinfo('执行完毕！',f'本次运行共发送{all_count}条邮件')

if os.path.exists('config.txt'):
    content_data = open('config.txt').read()
    content_data = [i for i in content_data.split('\n') if i]
    EMAIL_ADDRESS = content_data[0]
    key = content_data[1]
    content_info = '\n'.join(content_data[2:])
else:
    key = ''
    EMAIL_ADDRESS = ''
    content_info = ''
root = tk.Tk()

username_label = tk.Label(root, text="账号")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
username_entry.insert(0,EMAIL_ADDRESS)
password_label = tk.Label(root, text="16位密钥")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()
password_entry.insert(0,key)
content_label = tk.Label(root, text="内容")
content_label.pack()
content_text = tk.Text(root)
content_text.pack()
content_text.insert("1.0",content_info)
state_now = tk.Label(root, text='未启动')
state_now.pack()

start_button = tk.Button(root, text="启动", command=start)
start_button.pack()

stop_button = tk.Button(root, text="停止", command=stop)
stop_button.pack()

root.mainloop()
