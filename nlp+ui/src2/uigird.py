import tkinter as tk
from my_ui_test import allf, FMMSegment
import tkinter.messagebox
import re
need_delete_button = []
need_delete_text = []
inv_index, name_list, doc_list, loc_set, dict_loc, file_dict_lines, N, my_ins = None, None, None, None, None, None, None, None
# Mocked data - Replace this with your actual backend code
def search_results(input_text):
    global inv_index, name_list, doc_list, loc_set, dict_loc, file_dict_lines, N, my_ins
    res, use_time, inv_index, name_list, doc_list, loc_set, dict_loc, file_dict_lines, N, my_ins = allf(input_text,inv_index, name_list, doc_list, loc_set, dict_loc, file_dict_lines, N, my_ins)
    # Replace this with your backend code that performs word segmentation and searches for results
    # Mocking the results for demonstration purposes
    results = {
        "功能": [(i[1],i[2]) for i in res[0]],
        "产品":  [(i[1],i[2]) for i in res[1]],
        "缴费": [(i[1],i[2]) for i in res[2]],
        "生活":  [(i[1],i[2]) for i in res[3]],
        "活动":  [(i[1],i[2]) for i in res[4]],
    }
    print(res)
    return results, use_time

def show_all_results(category, category_results, input_text):

    top_level = tk.Toplevel(root)
    main_window_x = root.winfo_rootx()
    main_window_y = root.winfo_rooty()
    new_window_x = main_window_x + 400
    new_window_y = main_window_y - 25
    top_level.geometry(f"400x600+{new_window_x}+{new_window_y}")
    top_level.title(f"{category}:所有结果")
    h = 0
    result_label = tk.Text(top_level,wrap=tk.NONE, height=46, borderwidth=0, highlightthickness=0)
    result_label.place(x=10,y=10)
    result_label.configure(bg=bg_color)  # 设置背景颜色
    scrollbar = tk.Scrollbar(top_level, command=result_label.yview)
    scrollbar.place(x=385, y=0, relheight=1)
    result_label.config(yscrollcommand=scrollbar.set)
    result_label.tag_configure("red_font", foreground="red")
    all_set = set()
    all_text = ''
    for i, result in enumerate(category_results):
        h += 40
        now_text = str(i + 1) + '.' + result[0]
        all_text += now_text + "\n\n"
        result_label.insert(tk.END, now_text, )
        result_label.insert(tk.END, "\n\n")
        # result_label.insert(tk.END, str(i+1) + '.' + result)
        for j in result[1]:
            all_set.add(j)
    for word in all_set:
        search_pattern = word
        start_index = "1.0"
        while True:
            found_index = result_label.search(search_pattern, start_index, tk.END, nocase=tk.TRUE)
            if not found_index:
                break
            result_label.tag_add("red_font", found_index, f"{found_index}+{len(search_pattern)}c")
            start_index = f"{found_index}+1c"



def search_button_click():
    input_text = input_entry.get()
    results, use_time = search_results(input_text)
    update_results_display(results, input_text, use_time)
def help_info():
    tkinter.messagebox.showinfo('使用说明','XXX\nXXX\nXXX')
def update_results_display(results, input_text, use_time):
    for b in need_delete_button:
        b.destroy()
    for b in need_delete_text:
        b.destroy()
    need_delete_button.clear()
    need_delete_text.clear()

    ll.configure(text=f'本次搜索用时{use_time}毫秒')
    bg_color = root.cget("bg")
    # Clear previous results
    # for widget in results_frame.winfo_children():
    #     widget.destroy()

    # Display new results
    h = 0
    for category, category_results in results.items():
        category_label = tk.Text(root, height=1, wrap=tk.NONE, borderwidth=0, highlightthickness=0)
        category_label.place(x=10, y=80+h)
        category_label.configure(font=("FangSong", 12, "bold"))
        need_delete_text.append(category_label)
        now_text = f"{category}:"
        category_label.insert(tk.END, now_text,)
        category_label.configure(bg=bg_color)  # 设置背景颜色
        # Add a button next to the category label to show all results
        show_all_button = tk.Button(root, text=f"全部({len(category_results)})", command=lambda cat=category, cr=category_results: show_all_results(cat, cr, input_text))
        show_all_button.place(x=300, y=80+h)
        show_all_button.configure(relief=tk.FLAT)  # 设置按钮边框为平坦样式
        show_all_button.configure(bd=0)  # 设置按钮边框宽度为0
        show_all_button.configure(font=("KaiTi", 12, "underline"))  # 设置字体和下划线
        need_delete_button.append(show_all_button)
        h += 25
        # Display first 3 results as labels
        for i, result in enumerate(category_results[:3]):  # Limit to at most 3 results per category
            result_label = tk.Text(root, height=1, wrap=tk.NONE, borderwidth=0, highlightthickness=0)
            result_label.place(x=10, y=80+h)
            result_label.tag_configure("red_font", foreground="red")
            result_label.configure(bg=bg_color)
            need_delete_text.append(result_label)
            h += 25
            now_text = str(i + 1) + '.' + result[0]
            result_label.insert(tk.END, now_text, )
            result_label.insert(tk.END, "\n\n")
            for word in result[1]:
                search_pattern = word
                start_index = "1.0"
                while True:
                    found_index = result_label.search(search_pattern, start_index, tk.END, nocase=tk.TRUE)
                    if not found_index:
                        break
                    result_label.tag_add("red_font", found_index, f"{found_index}+{len(search_pattern)}c")
                    start_index = f"{found_index}+1c"
# Create the main application window
root = tk.Tk()
root.title("Search App")
root.geometry("400x600")
# Create the widgets
input_frame = tk.Frame(root)
input_frame.pack(pady=5)


input_entry = tk.Entry(input_frame, width=35)
input_entry.pack(side="left", padx=5)

search_button = tk.Button(input_frame, text="搜索", height=1, command=search_button_click)
search_button.pack(side="left", padx=5)

search_button = tk.Button(input_frame, text="清空", height=1, command=lambda : input_entry.delete(0,'end'))
search_button.pack(side="left", padx=5)
bg_color = root.cget("bg")
# results_frame = tk.Frame(root)
# results_frame.pack(pady=10)
help = tk.Button(root, text='使用说明', command=help_info)
help.place(x=30, y=40)
help.configure(relief=tk.FLAT)
help.configure(bd=0)
help.configure(font=("Microsoft YaHei", 10, "underline"))
ll = tk.Label(root,text='')
ll.place(x=130,y=43)
# Start the main event loop
root.mainloop()

