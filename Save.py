import tkinter as tk
from pytube import YouTube

def download_video():
    url = entry.get()
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        video_stream.download()
        label.config(text="Загрузка успешно завершена!", fg="green")
    except Exception as e:
        label.config(text="Произошла ошибка при загрузке видео:", fg="red")
        print(str(e))

root = tk.Tk()
root.title("Скачивание видео с YouTube")

label = tk.Label(root, text="Введите ссылку на видео YouTube:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

download_button = tk.Button(root, text="Скачать видео", command=download_video)
download_button.pack()

root.mainloop()
