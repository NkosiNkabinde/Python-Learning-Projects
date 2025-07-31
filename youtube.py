from pytube import YouTube
from pytube import SearchVideo
from pytube import Playlist
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive =True, file_extension='mp4') #.order_by('resolution').desc().first()
        highest_res_stream = streams.get_highest_resolution
        highest_res_stream.download(output_path =save_path)
        print(f"Video downloaded successfully at {save_path}")



    except Exception as e :
        print(f"An error occurred: {e}")

url = "https://www.youtube.com/watch?v=WlwHvhIIVmc&list=RDWlwHvhIIVmc&start_radio=1"


download_video(url)





