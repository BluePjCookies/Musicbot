import threading
from Musicbot.bot import MusicBot

musicbot = MusicBot(video_folder="") #path to video_folder
thread = threading.Thread(target=musicbot.bot)
thread.start()
print("music bot query starting")
musicbot.query()