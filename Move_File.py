
import os
import shutil

from_dir = "C:\\Users\\user\\Downloads"
to_dir = "C:\P102\Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for P102_example in list_of_files:

    name, extension = os.path.splitext("C:\\Users\\user\\Downloads\\P102_example")
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir+'/'+P102_example
        path2 = to_dir+'/'+"Document_Files"
        path3 = to_dir+'/'+"Document_Files"+'/'+P102_example

        if os.path.exists(path2):
            print("Moving"+P102_example+".....")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving"+P102_example+".....")
            shutil.move(path1,path3)




