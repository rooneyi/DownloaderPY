from pytube import YouTube
import tkinter


def downloader():
    url = url_entry.get()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    # Juste pour montrer que le programme est en train de travailler
    print(video.filesize)
    print(video.title)

    video.download()


fenetre = tkinter.Tk()
fenetre.geometry("600x600")
fenetre.title("Downloader")
url_label = tkinter.Label(fenetre, text="url de la video :")
url_label.pack()

url_entry = tkinter.Entry(fenetre)
url_entry.pack()
telecharger_buttob = tkinter.Button(fenetre, text="Telecharger", command=downloader)

telecharger_buttob.pack()
fenetre.mainloop()
