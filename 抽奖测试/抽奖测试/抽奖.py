import tkinter as tk
import random

def draw_winner():
    # 提供的名单
    name_list = [
        "薛舒丽", "江林雅", "伍诗彤", "曾可莹", "罗欣怡", "詹辰愉", "赖裕好", "张铭宇", "朱希贝", "丘淼", "汪楚妍", "潘盈盈", "刘粤华",
        "游思雅", "廖雨娟", "李卓朋", "邹婷婷", "刘仕文", "曾钰桃", "苏卓蓝", "廖晓阳", "张昆", "曾除伟", "傅颖颖", "段欣", "刘雨阳",
        "张文锦", "李军威", "曾治业", "欧嘉文", "谢粮泽", "程煌杰", "邱燕琴", "黄子航", "袁立", "张瑶瑶", "林希", "黄诗煜"
    ]

    if name_list:
        # 在名单中添加额外的"赖欲银"和"李模"，以降低它们的抽中概率
        name_list += ["赖欲银", "李模"]
        
        # 使用random.choices来设置权重
        winner = random.choices(name_list, weights=[1 if name not in ["赖欲银", "李模"] else 0.2 for name in name_list])[0]
        result_label.config(text=f"抽中的人是：{winner}")

    # 更新可能被抽中的人的名单
    name_list_text.config(state=tk.NORMAL)
    name_list_text.delete(1.0, tk.END)
    name_list_text.insert(tk.END, "\n".join(name_list))
    name_list_text.config(state=tk.DISABLED)

# 创建主窗口
root = tk.Tk()
root.title("随机抽人软件")

# 添加新的背景图片（替换"your_new_image.png"为你的新图像文件路径）
# bg_image = tk.PhotoImage(file="choujiang.jpg")
# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(relwidth=1, relheight=1)

# 创建文本标签
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

# 创建抽奖按钮
draw_button = tk.Button(root, text="抽奖", command=draw_winner)
draw_button.pack()

# 创建可能被抽中的人的名单文本框
name_list_text = tk.Text(root, height=10, width=30)
name_list_text.insert(tk.END, "可能被抽中的人的名单：")
name_list_text.config(state=tk.DISABLED)
name_list_text.pack()

# 运行主循环
root.mainloop()
