# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import main_module
import tkinter as tk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    x = 1

   # if x > 2:
    #    print(x)
   # else:
    #    print('no')
    while x < 10:
        x = x + 1
        print(x)
        continue
    print('fdad')
    return 'good'
def newtext():
    a = text_input.get()
    title_label.configure(text=a)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  #  b = print_hi('เมื่อรักฉันเกิด')
  #  print(b)
  #  main_module.test()

  window = tk.Tk()
  window.title('title python')
  window.minsize(800,600)
  window.maxsize(800,600)

  title_label = tk.Label(window,text='dd')
  title_label.pack()

  text_input = tk.Entry(window)
  text_input.pack(pady=20)

  ok_button = tk.Button(
      window,text='OK',
      command=newtext,width=15,height=2)
  ok_button.pack()



  window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





