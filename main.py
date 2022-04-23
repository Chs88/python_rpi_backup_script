import variables
import os
import subprocess as sb
import logging


## configure directories

os.chdir("/home/chs88/Desktop/Practice_Projects")
wdir = os.getcwd() ## working directory
# ddir =  ## destination directory


## Configure logging

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename=os.path.join(wdir, "BACKUP/backuplog"), level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


## Configure functions for the backup

#Find existing backup file:

def findBackup(name, path):
    file_name = os.path.join(path, name)
    exists = os.path.exists(file_name)
    if exists == True:
        

    

def createArchive(directory, file_name):
    number = 0
    logging.info(f"Backup started on " + wdir)
    p1 = sb.run(['tar', '-cvf', f"{file_name}{number}",  directory], capture_output=True, text=True,)
    # logging.info(f"Backing up " + wdir)
    logging.info("Backup successful.")
    





if __name__ == "__main__":
    createArchive(wdir)
    # pass
