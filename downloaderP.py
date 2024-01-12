from pytube import YouTube

url = "https://www.youtube.com/watch?v=VSyORTdmVoU"

yt = YouTube(url)

print("TITRE : " + yt.title)
print("DESCRIPTION : " + str(yt.description))
print("DUREE : " + str(yt.length) + " secondes")
print("AUTEUR : " + yt.author)
print("VUES : " + str(yt.views))
print("NOTE : " + str(yt.rating))
print("TAGS : " + str(yt.keywords))
print("DATE DE PUBLICATION : " + yt.publish_date.strftime("%d/%m/%Y"))
print("URL : " + url)
print("FORMATS DISPONIBLES : " + str(yt.streams.filter(progressive=True)))

downloaded_stream = yt.streams.get_highest_resolution()
print("Téléchargement de la vidéo en cours...") # Juste pour montrer que le programme est en train de travailler
downloaded_stream.download()