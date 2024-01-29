import queue
from formatting import fprint
import os
from pytube import Search
import subprocess
class Commands:
    def __init__(self, video_folder : str = None):
        self.video_folder = video_folder
        if os.path.exists(self.video_folder) is False:
            raise Exception("Provide a path to video folder")

        self.data = {
            "is_loop" : False,
            "quit" : False,
            "playing_no." : 1,
            "is_paused" : False,
            "skip" : False
        }
        self.process = None
    
    def get_files_in_folder(self):
        files = os.listdir(self.video_folder)
        if ".DS_Store" in files: #this is a really bad problem that apple have
            files.remove(".DS_Store")
        files.sort(key=lambda x : int(x.split(".")[0]))
        files_full_path = [self.video_folder + f"/{file}" for file in files]
        return files_full_path
    
    def get_number_and_filename(self, file_full_path):
        file_name = file_full_path.replace(self.video_folder, "")[1:]
        number = int(file_name.split(".")[0])
        file_name = file_name.replace(f"{str(number)}.", "")
        return number, file_name
    
    def query(self):
        while True:
            query = input("Search a Song/queue(q): ").lower()
            if query == "":
                pass
            elif query == "q" or query == "queue":
                files = self.get_files_in_folder()
                
                data = self.data
                for file in files:
                    number, file_name = self.get_number_and_filename(file)
                    if number == data["playing_no."]:
                        fprint("green", str(number), ". ", "reset", "underline", file_name)
                    else:
                        fprint("green", str(number), ". ", "reset", file_name)
            elif query == "clear":
                self._clear()

            elif "remove" in query:
                number = query.replace("remove", "").strip()
                if number.isnumeric():
                    self._remove_file(int(number))
                else:
                    self._download_audio(query)
                    
            elif query == "loop":
                self._loop()
            
            elif query == "quit":
                self._quit()
                break
            
            elif query == "pause":
                self._pause()
            
            elif query == "play":
                self._play()
            
            elif query == "skip":
                self._skip()

            elif query == "data":
                data = self.data
                fprint("green", data)
            
            


            else:
                self._download_audio(query)
            
            self._update_files_no()


    def _update_files_no(self):
        files = self.get_files_in_folder()
        for index, file_path in enumerate(files):
            number, file_name = self.get_number_and_filename(file_path)
            audio_file = f"{str(index + 1)}.{file_name}"
            if os.path.exists(file_path):
                os.rename(file_path, f"{self.video_folder}/{audio_file}")
    
    def _remove_file(self, num : int):
        
        files = self.get_files_in_folder()
        data = self.data
        playingnum = data["playing_no."]
        if num == playingnum or num > len(files):
            return None
        elif num < playingnum:
            self.data["playing_no."] -= 1 
        file_path_to_remove = files[num-1]
        number, file_name = self.get_number_and_filename(file_path_to_remove)
        fprint("Removing ", "underline", "green", file_name)
        os.remove(file_path_to_remove)
    
    def _download_audio(self, query : str):
        try:
            files_len = len(self.get_files_in_folder())
            s = Search(query).results[0]
            print(s.title)
            tag = list(s.streams.filter(only_audio=True).itag_index)[0]
            stream = s.streams.get_by_itag(tag)
            print("Downloading")
            stream.download(output_path=self.video_folder, filename_prefix=f'{str(files_len+1)}.', max_retries = 15)
            print("Download success")
            
        except Exception as e:
            print(e)
    
    def _clear(self):
        files = self.get_files_in_folder()
        num = self.data["playing_no."] - 1
        for i in range(0, len(files)):
            if i == num:
                continue
            os.remove(files[i])
    
    def _loop(self):
        if self.data["is_loop"]:
            self.data["is_loop"] = False
            fprint("green", "Setting loop to False")
        else:
            self.data["is_loop"] = True
            fprint("green", "Setting loop to True")
        

    def _quit(self):
        self.data["quit"] = True
        fprint("green", "Commands quitting")
        self.process.terminate()
    
    def _pause(self):
        self.data["is_paused"] = True
        fprint("green", "Pausing Video")
        self.process.terminate()
        
    def _play(self):
        self.data["is_paused"] = False
        fprint("green", "Playing video")
    
    def _skip(self):
        self.data["skip"] == True
        files = self.get_files_in_folder()
        for file in files:
            num, file_name = self.get_number_and_filename(file)
            if self.data["playing_no."] == num:
                fprint("green", "skipping ", str(num), ".", file_name)
                self.process.terminate()
                return None


    
    def play(self, file):
        self.process = subprocess.Popen(["afplay", file])
        self.process.wait()

    
if __name__ == "__main__":
    c = Commands("/Users/Joshua/Vscode/Python/Youtube/video_files")

    c.query()


#imma about to commit some big changes.