
import os



def here_we_go():
        for filename in os.listdir(folder_track):
                
            extension_file = filename.split('.')
            print(extension_file)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "mp3"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Mysic/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "exe"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Progi/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "py"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Py_file/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "torrent"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Torrent/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "whl"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/File_dlia_python/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "msi"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/File_win/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "zip" or extension_file[-1].lower() == "iso" or extension_file[-1].lower() == "rar"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Arxiv/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "mp4" or extension_file[-1].lower() == "mov" or extension_file[-1].lower() == "avi"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Videos/" + filename
                os.rename(file, new_path)

            if len(extension_file) > 1 and (extension_file[-1].lower() == "jpg" or extension_file[-1].lower() == "png" or extension_file[-1].lower() == "svg" or extension_file[-1].lower() == "psd"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Photos/" + filename
                os.rename(file, new_path)

   

folder_track = 'C:/Users/Dmitriy/Downloads'
folder_dest = 'C:/Users/Dmitriy/Downloads/mu_file'
       

if __name__ == '__main__':
    here_we_go()