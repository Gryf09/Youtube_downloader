# %%
from pytube import YouTube
from mp3_add_thumbnail import add_thumbnail
from moviepy.editor import AudioFileClip
import os, shutil, requests

def download_thumbnail(yt_vid):
	def has_highres_thumbnail(thumbnail_url):
		response = requests.head(thumbnail_url)
		return response.status_code == 200
	
	thumbnail_default_url = yt_vid.thumbnail_url
	if "sddefault" in thumbnail_default_url:
		thumbnail_highres_url = thumbnail_default_url.replace("sddefault", "maxresdefault")
		thumbnail_url_todownload = thumbnail_highres_url if has_highres_thumbnail(thumbnail_highres_url) else thumbnail_default_url
	
	response = requests.get(thumbnail_url_todownload)
	print(thumbnail_url_todownload)
	file = open("thumbnail.png", "wb")
	file.write(response.content)
	file.close()

def convert_mp4_to_mp3(filename):
	videoclip = AudioFileClip(filename)
	audioclip = filename.replace(".mp4", ".mp3")
	videoclip.write_audiofile(audioclip)
	videoclip.close()
	return audioclip

# %%
if __name__ == '__main__':
	yt_page = input("Insert Youtube URL: ")
	yt_vid = YouTube(yt_page)
	print(yt_vid.title)

	streams = yt_vid.streams.filter(only_audio=True).order_by('abr').desc()
	stream = streams.first()
	video_filepath = stream.download()

	# Convert MP4 to MP3
	# video_filepath = f"{yt_vid.title}.{stream.subtype}"
	mp3_filepath = video_filepath.replace(stream.subtype, '.mp3')
	print(mp3_filepath)

	video = AudioFileClip(video_filepath)
	video.write_audiofile(mp3_filepath)
	os.remove(video_filepath)


	# %%
	print('File downloaded')

	download_thumbnail(yt_vid)
		
	try:
		add_thumbnail(mp3_filepath, "thumbnail.png")
		print("Thumbnail added")
	except:
		print("ERROR \nThumbnail not added")

	os.remove("thumbnail.png")
	# %%
	output_path = r"E:\Muzyka\Do przesłuchania"

	# delete ' " : ? | signs from title as it will cause error when moving files
	mp3_title = yt_vid.title.replace('\"', '').replace('\'', '').replace(':', '').replace('?', '').replace('|', '')
	print(mp3_title)
	
	try:
		shutil.move(mp3_filepath, os.path.join(output_path, mp3_title + '.mp3'))
		print('File moved')		
	except Exception as exc:
		print("Ooops, File not moved, here comes an exception: ", exc)
	input('Press Enter to escape...')
