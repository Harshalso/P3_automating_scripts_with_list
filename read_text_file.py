import os
folder_path = r"C:\Users\HARSHAL\Downloads"
file_name = "Answer.txt"
file_path = os.path.join(folder_path,file_name)
file_obj = open(file_path, "r")
print(file_obj.read())

