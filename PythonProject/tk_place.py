import tkinter as tk

root = tk.Tk()
root.title("Tkinter Place")
root.geometry("400x300")
root.resizable(False, False)

# 左側欄
tk.Frame(root, bg="lightgreen").place(x=0, y=0, width=40, height=300)

# 右側欄
tk.Frame(root, bg="lightblue").place(x=360, y=0, width=40, height=300)

# 上層
top = tk.Frame(root, bg="red")
top.place(x=40, y=0, width=320, height=60)

tk.Label(top, text="left", bg="white", fg="black").place(x=10, y=5)
tk.Label(top, text="center", bg="white", fg="black").place(x=130, y=5)
tk.Label(top, text="Right", bg="white", fg="black").place(x=250, y=5)

# 下層
tk.Frame(root, bg="blue").place(x=40, y=270, width=320, height=30)

# 中層
tk.Frame(root, bg="yellow").place(x=40, y=60, width=320, height=210)

root.mainloop()