from datetime import datetime
import time
import os
import subprocess as sb
import logging



## Configure logging

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename="/mnt/shared_hdd/rpi_backups/backuplog.txt", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


## Configure timestamp
# dd/mm/YY H:M:S
now = datetime.now()
date_string = now.strftime("%d-%m-%Y-%H%M")


### configure directories and file names

source = "/home/" # home folder
# destination directory
target = "/mnt/shared_hdd/rpi_backups/home_backups/" ## external hdd
#configuring the filename for the backup tar file
filename = f"{target}backup-{date_string}.tgz"


# #check if the folder exists
def sourceExists():
    if os.path.exists(source) == True:
        return source
    else:
        logger.error("The source directory doesn't exist")
        print("The source directory doesn't exist")
        exit()




## Configure functions for the backup


def createArchive(source, filename):
    logging.info(f"Backup started on " + source)
    print(f"Backup started on " + source)
    try:
        p1 = sb.run(['tar','-a','-cf', filename,  source])
        logging.info("Home folder backup successful.")
        print("Home folder backup successful.")
    except:
        logging.error(f"An exception occurred.")


def backupFileSystem():
    p2 = sb.run(['sudo', 'timeshift', '--create', '--comments', f'{date_string}', '--tags', 'D', '--snapshot-device', '/dev/sda1'])
    logging.info("File system backup successful.")
    


def cleanup():
    p3 = sb.run(['tar','-a','-cf', f'/mnt/shared_hdd/rpi_backups/snapshots/snapshot-{date_string}.tgz','/mnt/shared_hdd/timeshift/'])
    cleanup = sb.run(['rm', '-rf', '/mnt/shared_hdd/timeshift/'])

while os.path.exists('/mnt/shared_hdd/timeshift/'):
    time.sleep(1)

if __name__ == "__main__":
    createArchive(
        sourceExists(), filename
    )
    backupFileSystem()
    while not os.path.exists('/mnt/shared_hdd/timeshift/'):
        time.sleep(1)
    cleanup()
    logging.info("All backups and cleanup successful")
    # pass
