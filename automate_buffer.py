import arcpy
arcpy.env.workspace = r"D:\Bharati\Sem_3\Programming_3\P3_automating_scripts_with_list\Practical_3_ProProject\Practical_3_ProProject\03_Automating_Scripts_With_Lists.gdb"
fc_list = arcpy.ListFeatureClasses()
print(fc_list)

for fc in fc_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType
    if shape_type == "Point":
        buffer_distance = "500 feet"
    elif shape_type == "Polyline":
        buffer_distance = "1000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "600 feet"
    arcpy.analysis.Buffer(fc,fc +"_Buffer", buffer_distance)
print("--------------------------------")
