import threading
from bot import MusicBot
from formatting import fprint
musicbot = MusicBot(video_folder="/Users/Joshua/Vscode/Python/Youtube/Musicbot/video_folder") #path to video_folder
thread = threading.Thread(target=musicbot.bot)
thread.start()
fprint("underline", "bold", "green", "Music bot query starting")
musicbot.query()