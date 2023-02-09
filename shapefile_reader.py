# import geopandas as gpd

# shp_file = "AdamsCounty_Parcels202211.shp"

# #function to write csv file
# print("Reading shapefile...")
# shapefile = gpd.read_file(shp_file)
# print("Shapefile read successfully")
# #print(shapefile)
# #create csv file from scratch to write data

# #write boundary column list of the shapefile into a csv file
# print("Writing csv file...")
# with open("output-%s.csv"%shp_file.replace(".shp", ""), "w") as csv_file:    
#     for line in shapefile:        
#         #write line into csv file        
#         csv_file.write(str(line) + "\n")
#         print("csv file written successfully")


import shapefile  # pip install pyshp
import xlwt as xlwt

shp_file = "../AdamsCounty_Parcels202211.shp"


# read shapefile using pyshp
def read_shapefile(shp_file):
    sf = shapefile.Reader(shp_file)
    # fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    # df = pd.DataFrame(columns=fields, data=records)
    # df = df.assign(coords=shps)
    fields = [x[0] for x in sf.fields][1:] + ["boundaries"]
    return [fields] + list(zip(records, shps))


# function to write a xlsx file
def write_xlsx(data):
    print("Writing xlsx file...")
    # create xlsx file
    wb = xlwt.Workbook()
    # add a sheet
    ws = wb.add_sheet("Sheet 1")
    rows = len(data)
    for c, row in enumerate(data[0]):
        ws.write(0, c, row)
    for r, row in enumerate(data[1:]):
        current_row = r + 1
        for col, value in enumerate(row[0]):
            ws.write(current_row, col, value is None and "" or value)
        ws.write(current_row, col + 1, str(row[1]))
        print("Row %s of %s written" % (current_row, rows))
    # save xlsx file
    print("Saving xlsx file...")
    wb.save("output-%s.xls" % shp_file.replace(".shp", ""))
    print("xlsx file written successfully")
