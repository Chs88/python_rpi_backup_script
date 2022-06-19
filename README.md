# python_rpi_backup_script
## Introduction
This short and basic script was created as a practice in Python scripting. 
The script creates an archive of the /home directory of the system (A raspberry pi running Ubuntu server 20 in my personal case), compresses it in a tar.gz file and saves it on an external HDD. 
I've also used [timeshift](https://github.com/teejee2008/timeshift) which is a system restore tool for Linux. I've used this to create snapshots of the entire filesystem. 
All variable names, directory names and hard drive names are specific to my personal case.
## Libraries used
- datetime (To set timestaps for the archive files)
- time (To use the sleep() function to wait for some commands to finish running)
- os (Used for pathing and listing directories)
- subprocess (Used for running the bash commands)
- logging (I use this to creat logs for the script)
