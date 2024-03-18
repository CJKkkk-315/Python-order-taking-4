import tkinter as tk
from my_ui_test import allf

# Mocked data - Replace this with your actual backend code
def search_results(input_text):
    res = allf(input_text)
    print(res)
    # Replace this with your backend code that performs word segmentation and searches for results
    # Mocking the results for demonstration purposes
    results = {
        "功能": [i[1] for i in res[0]],
        "产品":  [i[1] for i in res[1]],
        "缴费": [i[1] for i in res[2]],
        "生活":  [i[1] for i in res[3]],
        "活动":  [i[1] for i in res[4]],
    }
    return results

def show_all_results(category, category_results):
    top_level = tk.Toplevel(root)
    top_level.title(f"All Results for {category}")
    for result in category_results:
        result_label = tk.Label(top_level, text=result)
        result_label.pack(anchor="w", padx=15, pady=2)

def search_button_click():
    input_text = input_entry.get()
    results = search_results(input_text)
    update_results_display(results)

def update_results_display(results):
    # Clear previous results
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Display new results
    for category, category_results in results.items():
        category_label = tk.Label(results_frame, text=f"{category}:")
        category_label.pack(side="top", anchor="w", padx=5, pady=2)

        # Add a button next to the category label to show all results
        show_all_button = tk.Button(results_frame, text="Show All", command=lambda cat=category, cr=category_results: show_all_results(cat, cr))
        show_all_button.pack(side="top", anchor="e", padx=5, pady=2)

        # Display first 3 results as labels
        for i, result in enumerate(category_results[:3]):  # Limit to at most 3 results per category
            result_label = tk.Label(results_frame, text=result)
            result_label.pack(side="top", anchor="w", padx=15, pady=2)

# Create the main application window
root = tk.Tk()
root.title("Search App")

# Create the widgets
input_frame = tk.Frame(root)
input_frame.pack(pady=5)


input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side="left", padx=5)

search_button = tk.Button(input_frame, text="搜索", command=search_button_click)
search_button.pack(side="left", padx=5)

search_button = tk.Button(input_frame, text="清空", command=search_button_click)
search_button.pack(side="left", padx=5)

results_frame = tk.Frame(root)
results_frame.pack(pady=10)

# Start the main event loop
root.mainloop()

