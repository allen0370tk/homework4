import tkinter as tk

root = tk.Tk()
root.title("Tkinter Pack")
root.geometry("400x300")
root.resizable(False, False)

# 左側欄
left = tk.Frame(root, bg="lightgreen", width=40)
left.pack(side="left", fill="y")

# 右側欄
right = tk.Frame(root, bg="lightblue", width=40)
right.pack(side="right", fill="y")

# 中間區域
center = tk.Frame(root)
center.pack(expand=True, fill="both")

# 上層
top = tk.Frame(center, bg="red", height=60)
top.pack(side="top", fill="x")

tk.Label(top, text="left", bg="white", fg="black").pack(side="left", anchor="n", padx=10)
tk.Label(top, text="center", bg="white", fg="black").pack(side="top", anchor="n")
tk.Label(top, text="Right", bg="white", fg="black").pack(side="right", anchor="n", padx=10)

# 下層
bottom = tk.Frame(center, bg="blue", height=30)
bottom.pack(side="bottom", fill="x")

# 中層
middle = tk.Frame(center, bg="yellow")
middle.pack(expand=True, fill="both")

root.mainloop()