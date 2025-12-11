print("sinh vien : le hoang vu")

print("ma so sv :245751030110084")

print("#############################")
import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="Choose your favourite programming language:",
         justify=tk.LEFT, padx=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language[0],
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   indicatoron=0,
                   width=20,
                   value=language[1]).pack(anchor=tk.W)

root.mainloop()
