import arcpy
import os


def main(fcp, outnm='barriers.json'):
    dname = os.path.dirname(fcp)
    fc = os.path.basename(fcp)
    arcpy.env.workspace = dname
    try:
        ftrs=arcpy.SearchCursor(fc)
        if ftrs is not None:
            plen = len(dname)
            if dname[plen - 3:] == 'gdb':
                output = os.path.join(os.path.dirname(dname), outnm)
            else:
                output = os.path.join(dname, outnm)
            with open(output,"w") as json:
                count=0
                fc=None
                json.write("[")
                for ftr in ftrs:
                    if ftr.FIRST_BA_1 == 1:
                        fc="Yes"
                    else:
                        fc="No"
                    json.write('{"id":%d,"lat":%f,"lon":%f,"name":"%s","waterbody":"%s","inspdate":"%s","distance":%f,"ub":"%s","fc":"%s","aid":"%s"},'%(ftr.BarrierID,ftr.Latitude,ftr.Longitude,ftr.Barrier_Nm.replace("\"","'"),ftr.WaterbodyN,ftr.Last_Inspe,ftr.Shape_Leng,ftr.UpstreamID,fc,ftr.AgencyID))
                    count=count+1
                json.seek(json.tell()-1)
                json.write("]")
    except Exception as e:
        print(str(e))
    else:
        print("done.%d records were written to the file\n"%count)
if __name__ == '__main__':
    fclass = 'ArcGIS\\stream\\Update05_13\\BarrierPrj05_13.shp'
    main(fclass)
