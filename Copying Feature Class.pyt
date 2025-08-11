# -*- coding: utf-8 -*-

import arcpy
import os


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Copying Feature Class"
        self.alias = "Copying Feature Class"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Copying Feature Class in a folder of GDBs"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params = [
            arcpy.Parameter(
                displayName = "Feature Class Name",
                name = "Feature Class Name",
                datatype = "DEFeatureClass",
                parameterType = "Required",
                direction = "Input",
                multiValue = True),
            arcpy.Parameter(
                displayName = "Input GDB",
                name = "Input GDB",
                datatype = "DEWorkspace",
                parameterType = "required",
                direction = "Input"),
            arcpy.Parameter(
                displayName = "Output GDB FOLDER",
                name = "Output GDB FOLDER",
                datatype = "DEFolder",
                parameterType = "required",
                direction = "Input"),
            arcpy.Parameter(
                displayName = "Filter Name (separate more than one with a comma)",
                name = "Filter Name  (separate more than one with a comma)",
                datatype = "GPString",
                parameterType = "optional",
                direction = "Input"),
            arcpy.Parameter(
                displayName = "Type (Point, Polyline, Polygon)",
                name = "Type (Point, Polyline, Polygon)",
                datatype = "GPString",
                parameterType = "Required",
                direction = "Input")
        ]
        params[4].filter.type = "ValueList"
        params[4].filter.list = ["Point", "Polyline", "Polygon"]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True
    
    def get_gdb_list(self, folder_path):
        """Get a list of all geodatabases in the specified folder."""
        gdb_list = []
        for root, dirs, files in os.walk(folder_path):
            for dir_name in dirs:
                if dir_name.endswith(".gdb"):
                    gdb_list.append(os.path.join(root, dir_name))
        return gdb_list

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_feature_classes_str = parameters[0].valueAsText
        input_gdb_folder = parameters[1].valueAsText
        output_gdb_folder = parameters[2].valueAsText
        filter_names = parameters[3].valueAsText
        shp_type = parameters[4].valueAsText
        # Check if the input feature class is empty
        #feature_class_name = os.path.basename(input_feature_class)
        # Locate all geodatabases
        gdb_list = self.get_gdb_list(output_gdb_folder)
        # Check if the geodatabase list is empty
        if len(gdb_list) == 0:
            arcpy.AddMessage("No geodatabases found in the specified folder.")
            return
        # Process each geodatabase
            
        for gdb_path in gdb_list:
            arcpy.env.workspace = gdb_path
            # Check if the feature class already exists
            if filter_names is not None and len(filter_names) > 0:
                for filter_name in filter_names.split(","):
                    filter_name = filter_name.strip()
                    feature_classes = arcpy.ListFeatureClasses(f"*{filter_name}*", shp_type)
                    for feature_class in feature_classes:
                        arcpy.AddMessage(f"Deleted {feature_class} from {gdb_path}")
                        arcpy.management.Delete(feature_class)
            base_output_path = gdb_path
            for input_feature_class in input_feature_classes_str.split(";"):
                input_feature_class = input_feature_class.strip().replace("'", "")
                output_feature_class = os.path.join(base_output_path, os.path.basename(input_feature_class))
                arcpy.management.Copy(input_feature_class, output_feature_class)
                arcpy.AddMessage(f"Copied {input_feature_class} to {output_feature_class}")
            # Copy the feature class to the geodatabase
        arcpy.AddMessage("Copying completed successfully.")
        return


    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
