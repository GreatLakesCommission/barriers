import arcpy
def main():
    arcpy.env.workspace="Trapping.gdb"
    try:
        ftrs=arcpy.SearchCursor("TrapLocations_FIX")
        if ftrs is not None:
            with open(r"trapping.json","w") as txt:
                count=0
                #txt.write("lat\tlon\ttitle\tdescription\ticonSize\ticonOffset\ticon\n")
                txt.write("[")
                for ftr in ftrs:
                    #txt.write('%f\t%f\t%s\t%s\t-10,-25\ticons\\flag.png\n'%(ftr.Latitude,ftr.Longitude,ftr.StreamName,ftr.Years))
                    txt.write('{"lat":%f,"lon":%f,"id":"%s","country":"%s","agency":"%s","lake":"%s","stream":"%s","years":[%s],"catch":[%s],"img":"%s"},'%(ftr.Latitude,ftr.Longitude,ftr.Identifier,ftr.Country,ftr.Agency,ftr.LakeName,ftr.StreamName,ftr.Years,ftr.Catches,,ftr.Link))
                    count=count+1
                txt.seek(txt.tell()-1)
                txt.write("]")
    except Exception as e:
        print(str(e))
    else:
        print("done.%d records were written to the file\n"%count)

if __name__ == '__main__':
    main()
