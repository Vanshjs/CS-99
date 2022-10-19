import os
import shutil
import time

def main():
    deleted_folder_count=0
    deleted_files_count=0
    path=r"D:\Vansh\Module3\Projects\Project99\demo"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >=getage(root_folder):
                remove_folder(root_folder)
                deleted_folder_count +=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds >=getage(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_count += 1
                for file in files:
                    file_path=os.path.join(root_folder, file)
                    if seconds >=getage(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1

        else:
            if seconds >=getage(path):
                remove_file(path)
                deleted_files_count += 1

    else:
        print(f'"{path}" is not found')
        deleted_files_count += 1
        print(f"Total folders deleted:{deleted_folder_count}")
        print(f"Total files deleted:{deleted_files_count}")

def remove_folder(path):

    if not shutil.rmtree(path):
        print(path+"is removed successfully")
    else:
        print(f"Unable to delete the "+path)
def remove_file(path):

    if not os.remove(path):
        print(f"{path} is removed successfully")

    else:
        print("Unable to delete the " + path)

def getage(path):
    ctime = os.stat(path).st_ctime
    return ctime
main()