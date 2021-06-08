#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/student/mycode/")

#copy file to backup file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy entire folder & create it if it doesn't exit
shutil.copytree("5g_research/", "5g_research_backup/")
