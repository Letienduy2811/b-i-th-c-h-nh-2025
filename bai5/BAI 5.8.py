from tkinter import *

root = Tk()
root.title("Thông tin cá nhân")
print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
root.geometry("300x280")

Label(root, text="Họ tên:").pack()
name = Entry(root)
name.pack()

Label(root, text="Ngày sinh:").pack()
dob = Entry(root)
dob.pack()

Label(root, text="MSSV:").pack()
mssv = Entry(root)
mssv.pack()

Label(root, text="Năm học:").pack()
year = Entry(root)
year.pack()

Label(root, text="Chọn số:").pack()
v = IntVar()
v.set(1)

def showNumber():
    print("Bạn chọn:", v.get())

Radiobutton(root, text="1", variable=v, value=1).pack()
Radiobutton(root, text="2", variable=v, value=2).pack()
Radiobutton(root, text="3", variable=v, value=3).pack()

def clicked():
    print("Họ tên:", name.get())
    print("Ngày sinh:", dob.get())
    print("MSSV:", mssv.get())
    print("Năm học:", year.get())
    print("Số đã chọn:", v.get())

Button(root, text="Click Me", command=clicked).pack(pady=10)

root.mainloop()
