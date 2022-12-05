import requests
import numpy as np
import os

j2000=2451545
deltaJ2000=0.3554779

#function to implement UT1 conversion
def UTCtoUT1(jdfull): #input in fractional julian days (UTC standard)

    if os.path.exists("finals2000A.daily"): #check for the presence of the conversion table
        Updated="The conversion table was already present inside the folder"
    else:
        tableURL="https://maia.usno.navy.mil/ser7/finals2000A.daily"
        req=requests.get(tableURL,allow_redirects=True) 
        Updated="The conversion table was downloaded from https://maia.usno.navy.mil/ser7/finals2000A.daily"
        tablefile=open("finals2000A.daily","w").write(req.text) #download and writes conversion table to a file

    file=open("finals2000A.daily","r")
    flag=0
    counter=0
    filedata=file.readlines()

    Mjd=np.floor((jdfull)-2400000.5) #modified julian date of the input

    while flag==0: #reads the table line by line
        line=filedata[counter]
        JD=float(line[7:15]) #modified julian day of the current line
        bull=float(line[58:68]) #UT1-UTC difference for current line (corresponds to julian day)
        if JD==Mjd: #if line corresponds to the input (UT1 conversion table has defined bulls for every day)
            flag=1
        counter=counter+1
    file.close()
        
    return bull #returns UT1-UTC difference

#function to implement GPS conversion
def UTCtoGPS(jdfull): #input in fractional julian days (UTC standard)

    if os.path.exists("tai-utc.dat"): #check for the presence of the conversion table
        Updated="The conversion table was already available insinde the folder"
    else:
        tableURL="https://maia.usno.navy.mil/ser7/tai-utc.dat"
        req=requests.get(tableURL,allow_redirects=True) 
        Updated="The conversion table was downloaded from https://maia.usno.navy.mil/ser7/tai-utc.dat"
        tablefile=open("tai-utc.dat","w").write(req.text) #download and writes conversion table to a file

    f=open("tai-utc.dat","r")
    file=f.readlines()
    file=str(file)
    file=file.split("\n") #reads complete conversion table and splits it into lines
    totallines=len(f.readlines())

    counter=0
    flag=0
    GPSjd_0=2437300.5 #first day available on the GPS conversion table

    while flag==0: #reads table line by line
        line=file[counter]
        GPSjday=float(line[19:28]) #reads julian day corresponding to current line
        bull=float(line[39:50]) #reads corresponding TAI-UTC difference
        if ((jdfull)>=GPSjd_0 and (jdfull)<GPSjday) or counter>=totallines: #check if input is between two days or after the last line
            flag=1
        else: GPSjd_0=GPSjday
        counter=counter+1
    f.close()

    return bull #returns the TAI-UTC difference