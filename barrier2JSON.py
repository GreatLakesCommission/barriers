import arcpy
def main():
    arcpy.env.workspace="ArcGIS\\stream\\Update05_13"
    try:
        ftrs=arcpy.SearchCursor("BarrierPrj05_13.shp")
        if ftrs is not None:
            with open(r"barriers.json","w") as json:
                count=0
                fc=None
                json.write("[")
                for ftr in ftrs:
                    if ftr.FIRST_BA_1 == 1:
                        fc="Yes"
                    else:
                        fc="No"
                    json.write('{"id":%d,"lat":%f,"lon":%f,"name":"%s","waterbody":"%s","inspdate":"%s","distance":%f,"ub":"%s","fc":"%s"},'%(ftr.BarrierID,ftr.Latitude,ftr.Longitude,ftr.Barrier_Nm.replace("\"","'"),ftr.WaterbodyN,ftr.Last_Inspe,ftr.Shape_Leng,ftr.UpstreamID,fc))
                    count=count+1
                json.seek(json.tell()-1)
                json.write("]")
    except Exception as e:
        print(str(e))
    else:
        print("done.%d records were written to the file\n"%count)
if __name__ == '__main__':
    main()
