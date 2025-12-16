import tkinter as tk

root = tk.Tk()
root.title("Tkinter Grid")
root.geometry("400x300")
root.resizable(False, False)

# 設定 grid 欄列比例
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# 左側欄
left = tk.Frame(root, bg="lightgreen", width=40)
left.grid(row=0, column=0, sticky="ns")

# 右側欄
right = tk.Frame(root, bg="lightblue", width=40)
right.grid(row=0, column=2, sticky="ns")

# 中間區域
center = tk.Frame(root)
center.grid(row=0, column=1, sticky="nsew")

# 上層
top = tk.Frame(center, bg="red", height=60)
top.grid(row=0, column=0, sticky="ew")

tk.Label(top, text="left", bg="white", fg="black").grid(row=0, column=0, sticky="n", padx=10)
tk.Label(top, text="center", bg="white", fg="black").grid(row=0, column=1, sticky="n")
tk.Label(top, text="Right", bg="white", fg="black").grid(row=0, column=2, sticky="n", padx=10)

# 中層
middle = tk.Frame(center, bg="yellow")
middle.grid(row=1, column=0, sticky="nsew")

# 下層
bottom = tk.Frame(center, bg="blue", height=30)
bottom.grid(row=2, column=0, sticky="ew")

# 調整中間區域的比例
center.grid_rowconfigure(1, weight=1)
center.grid_columnconfigure(0, weight=1)

root.mainloop()