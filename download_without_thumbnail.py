from pytube import YouTube
import os
import shutil
import requests

if __name__ == '__main__':
	yt_page = input("Insert Youtube URL: ")
	yt_vid = YouTube(yt_page)
	print(yt_vid.title)
	print(yt_vid.streams.filter(only_audio=True).last())
	stream = yt_vid.streams.filter(only_audio=True).get_audio_only()

	file = stream.download()
	base, ext = os.path.splitext(file)
	new_file = base + '.mp3'
	os.rename(file,new_file)
	print('File downloaded')

	output_path = r"E:\Muzyka\Do przesłuchania"
	shutil.move(new_file, output_path)
	print('File moved')
