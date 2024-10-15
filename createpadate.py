import os
from datetime import datetime

class FolderCreator:
    def __init__(self,path):
        self.current_datetime = datetime.now()
        self.folder_name = self.current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        self.path = path

    def create_folder(self):
        folder_p = os.path.join(self.path,self.folder_name)
        os.mkdir(folder_p)
        print(f"Folder {folder_p} create")
        return folder_p