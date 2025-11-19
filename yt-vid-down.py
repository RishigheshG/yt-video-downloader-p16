from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
  try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Title: {yt.title}")
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path = save_path)
    print("Download completed!")

  except Exception as e:
    print(e)

def open_file_dialog():
  folder_selected = filedialog.askdirectory()
  if folder_selected:
    print(f"Selected folder: {folder_selected}")
  return folder_selected

if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()  # Hide the root window
  video_url = input("Enter the YouTube video URL: ")
  save_directory = open_file_dialog()
  if save_directory:
    download_video(video_url, save_directory)
    print("Video downloaded successfully!")
  else:
    print("No folder selected. Exiting.")
