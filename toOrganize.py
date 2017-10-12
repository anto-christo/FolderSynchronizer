import os
import shutil

path = os.getcwd()

arr = os.listdir()

slash = "\\"

# File types and their corresponding extensions

Text = [ ".doc" , ".log" , ".msg" , ".odt" , ".rtf" , ".tex" , ".txt" , ".wpd" , ".wps" , ".docx" , ".pages" ]

Data = [ ".csv" , ".dat", ".ged" , ".key" , ".keychain" , ".pps" , ".ppt" , ".pptx" , ".sdf" , ".tar" , ".tax2016" , ".vcf" , ".xml" ]

Audio = [ ".aif" , ".iff" , ".m3u" , ".m4a" , ".mid" , ".mp3" , ".mpa" , ".wav" , ".wma" ]

Video = [ ".3g2" , ".3gp" , ".asf" , ".avi" , ".flv" , ".m4v" , ".mov" , ".mp4" , ".mpg" , ".rm" , ".srt" ,".swf" , ".vob" , ".wmv" ]

ThreeDImg = [ ".3dm" , ".3ds" , ".max" , ".obj" ]

RasterImage = [ ".bmp" , ".dds" , ".gif" , ".jpg" , ".png" , ".psd" , ".thm" , ".tif" , ".yuv" , ".pspimage" , ".tga" , ".tiff" ]

ThreeDImg = [ ".3dm" , ".3ds" , ".max" , ".obj" ]

VectorImage = [ ".ai" , ".eps" , ".ps" , ".svg" ]

PageLayout = [ ".indd" , ".pct" , ".pdf" ]

Spreadsheet = [ ".xlr" , ".xls" , ".xlsx" ]

Database =  [ ".accdb" , ".db" , ".dbf"  , ".mdb" , ".pdb" , ".sql" ]

Executable = [ ".apk" , ".app" , ".bat" , ".cgi" , ".com" , ".exe" , ".gadget" , ".jar" , ".wsf" ]

Game = [ ".dem" , ".gam" , ".nes" , ".rom" , ".sav" ]

CAD = [ ".dwg" , ".dxf" ]

GIS = [ ".gpx" , ".kml" , ".kmz" ]

Web = [ ".asp" , ".aspx" , ".cer" , ".cfm" , ".csr" , ".css" , ".htm" , ".html" , ".js" , ".jsp" , ".php" , ".rss" , ".xhtml" ]

Plugin = [  ".crx" , ".plugin" ]

Font = [ ".fnt" , ".fon" , ".otf" , ".ttf" ]

System = [ ".cab" , ".cpl" , ".cur" , ".deskthemepack" , ".dll" , ".dmp" , ".drv" , ".icns" , ".ico" , ".lnk" , ".sys" ]

Settings = [ ".cfg" , ".ini" , ".prf" ]

Encoded = [ ".hqx" , ".mim" , ".uue" ]

Compressed = [ ".7z" , ".cbr" , ".deb" , ".gz" , ".pkg" , ".rar" , ".rpm" , ".sitx" , ".tar.gz" , ".zip" , ".zipx" ]

DiskImage = [ ".bin" , ".cue" , ".dmg" , ".iso" , ".mdf" , ".toast" , ".vcd" ]

Developer = [ ".c" , ".class" , ".cpp" , ".cs" , ".dtd" , ".fla" , ".h" , ".java" , ".lua" , ".m" , ".pl" , ".py" , ".sh" , ".sln" , ".swift" , ".vb" , ".vcxproj" , ".xcodeproj" ]

Backup = [ ".bak" , ".tmp" ]

Misc = [ ".crdownload" , ".ics" , ".msi" , ".part" , ".torrent" ]

for x in arr:
    if os.path.isfile(x) and x!="toOrganize.py" and x!="toDisorganize.py":
        for i in x:
            if(i=="."):

                extension_name = x[x.rfind(i):len(x)]
                if(extension_name in Text):
                    folder_name ="Text"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Data):
                    folder_name ="Data"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Audio):
                    folder_name ="Audio"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Video):
                    folder_name ="Video"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in ThreeDImg):
                    folder_name ="3DImage"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in RasterImage):
                    folder_name ="RasterImage"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in VectorImage):
                    folder_name ="VectorImage"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in PageLayout):
                    folder_name ="PageLayout"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Spreadsheet):
                    folder_name ="Spreadsheet"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Database):
                    folder_name ="Database"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Executable):
                    folder_name ="Executable"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Game):
                    folder_name ="Game"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in CAD):
                    folder_name ="CAD"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in GIS):
                    folder_name ="GIS"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Web):
                    folder_name ="Web"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Plugin):
                    folder_name ="Plugin"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Font):
                    folder_name ="Font"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in System):
                    folder_name ="System"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Settings):
                    folder_name ="Settings"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Encoded):
                    folder_name ="Encoded"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Compressed):
                    folder_name ="Compressed"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in DiskImage):
                    folder_name ="DiskImage"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Developer):
                    folder_name ="Developer"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Backup):
                    folder_name ="Backup"
                    newpath = path + slash + folder_name
                    print(newpath)

                elif(extension_name in Misc):
                    folder_name ="Misc"
                    newpath = path + slash + folder_name
                    print(newpath)

                else:
                    folder_name ="Other"
                    newpath = path + slash + folder_name
                    print(newpath)


        if not os.path.exists(newpath):
            os.makedirs(newpath)

        shutil.move(path + slash + x,newpath + slash +x)
