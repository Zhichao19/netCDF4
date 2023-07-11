#!/usr/bin/env python

# Import required python modules
import ftplib
import os

# %% 


# Define the local directory name to put data in
ddir="C:\\datadir"

# If directory doesn't exist make it
if not os.path.isdir(ddir):
    os.mkdir(ddir)

# Change the local directory to where you want to put the data
os.chdir(ddir)

# login to FTP
f=ftplib.FTP("ftp.ceda.ac.uk", "", "")
# f=ftplib.FTP("ftp.ceda.ac.uk", "zw2023", "of*&mZ4^o&6")
# f=ftplib.FTP("anon-ftp.ceda.ac.uk", "", "")
f.login("zw2023", "iGDdEi0Q0?bP")

# %% 
# loop through years
for year in range(1960,1961):

    # loop through months
    for month in range(1,13):

        # get number of days in the month
        if year%4==0 and month==2:
            ndays=29
        else:
            ndays=int("dummy 31 28 31 30 31 30 31 31 30 31 30 31".split()[month])

        # loop through days
        # for day in range(1, ndays+1):

            # loop through hours
            # for hour in range(0, 19, 6):

                # loop through variables
                # for var in ("10u", "10v"):

        # change the remote directory
        # f.cwd("/badc/ecmwf-e40/data/gg/as/%.4d/%.2d/%.2d" % (year, month, day))
        f.cwd("/badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.1.0.0/1km/tasmax/day/v20220310")
        
        # define filename
        # file="ggas%.4d%.2d%.2d%.2d%s.grb" % (year, month, day, hour, var)
        file="tasmax_hadukgrid_uk_1km_day_1960%.2d01-1960%.2d%.2d.nc" % (month, month, ndays)
        # get the remote file to the local directory
        f.retrbinary("RETR %s" % file, open(file, "wb").write)

# Close FTP connection
f.close()



























