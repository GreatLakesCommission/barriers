import arcpy
def main():
    #arcpy.env.workspace="stream\\StreamTreatments.gdb"
    arcpy.env.workspace="stream"
    try:
        #ftrs=arcpy.SearchCursor("StreamTreatments11_21")
        ftrs=arcpy.SearchCursor("All_2015_TFM_Streams_WORK.shp")
        if ftrs is not None:
            #with open(r"treatments.json","w") as txt:
            with open(r"treatments2015.json","w") as txt:
                count=0
                #txt.write("lat\tlon\ttitle\tdescription\ticonSize\ticonOffset\ticon\n")
                txt.write("[")
                for ftr in ftrs:
                    #txt.write('%f\t%f\t%s\t%s\t-10,-25\ticons\\flag.png\n'%(ftr.Latitude,ftr.Longitude,ftr.StreamName,ftr.Years))
                    #txt.write('{"lat":%f,"lon":%f,"sname":"%s","years":"%s"},'%(ftr.Latitude,ftr.Longitude,ftr.StreamName,ftr.Years))
                    txt.write('{"lat":%f,"lon":%f,"sname":"%s","link":"%s"},'%(ftr.LAT_DEG,ftr.LONG_DEG,ftr.STREAM_NAM,ftr.Link))
                    count=count+1
                txt.seek(txt.tell()-1)
                txt.write("]")
    except Exception as e:
        print(str(e))
    else:
        print("done.%d records were written to the file\n"%count)

if __name__ == '__main__':
    main()
