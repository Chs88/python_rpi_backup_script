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


### configure directory paths and file names

#source to back up
source = "/home/" # home folder
# destination directory
target = "/mnt/shared_hdd/rpi_backups/" ## external hdd
#configuring the filename for the backup tar file
home_tar_filename = f"{target}/home_backups/backup-{date_string}.tgz"
# configuring destination snapshot device for timeshift
snapshot_device = '/dev/sda1/'
#snapshot target
snapshot_source = '/mnt/shared_hdd/timeshift/'


# #check if the folder exists
def source_exists():
    if os.path.exists(source) == True:
        return source
    else:
        logger.error("The source directory doesn't exist")
        print("The source directory doesn't exist")
        exit()




## Configure functions for the backup


def create_archive(source, filename):
    logging.info(f"Backup started on " + source)
    print(f"Backup started on " + source)
    try:
        p1 = sb.run(['tar','-a','-cf', filename,  source])
        logging.info("Home folder backup successful.")
        print("Home folder backup successful.")
    except:
        logging.error(f"An exception occurred.")


def backup_file_system():
    p2 = sb.run(['sudo', 'timeshift', '--create', '--comments', f'{date_string}', '--tags', 'D', '--snapshot-device', f'{snapshot_device}'])
    logging.info("File system backup successful.")
    

##creating function that deletes old archives

def delete_oldest(folder):
    list_of_files = os.listdir(folder)
    os.chdir(folder)
    if len(list_of_files) >= 4: ## if there are 4 or more files
        oldest_file = min(list_of_files, key=os.path.getctime)
        os.remove(os.path.abspath(oldest_file))
    


def clean_up():
    p3 = sb.run(['tar','-a','-cf', f'/mnt/shared_hdd/rpi_backups/snapshots/snapshot-{date_string}.tgz',f'{snapshot_source}'])
    cleanup = sb.run(['rm', '-rf', f'{snapshot_source}'])





if __name__ == "__main__":
    create_archive(
        source_exists(), home_tar_filename
    )
    backup_file_system()
    while not os.path.exists(f'{snapshot_source}'):
        time.sleep(1)
    clean_up()
    delete_oldest(target + '/home_backups/')
    delete_oldest(target + '/snapshots/')
    logging.info("All backups and cleanup successful")
    # pass
