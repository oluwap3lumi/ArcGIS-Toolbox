import arcpy
import os

gdb_folders = r"C:\Users\ayoaj\Desktop\IBEDC HEAD OFFICE\GIS DATA\DOMAIN (2)\DOMAIN\OGUN DOMAIN GDB"

for dirpath, dirnames, filenames in os.walk(gdb_folders):
    for dirname in dirnames:
        if dirname.endswith(".gdb"):
            gdb_path = os.path.join(dirpath, dirname)
            print(f"\nProcessing GDB: {gdb_path}")
            arcpy.env.workspace = gdb_path

            for feature_class in arcpy.ListFeatureClasses():
                print(f"  Checking Feature Class: {feature_class}")
                desc = arcpy.Describe(feature_class)

                # Enable attachments if not already enabled
                print("    Enabling Attachments...")
                arcpy.management.EnableAttachments(feature_class)

                # Add GlobalIDs if not present
                print("    Adding GlobalIDs...")
                arcpy.management.AddGlobalIDs(feature_class)

                # Enable editor tracking
                print("    Enabling Editor Tracking...")
                arcpy.management.EnableEditorTracking(
                    feature_class,
                    "created_user", "created_date",
                    "last_edited_user", "last_edited_date",
                    "ADD_FIELDS", "LOCAL"
                )