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


### configure directories and file names

source = "/home/chs88/Desktop/Practice_Projects"
# destination directory
target = "/home/chs88/scripts_backup/" 
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
        p1 = sb.run(['tar','-a','-cf', filename,  source], capture_output=True, text=True,)
        logging.info("Backup successful.")
    except:
        logging.error(f"An exception occurred.")

    



if __name__ == "__main__":
    createArchive(
        sourceExists(), filename
    )
    # pass
