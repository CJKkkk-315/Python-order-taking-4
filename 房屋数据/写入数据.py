import pandas as pd
import os
from tkinter import *
import shutil
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
df = pd.read_excel('模拟1/凤珍海王1魏根英档案.xlsx')
df.to_excel('test.xlsx')