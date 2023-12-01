# NOT WORKING!!!!
# countdown.py - A simple countdown script.
import time, subprocess
timeLeft = 60
while timeLeft > 0:
 print(timeLeft, end='')
 time.sleep(1)
 timeLeft = timeLeft - 1
# TODO: At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'c:\Users\Bruker\OneDrive\Desktop\MusicDownloader\Fuse ODG - No Daylight (Official Video) #AFROJAM.mp3'], shell=True)