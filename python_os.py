'''This is a project that makes different folders for files with different
extensions '''
import os 

folder_path  =  os.path.join(os.getcwd(),"new_folder")
files = os.listdir("new_folder")

if not os.path.exists(folder_path+"/text_only"):
    os.makedirs(folder_path+"/text_only")
if not os.path.exists(folder_path+"/jpg_only"):
    os.makedirs(folder_path+"/jpg_only")
if not os.path.exists(folder_path+"/docx_only"):
    os.makedirs(folder_path+"/docx_only")

for file in files:
    file_path = os.path.join(folder_path,file)
    if os.path.isfile(file_path):
        if os.path.splitext(file_path)[-1] == ".txt":
            os.rename(file_path,folder_path+"/text_only/"+file)
        if os.path.splitext(file_path)[-1] == ".jpg":
            os.rename(file_path,folder_path+"/jpg_only/"+file)
        if os.path.splitext(file_path)[-1] == ".docx":
            os.rename(file_path,folder_path+"/docx_only/"+file)