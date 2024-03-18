import tkinter as tk

# Mocked data - Replace this with your actual backend code
def search_results(input_text):
    # Replace this with your backend code that performs word segmentation and searches for results
    # Mocking the results for demonstration purposes
    results = {
        "Category 1": ["Result 1A", "Result 1B", "Result 1C", "Result 1D"],
        "Category 2": ["Result 2A", "Result 2B"],
        "Category 3": ["Result 3A", "Result 3B", "Result 3C"],
        "Category 4": ["Result 4A", "Result 4B"],
        "Category 5": ["Result 5A", "Result 5B", "Result 5C"],
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
    update_results_display(results, input_text)

def update_results_display(results, input_text):
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

        # Display first 3 results as labels with keyword highlighting
        for i, result in enumerate(category_results[:3]):  # Limit to at most 3 results per category
            result_label = tk.Label(results_frame, text="", justify="left")  # Create a label with left alignment
            result_label.pack(side="top", anchor="w", padx=15, pady=2)

            # Split the result text based on keyword occurrence and highlight the keywords in red
            current_idx = 0
            words = input_text.split()
            for word in words:
                idx = result.lower().find(word.lower(), current_idx)
                if idx == -1:
                    result_label.config(text=result[current_idx:], fg="black")
                    break
                result_label.config(text=result[current_idx:idx], fg="black")
                keyword_label = tk.Label(result_label, text=result[idx:idx+len(word)], fg="red")
                keyword_label.pack(side="left")
                current_idx = idx + len(word)
            else:
                result_label.config(text=result[current_idx:], fg="black")

# Create the main application window
root = tk.Tk()
root.title("Search App")

# Create the widgets
input_label = tk.Label(root, text="Enter your sentence:")
input_label.pack(pady=5)

input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack(pady=5)

results_frame = tk.Frame(root)
results_frame.pack(pady=10)

# Start the main event loop
root.mainloop()
