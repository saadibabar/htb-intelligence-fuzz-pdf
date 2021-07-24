import requests
import os
import string


pdff= open('pdfsfound.txt','w')
pdff.close()

for m in range(01,12):
        for d in  range(01,31):
                m = str(m).zfill(2)
                d = str(d).zfill(2)
                print("checking file 2020-"+m+"-"+d+"-upload.pdf")
                r = requests.get("http://intelligence.htb/documents/2020-"+m+"-"+d+"-upload.pdf");
                if (r.status_code == 200):
                        print ("FOUND : http://intelligence.htb/documents/2020-"+m+"-"+d+"-upload.pdf")
                        
                        with open('pdfsfound.txt','a') as pdf:
                                pdf.write("http://intelligence.htb/documents/2020-"+m+"-"+d+"-upload.pdf\n")

pdf.close()


