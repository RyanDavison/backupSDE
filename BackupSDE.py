############################################################################################################################################################################################
##BackupSDE.py
##
##Author: Ryan Davison
##
##
##
##Purpose: This script copies all SDE feature datasets and their contents to a
##file geodatabase in a different location.
##
##This script can be used as is or incorporated into ArcCatalog as a one-click
##geoprocessing tool.
##
##The user of this tool needs to change the outFolderPath and the env.workspace
##variables
############################################################################################################################################################################################

#Import modules.
import arcpy, os, datetime
from arcpy import env

#Set the arcpy environment to allow overwriting of existing data.
arcpy.env.overwriteOutput = True

#Replace the path below with a path to your own backup location.
outFolderPath = r"[Path_to_Backup_Folder\\]"

#Create an output geodatabase to hold your backup.
#The geodatabase name will be constructed using the current date.
created = datetime.date.today()
created = created.strftime("%y%m%d")
outName = "SDEbackup" + created + ".gdb"

#Create the output geodatabase.
arcpy.CreateFileGDB_management(outFolderPath, outName)

#Set the workspace to your SDE instance that you want to copy.
arcpy.env.workspace = r"Database Connections\[SDE User Name].sde"

#Create a list of all datasets in the SDE
fdList = arcpy.ListDatasets("", "Feature")

#Copy each feature from the SDE to the backup database
for ds in fdList:
    outData = outFolderPath + outName + "\\" + ds
    dataType = "FeatureDataset"
    arcpy.Copy_management(ds, outData, dataType)






