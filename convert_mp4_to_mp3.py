from moviepy.editor import *

def convert_mp4_to_mp3(filename):
	videoclip = AudioFileClip(filename)
	audioclip = filename.replace(".mp4", ".mp3")
	videoclip.write_audiofile(audioclip)
	videoclip.close()
	return audioclip

if __name__ == '__main__':
	videoclip = "Solange - Losing You (Cyril Hahn Remix).mp4"
	convert_mp4_to_mp3(videoclip)
