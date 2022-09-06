import ctypes
import time
import os
def main(User_input, time_input = 30):
    SPI_SETDESKWALLPAPER = 20
    time_loop = time_input #seconds
    time_current = time.time()
    count = 0
    file_path = "[replace with absolute path of gif folder]" + "/" + User_input.strip()
#example of absolute path would be: "C:\Users\Yor PC\Desktop\HomeScreen Gif\Gif Pictures"
    if os.path.isdir(file_path):
        os.chdir(file_path)
        files = filter(os.path.isfile, os.listdir(file_path))
        files = [os.path.join(file_path, f) for f in files]
        files.sort(key=lambda x: os.path.getmtime(x))
        len_file_dir = len(files)-1
        for file in range(len(files)):
            files[file] = files[file].split(file_path)[1]
        print("Close the code to stop the gif")
        while time.time() - time_current <= time_loop:
            inner_time = time.time()
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (file_path+files[count%len_file_dir]), 1)
            count += 1
            while time.time() - inner_time <= 0.075:
                continue
    else:
        print("Not Found")

User_input = input("Provide a gif name from the folder: ").lower()
try:
    time_input = int(input("Provide a time in seconds to loop gif: "))
    main(User_input, time_input)
except:
    print("Oops...something's wrong")

