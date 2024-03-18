import tkinter as tk

def search_text():
    search_pattern = search_entry.get()
    start_index = "1.0"
    while True:
        found_index = text_widget.search(search_pattern, start_index, tk.END, nocase=tk.TRUE)
        if not found_index:
            break
        text_widget.tag_add("highlight", found_index, f"{found_index}+{len(search_pattern)}c")
        start_index = f"{found_index}+1c"

root = tk.Tk()
root.title("Text Search Example")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_text)
search_button.pack()

text_widget.tag_configure("highlight", background="yellow")

root.mainloop()
