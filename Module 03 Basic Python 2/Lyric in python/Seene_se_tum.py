from time import sleep
from playsound import playsound
from threading import Thread
song_path=r"P:\Phitron\SDT\Python\Module 03 Basic Python 2\Lyric in python\song.mp3"

def play():
    playsound(song_path)
    
Thread(target=play,daemon=True).start()
RED = "\033[31m"
GREEN = "\033[32m"
MA="\033[35m"
RESET = "\033[0m"

sleep(4.5)
print(RED+ "Seene se tum mere Aake lag jaao na" +RESET)
sleep(6.3)
print(MA+"Darte ho kyon"+RESET)
sleep(1.8)
print(GREEN+"Zara paas toh aao na"+RESET)
sleep(5)




