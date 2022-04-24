from datetime import datetime
import os
import subprocess as sb
import logging



## Configure logging

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename="/home/chs88/scripts_backup/backuplog.txt", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


## Configure timestamp
# dd/mm/YY H:M:S
now = datetime.now()
date_string = now.strftime("%d-%m-%Y-%H:%M")


## configure directories and file names

#check if the folder exists
def wdirExists():
    try:
        os.chdir("/home/chs88/Desktop/Practice_Projects")
    except:
        logging.error("Working directory doesn't exist")
    else:
        os.chdir("/home/chs88/Desktop/Practice_Projects")
        wdir = os.getcwd() ## working directory
        return wdir

# destination directory
ddir = "/home/chs88/scripts_backup/" 
#configuring the filename for the backup tar file
filename = f"{ddir}backup-{date_string}"




## Configure functions for the backup


def createArchive(wdir, filename):
    logging.info(f"Backup started on " + wdir)
    print(f"Backup started on " + wdir)
    try:
        p1 = sb.run(['tar', '-cvf', filename,  wdir], capture_output=True, text=True,)
        logging.info("Backup successful.")
    except:
        logging.error(f"An exception occurred.")

    



if __name__ == "__main__":
    createArchive(
        wdirExists(), filename
    )
    # pass
