############################################################################################################################################################################################
##BackupSDE.py
##
##Author: Ryan Davison
##        
##
##
##Purpose: This script copies all SDE feature datasets and their contents to a file geodatabase in a different location. 
##
##This script can be used as is or incorporated into ArcCatalog as a one-click geoprocessing tool.
##
##
############################################################################################################################################################################################

####BEGIN SCRIPT

#Import modules.
import arcpy, os, datetime
from arcpy import env


arcpy.env.overwriteOutput = True
outFolderPath = r"[Path_to_Backup_Folder\\]"
created = datetime.date.today()
created = created.strftime("%y%m%d")
outName = "SDEbackup" + created + ".gdb"


arcpy.CreatePersonalGDB_management(outFolderPath, outName)


arcpy.env.workspace = r"Database Connections\[SDE User Name].sde"
fdList = arcpy.ListDatasets("", "Feature")


for ds in fdList:
    outData = outFolderPath + outName + "\\" + ds
    dataType = "FeatureDataset"
    arcpy.Copy_management(ds, outData, dataType)

####END SCRIPT






