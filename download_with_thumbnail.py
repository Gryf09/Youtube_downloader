# %%

from pytube import YouTube
from mp3_add_thumbnail import add_thumbnail
from convert_mp4_to_mp3 import convert_mp4_to_mp3
import os
import shutil
import requests

def download_thumbnail(yt_vid):
	thumbnail_url = yt_vid.thumbnail_url
	# if thumbanil res is small, change to max res
	if "sddefault" in thumbnail_url:
		thumbnail_url = thumbnail_url.replace("sddefault", "maxresdefault")
		print("Thumbnail changed to maxresdefault")
	
	response = requests.get(thumbnail_url)
	print(thumbnail_url)
	file = open("thumbnail.png", "wb")
	file.write(response.content)
	file.close()

# %%
if __name__ == '__main__':
	yt_page = input("Insert Youtube URL: ")
	yt_vid = YouTube(yt_page)
	print(yt_vid.title)
	print(yt_vid.streams.filter(only_audio=True).last())
	stream = yt_vid.streams.filter(only_audio=True).get_audio_only()

	file = stream.download()
	audio_filepath = convert_mp4_to_mp3(file)
	print(audio_filepath)
	os.remove(file)
	print('File downloaded')

	download_thumbnail(yt_vid)
		
	try:
		add_thumbnail(audio_filepath, "thumbnail.png")
		print("Thumbnail added")
	except:
		print("ERROR \nThumbnail not added")

	os.remove("thumbnail.png")
	# %%
	output_path = r"E:\Muzyka\Do przesłuchania"

	# delete ' and " from title as it will cause error when moving files
	mp3_title = yt_vid.title.replace('\"', '').replace('\'', '')
	print(mp3_title)
	
	try:
		shutil.move(audio_filepath, os.path.join(output_path, mp3_title + '.mp3'))
		print('File moved')		
	except Exception as exc:
		print("Ooops, File not moved, here comes an exception: ", exc)
	input('Press Enter to escape...')
	