import os 
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os_module import getall,moving
class myEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        time.sleep(5)
        print(event)
        moving()

def getall():
    default_folders = ['PDFs','Images','Zip,Rar','DOCs','EXE','ISO','Torrent & FDM','All Folders','All Others','Media']
    path = r'E:\Downloads'
    destination = r'E:\Downloads\All_Folders'


    all_pdfs = []
    all_images = []
    all_compressed = []
    all_docs = []
    all_exe = []
    all_iso = []
    all_others = []
    all_torrent_fdm = []
    all_media = []
    all_folders = []
    formats_image = ['.jpg','.png','jpeg','.ai','.bmp','.gif','.ico','.psd']
    formats_media = ['.avi','.flv','.mkv','.mov','.mp4','.wmv','.mp3']
    formats_compressed = ['.zip','.rar']
    formats_docs = ['.docx','.xlsx','.doc','.docm','.dot','.xml','.txt','.pdf','.csv','.json','.html',] 
    formats_exe = ['.exe','.msi']
    formats_iso = ['.iso']  
    formats_torrent_fdm = ['.torrent','.fdmdownload','.crdownload']
    for i,j,k in os.walk(path):
        for folder in j:
            if folder not in default_folders:
                all_folders.append(folder)

        for file in k:
            ext = os.path.splitext(file)[-1]
            if ext == '.pdf':
                all_pdfs.append(file)
            elif ext in formats_image:
                all_images.append(file)
            elif ext in formats_compressed:
                all_compressed.append(file)
            elif ext in formats_docs:
                all_docs.append(file)
            elif ext in formats_exe:
                all_exe.append(file)
            elif ext in formats_iso:
                all_iso.append(file)
            elif ext in formats_torrent_fdm:
                all_torrent_fdm.append(file)
            elif ext in formats_media:
                all_media.append(file)

            else:
                all_others.append(file)


        
        break

    data = {'PDFs':all_pdfs,'Images':all_images,'Zip,Rar':all_compressed,'DOCs':all_docs,'EXE':all_exe,'ISO':all_iso,'Torrent & FDM':all_torrent_fdm,'All Folders':all_folders,'All Others':all_others,'Media':all_media}

    return data



def moving():
    all_data = getall()

    path = r'E:\Downloads'
    def foreach(path,id):
        for file in all_data.get(id):
            source = os.path.join(path,file)
            final_destination = os.path.join(path,id)

            file_path = os.path.join(final_destination,file)
            os.makedirs(final_destination,exist_ok=True)
            if os.path.isfile(file_path):
                print('duplicate')
                without_ext = os.path.splitext(file)[-2]
                ext = os.path.splitext(file)[-1]
                without_ext = without_ext + '(1)'
                new_file = without_ext + ext
                print(new_file)

                final_destination = os.path.join(path,new_file)

                print(source)
                shutil.move(source,final_destination)
            else:
                shutil.move(source,final_destination)
    for key in all_data.keys():
        foreach(path,key)


if __name__ == "__main__":


    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    path = r'E:\Downloads'
    event_handler = myEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
