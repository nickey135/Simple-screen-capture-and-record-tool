import tkinter as tk
from tkinter import simpledialog
import cv2
import pyautogui
import numpy as np

# 截图函数
def scrt(filename='screenshot.png'):
    # 使用pyautogui截图
    img = pyautogui.screenshot()
    # 保存截图
    img.save(filename)

# 录屏函数
def scrd(filename='screen_record.avi', record_time=10, fps=30.0):
    # 获取屏幕大小
    screen_size = (1920, 1080)
    # 创建VideoWriter对象
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, fps, screen_size)
    # 录屏
    for i in range(int(fps * record_time)):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    # 释放资源
    out.release()
    cv2.destroyAllWindows()

def screenshot():
    root.withdraw()
    filename = simpledialog.askstring("截屏", "请完整输入图片名+.png后缀")
    root.deiconify()
    scrt(filename)

def screenrecord():
    root.withdraw()
    filename = simpledialog.askstring("录屏", "请完整输入视频名+.avi后缀")
    duration = simpledialog.askinteger("录屏", "请输入录制时间（秒）")
    root.deiconify()
    scrd(filename, duration)

root = tk.Tk()
root.title("截屏录屏工具")
root.geometry("400x200")
button1 = tk.Button(root, text="截屏", command=screenshot)
button1.pack(side=tk.LEFT)
button1.place(x=100,y=100)
button2 = tk.Button(root, text="录屏", command=screenrecord)
button2.pack(side=tk.LEFT)
button2.place(x=200,y=100)

root.mainloop()

