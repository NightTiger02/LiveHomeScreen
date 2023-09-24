import os
from moviepy.editor import VideoFileClip
print("Make sure you have a \'Gif Pictures\' folder next to this file")
#gif to img converter:
def GifToImg(name_gif, clip, start_time=0, end_time=0):
    #NewFolder
    name = name_gif.split(".")[0]
    path = "Gif Pictures/"+name
    if os.path.isdir(path) == False:
        if start_time > end_time:
            print("Invalid time slots")
            print("Entire file will be converted")
            start_time = 0
            end_time = clip.duration
        os.makedirs(path)
        duration = end_time
        frame = start_time
        count = 1
        print("Converting...")
        while frame <= duration:
            clip.save_frame(path+"/frame"+str(count)+".png", t = frame)
            count += 1
            frame += 0.08
        print("Done")
    else:
        print("Folder with name \'"+name+"\' exists")
        print("Pictures cannot be saved")
print("Keep the gif next to the python file before proceeding")
name_gif = input("Enter the entire gif name: ").strip()
try:
    clip = VideoFileClip(name_gif)
except:
    print("Could not find gif")
if input("Write \"Yes\" if you have a specific time slots of the clip: ").strip().lower() == "yes":
    try:
        start_time = int(input("Enter the start time: "))
        end_time = int(input("Enter the end time: "))
    except:
        print("Invalid time slots")
        print("Entire file will be converted")
else:
    start_time = 0
    end_time = clip.duration
GifToImg(name_gif, clip, start_time, end_time)
