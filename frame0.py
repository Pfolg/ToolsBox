# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   frame0 |User    Pfolg
# 2024/7/20   13:23
import os
from tkinter import ttk
import plugins.QRCodeMaker as qr
import plugins.makeFilesPhot as mf
import plugins.musicPlayer as mp
import win32com.client
import time
import requests
import plugins.FrameSetting as st
import plugins.randomName as rm
import plugins.otherFunction as ofc
import plugins.ThirdPackage as tp
import plugins.keyWordsAnalysis as ka
import random
import plugins.FrameWin as fw
import plugins.singleDouble as sd
import plugins.BoxMails as bm


def basicFrame0(w, h, window):
    try:
        with open(".\\setting\\Setting-APIuse.txt", 'r', encoding="utf-8") as file:
            listSentence = file.readlines()
        if listSentence:
            newList = [s.rstrip('\r\t\n') for s in listSentence]
            sentence = newList[random.randint(0, len(newList) - 1)]
        else:
            url = "https://tenapi.cn/v2/yiyan"
            content = requests.get(url)
            sentence = content.text
    except BaseException:
        sentence = ""

    def get_time():
        time2 = time.strftime('%Y-%m-%d %H:%M:%S')
        clock = ttk.Label(frame0, text=time2, font=10, foreground="#000000")
        time3 = int(time.strftime("%H"))
        if 0 <= time3 < 6:
            text = "凌晨好!"
        elif time3 < 12:
            text = "上午好!"
        elif time3 < 18:
            text = "下午好!"
        else:
            text = "晚上好!"
        clock.place(relx=.01, rely=.95)
        # 获取当前登录的用户名称
        userName = win32com.client.Dispatch('WScript.Network').UserName
        ttk.Label(frame0, text=f"{text} {userName}", foreground="#000000").place(relx=.25, rely=.95)
        clock.after(1000, get_time)  # 1000ms=1s

    def convertFrame(f1, f2):
        f1.place_forget()
        f2.place(relx=0, rely=0, width=w, height=h)

    def buttons(targetFrame: ttk.Frame, text: str, rx, ry, width=16):
        ttk.Button(frame0, text=text, width=width,
                   command=lambda: convertFrame(frame0, targetFrame)).place(relx=rx, rely=ry)  # 进入该frame的按钮
        ttk.Button(targetFrame, width=8, text='返回',
                   command=lambda: convertFrame(targetFrame, frame0)).place(relx=.9, rely=.9)

    # 初始窗口
    frame0 = ttk.Frame(window)
    frame0.place(relx=0, rely=0, width=w, height=h)
    ttk.Label(frame0, width=w, background="#61afef", compound="center").place(relx=0, rely=.02, height=70)
    ttk.Label(frame0, text="    " + sentence, font=("微软雅黑", 10), background="#61afef",
              compound="center", foreground="#FFFFFF").place(
        relx=0, rely=.02, height=70)

    # 产生frame框架
    frameMakeFiles = ttk.Frame(window)
    frameMusicPlayer = ttk.Frame(window)
    frameQR = ttk.Frame(window)
    frameRandomName = ttk.Frame(window)
    framePythonPackage = ttk.Frame(window)
    frameKeyWord = ttk.Frame(window)
    frameWin = ttk.Frame(window)
    frameClick = ttk.Frame(window)
    frameMail = ttk.Frame(window)

    # 最多34个，不能再多了，多了就要重构一下了
    # 由于循环的关系，每隔5个按钮就会跳过一个
    dictFrame = {
        "批量创建": frameMakeFiles,
        "音乐播放器": frameMusicPlayer,
        "二维码生成器": frameQR,
        "随机点名": frameRandomName,
        "Python第三方库工具": framePythonPackage,

        "Bug-1": 1,

        "PDF关键词分析": frameKeyWord,
        "电脑功能": frameWin,
        "自动点击": frameClick,
        "邮件": frameMail,
    }

    "主功能设定"
    # 批量创建文件（文件夹）
    mf.makeFilesPhot(frameMakeFiles)
    # 音乐播放器
    mp.musicPlayer(frameMusicPlayer)
    # 二维码生成器
    qr.QRCodeMaker(frameQR)
    # 随机点名
    rm.randomName(frameRandomName)
    # Python第三方库
    tp.ThirdPackage(framePythonPackage)
    # 关键词分析
    ka.analysisWindow(frameKeyWord)
    # 电脑功能
    fw.winFunction(frameWin)
    # 自动点击
    sd.singleDouble(frameClick)
    # 邮件
    bm.mainMail(frameMail)
    # 5行7列
    i = 0
    j = 2
    for key in dictFrame:
        if i < 5:
            if j < 9:
                buttons(dictFrame.get(key), key, 0.02 + (i * 2 / 10), j / 10)
                i += 1
            else:
                break
        else:
            i = 0
            j += 1

    # 设置
    frameSetting = ttk.Frame(window)
    st.frameSetting(frameSetting)
    buttons(frameSetting, "设置", .9, .9, 8)

    # 其他功能(私有功能)
    frameOtherFunctions = ttk.Frame(window)
    ofc.otherFunction(frameOtherFunctions)
    buttons(frameOtherFunctions, "其他功能", .82, .8)

    ttk.Button(frame0, text="关于ToolsBox", command=lambda: os.system(".\\README.md")).place(relx=.75, rely=.9)

    get_time()