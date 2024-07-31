# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   openWeather |User    Pfolg
# 2024/7/31   23:58
from tkinter import ttk
import requests
import json
import tkinter as tk


def openWeather(frame):
    try:
        with open(".\\setting\\Config.txt", "r", encoding="utf-8") as myF:
            myDict = json.load(myF)
            city = myDict.get("city")
            opwAPI = myDict.get("openweatherAPI")
    except BaseException:
        return False
    language = 'zh_cn'  # 简体中文  &lang={language}

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={opwAPI}&lang={language}'

    target = requests.get(url)
    content = target.json()
    s = json.dumps(content, ensure_ascii=False, indent=2)
    data = json.loads(s)

    if data["cod"] == 200:
        mycity = data["name"]
        weather_description = data["weather"][0]["description"]  # 多云
        temp = data['main']['temp']  # ℃
        humidity = data['main']['humidity']  # %

        weatherInformation = f"{mycity}    {weather_description}    {temp}℃    {humidity}%"

        ttk.Label(frame, text=weatherInformation).place(relx=.4, rely=.95)


if __name__ == '__main__':
    pass