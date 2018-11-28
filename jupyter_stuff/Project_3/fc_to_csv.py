import arcpy, csv

def tableToCSV(input_tbl, csv_filepath):
    '''go from feature class to csv'''
    fld_list = arcpy.ListFields(input_tbl)
    fld_names = [fld.name for fld in fld_list]
    with open(csv_filepath, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fld_names)
        with arcpy.da.SearchCursor(input_tbl, fld_names) as cursor:
            for row in cursor:
                writer.writerow(row)
        print (csv_filepath + " CREATED")
    csv_file.close()



