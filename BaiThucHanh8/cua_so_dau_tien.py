print("\nHoạt động 1: ")
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Cửa sổ Tkinter đầu tiên")
cua_so.geometry("400x300")
cua_so.mainloop()

import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Ứng dụng demo")
cua_so.geometry("400x300")
cua_so.resizable(False, False)
nhan = tk.Label(cua_so, text="Xin chào Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)
cua_so.mainloop()

print("\nHoạt động 2: ")
import tkinter as tk
cua_so = tk.Tk()
cua_so.title("Ví dụ Frame")
cua_so.geometry("400x300")
khung_tren = tk.Frame(cua_so, bg="lightyellow")
khung_tren.pack(fill="both", expand=True)
khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)
tk.Label(khung_tren, text="Khu vực tiêu đề", bg="lightblue").pack(pady=10)
tk.Label(khung_duoi, text="Khu vực nội dung", bg="lightyellow").pack(pady=10)
cua_so.mainloop()