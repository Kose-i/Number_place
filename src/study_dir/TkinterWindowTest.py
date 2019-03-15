#!/usr/bin/env python3

import tkinter as tk
import threading
import time

def thread1_func():
    # thread の名前を取得
    print('start 1')
    time.sleep(5)
    print('end 1')

def thread2_func():
    print('start 2')
    time.sleep(5)
    print('end 2')

root = tk.Tk()
root.geometry('800x460')
font = ('Helvetica, 14')
root.title('player')

root2 = tk.Tk()
root2.geometry('800x460')
root2.title('enemy')

root.mainloop()

# スレッドに workder1 関数を渡す
thread1 = threading.Thread(target=thread1_func)
thread2 = threading.Thread(target=thread2_func)
# スレッドスタート
thread1.start()
thread2.start()
print('started all')
