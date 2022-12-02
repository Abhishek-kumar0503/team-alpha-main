# Import everything needed to edit video clips
from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("Are you following your dreams - 6 Minute English.mp4")
  
# getting only first 5 seconds
clip = clip.subclip(0, 379)
  
# loading audio file
audioclip = AudioFileClip("output01.mp3").subclip(0, 379)
  
# adding audio to the video clip
videoclip = clip.set_audio(audioclip)
  
# showing video clip
videoclip.ipython_display()