from Musicbot.Command import Commands
import threading
import time
import subprocess
import os
from Musicbot.formatting import fprint
class MusicBot(Commands):
    def __init__(self, video_folder):
        super().__init__(video_folder)
    
    def bot(self):
        while True:
            files = self.get_files_in_folder()
            if files == []:
                time.sleep(1)
            else:
                index = self.data["playing_no."]
                data = self.data
                if data["is_paused"] is False:
                    self.play(files[index-1])
                    #after audio played
                    data = self.data
                    index = self.data["playing_no."]
                    if data["quit"]:
                        fprint("green", "Music bot Quitting")
                        break
                    if data["is_loop"] and data["is_paused"] == False:
                        index += 1
                    elif data["is_loop"] == False and data["is_paused"] == False:
                        index = 1
                        os.remove(files[index-1])

                    if data["is_loop"] == False and data["skip"]:
                        index = 1
                        os.remove(files[index-1])
                    
                    if data["skip"]:
                        self.data["skip"] == False
                    
                    self._update_files_no()
                    files = self.get_files_in_folder()
                    index = ((index-1) % len(files)) + 1
                    self.data["playing_no."] = index
                else:
                    time.sleep(1)

if __name__ == "__main__":
    musicbot = MusicBot(video_folder="/Users/Joshua/Vscode/Python/Youtube/video_files")
    thread = threading.Thread(target=musicbot.bot)
    thread.start()
    print("music bot query starting")
    musicbot.query()