# Conversion-to-UT1-and-GPS
The code in the repository allows to convert from UTC time standard to UT1 and GPS time standards, implemented through two different functions.

# UTCtoUT1
The UTC to UT1 conversion function reads as input the fractional julian day and returns the corresponding UT1-UTC difference (bull) in seconds. The difference is read from the "finals200A.daily" file, on the line corresponding to the modified julian day which corresponds to the input.
The function checks for the presence of the conversion table inside the current folder: if not present, the conversion table is donwloaded and written to a file. The file read procedurally, returning the UT1-UTC difference (in seconds) corresponding to the input.

#input: float jdfull
#output: float bull

~~~
UTCseconds=30
UTCjdfull=2400000.5
bull=UT1toUTC(UTCjdfull)
UT1seconds=UTCseconds+bull
~~~

# UTCtoGPS
The UTC to GPS conversion function reads as input the fractional julian day and returns the corresponding TAI-UTC difference (bull) in seconds. The difference is read from the "tai-utc.dat" file, on the line corresponding to the last leap second difference introduced before the input.
The function checks for the presence of the conversion table inside the current folder: if not present, the conversion table is donwloaded and written to a file. The file is split into lines and read procedurally, returning the TAI-UTC difference (in seconds) corresponding to the input. Then, the difference between TAI and GPS time is taken into account.

#input: float jdfull
#output: bull

~~~
UTCseconds=30
UTCjdfull=2400000.5
bull=GPStoUTC(UTCjdfull)
GPSseconds=UTCseconds+bull
~~~

