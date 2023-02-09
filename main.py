import shapefile_reader as sfr

shp_file = "../AdamsCounty_Parcels202211.shp"

values = sfr.read_shapefile(shp_file)
sfr.write_xlsx(values)


