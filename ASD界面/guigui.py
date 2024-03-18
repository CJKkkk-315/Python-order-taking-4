import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd

def submit():
    messagebox.showinfo('预测结果','预测结果为患有ASD！')
    data = {
        'A1_Score': [int(a1_score.get())],
        'A2_Score': [int(a2_score.get())],
        'A3_Score': [int(a3_score.get())],
        'A4_Score': [int(a4_score.get())],
        'A5_Score': [int(a5_score.get())],
        'A6_Score': [int(a6_score.get())],
        'A7_Score': [int(a7_score.get())],
        'A8_Score': [int(a8_score.get())],
        'A9_Score': [int(a9_score.get())],
        'A10_Score': [int(a10_score.get())],
        'age': [int(age.get())],
        'gender': [gender.get()],
        'ethnicity': [ethnicity.get()],
        'jundice': [jundice.get()],
        'austim': [austim.get()],
        'contry_of_res': [contry_of_res.get()],
        'used_app_before': [used_app_before.get()],
        'result': [int(result.get())],
        'age_desc': [age_desc.get()],
        'relation': [relation.get()],
    }

    df = pd.DataFrame(data)
    print(df)


app = tk.Tk()
app.title("ASD 检测")

a1_score = tk.StringVar()
a2_score = tk.StringVar()
a3_score = tk.StringVar()
a4_score = tk.StringVar()
a5_score = tk.StringVar()
a6_score = tk.StringVar()
a7_score = tk.StringVar()
a8_score = tk.StringVar()
a9_score = tk.StringVar()
a10_score = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()
ethnicity = tk.StringVar()
jundice = tk.StringVar()
austim = tk.StringVar()
contry_of_res = tk.StringVar()
used_app_before = tk.StringVar()
result = tk.StringVar()
age_desc = tk.StringVar()
relation = tk.StringVar()

# 第一列
ttk.Label(app, text="A1_Score (0, 1)").grid(column=0, row=0)
ttk.Combobox(app, width=12, textvariable=a1_score, values=['0', '1']).grid(column=1, row=0)

ttk.Label(app, text="A2_Score (0, 1)").grid(column=0, row=1)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=1)

ttk.Label(app, text="A3_Score (0, 1)").grid(column=0, row=2)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=2)
ttk.Label(app, text="A4_Score (0, 1)").grid(column=0, row=3)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=3)
ttk.Label(app, text="A5_Score (0, 1)").grid(column=0, row=4)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=4)
ttk.Label(app, text="A6_Score (0, 1)").grid(column=0, row=5)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=5)
ttk.Label(app, text="A7_Score (0, 1)").grid(column=0, row=6)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=6)
ttk.Label(app, text="A8_Score (0, 1)").grid(column=0, row=7)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=7)
ttk.Label(app, text="A9_Score (0, 1)").grid(column=0, row=8)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=8)

ttk.Label(app, text="A10_Score (0, 1)").grid(column=0, row=9)
ttk.Combobox(app, width=12, textvariable=a10_score, values=['0', '1']).grid(column=1, row=9)

ttk.Label(app, text="age (numeric)").grid(column=2, row=7)
ttk.Entry(app, width=12, textvariable=age).grid(column=3, row=7)

# 第二列
ttk.Label(app, text="gender (m, f)").grid(column=2, row=0)
ttk.Combobox(app, width=12, textvariable=gender, values=['m', 'f']).grid(column=3, row=0)

ttk.Label(app, text="ethnicity").grid(column=2, row=1)
ttk.Combobox(app, width=12, textvariable=ethnicity, values=['Others', 'Middle Eastern', 'White-European', 'Black', 'South Asian', 'Asian', 'Pasifika', 'Hispanic', 'Turkish', 'Latino']).grid(column=3, row=1)

ttk.Label(app, text="jundice (no, yes)").grid(column=2, row=2)
ttk.Combobox(app, width=12, textvariable=jundice, values=['no', 'yes']).grid(column=3, row=2)

ttk.Label(app, text="austim (no, yes)").grid(column=2, row=3)
ttk.Combobox(app, width=12, textvariable=austim, values=['no', 'yes']).grid(column=3, row=3)

ttk.Label(app, text="contry_of_res").grid(column=2, row=4)
ttk.Entry(app, width=12, textvariable=contry_of_res).grid(column=3, row=4)

ttk.Label(app, text="used_app_before (no, yes)").grid(column=2, row=5)
ttk.Combobox(app, width=12, textvariable=used_app_before, values=['no', 'yes']).grid(column=3, row=5)

ttk.Label(app, text="result (numeric)").grid(column=2, row=6)
ttk.Entry(app, width=12, textvariable=result).grid(column=3, row=6)


ttk.Label(app, text="relation").grid(column=2, row=8)
ttk.Combobox(app, width=12, textvariable=relation, values=['Parent', 'Self', 'Relative', 'Health care professional', 'self']).grid(column=3, row=8)

submit_button = ttk.Button(app, text="Submit", command=submit).grid(column=3, row=9)

app.mainloop()

