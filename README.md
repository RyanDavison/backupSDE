# backupSDE
A small script that backs up all features in an [ESRI SDE](http://downloads.esri.com/support/documentation/sde_/706Understanding_ArcSDE.pdf) database to a file geodatabase. The script
uses the arcpy library to create the backup output geodatabase and do the
actual copying into it from an SDE location.

##Use
Before running BackupSDE.py, you will want to modify two variables. The
*outFolderPath* is just a user defined path to the location you want your
backup to be housed in. *arcpy.env.workspace* is arcpy's workspace environment
variable. You can set it by replacing **[SDE User Name]** with the name of
your SDE connection.

##Alternative Use Method
Rather than locating the python file and running it manually every time you
want to backup your SDE, you could always [add the script to an ArcGIS toolbox](http://desktop.arcgis.com/en/arcmap/10.3/analyze/creating-tools/adding-a-script-tool.htm) and run it from ArcCatalog or ArcMap.
