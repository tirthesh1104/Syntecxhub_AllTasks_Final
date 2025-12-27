import shutil
import os
from datetime import datetime

source = input("Source folder path: ")
destination = input("Backup folder path: ")

time = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(destination, "backup_" + time)

shutil.copytree(source, backup_path)
print("Backup completed:", backup_path)
