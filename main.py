from pytube import YouTube
from moviepy.editor import *

def telecharger_et_convertir(url, chemin_sortie):
    try:
        # Téléchargement
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_path = video.download(output_path=chemin_sortie, filename="video_temp")

        # Conversion en .mov
        clip = VideoFileClip(video_path)
        clip.write_videofile(f"{chemin_sortie}/video_convertie.mov", codec="libx264")

        # Supprimer le fichier temporaire mp4
        os.remove(video_path)
        print("Téléchargement et conversion terminés.")
    except Exception as e:
        print("Une erreur est survenue :", e)

# Utilisation de la fonction
url_video = "https://www.youtube.com/watch?v=IIAlkQEw8Gc&ab_channel=MaxCodez"
chemin_sortie = "D:\alpha\Documents\Programation\python\mov-youtube-downloader"
telecharger_et_convertir(url_video, chemin_sortie)
