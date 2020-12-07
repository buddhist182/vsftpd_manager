import os
import sys
import time
import string

#Add ftp user and set passwd
if (len(sys.argv) < 2):
    print ('Too less parameter')
    sys.exit()

ftpuser = sys.argv[1]
passwd = sys.argv[2]
cmd = './ftp_adduser_script ' + ftpuser + ' ' + passwd
print(cmd)
os.system(cmd);

#Add user expire infomation
start_time = time.strftime("%Y%02m%02d", time.localtime())
year = time.strftime("%Y", time.localtime())
month = time.strftime("%02m", time.localtime())
date = time.strftime("%02d", time.localtime())
print(year+month+date)
y = int(year)
m = int(month)
d = int(date)
if (m > 9) :
    y = y + 1
    m = m + 3 - 12
    d = d - 1
else:
    m = m + 3
end_time = str(y) + '%02d'%m + '%02d'%d
print("endtime:"+ end_time)
ftpuserinfo = ftpuser + ' ' + passwd + ' '  + start_time + ' ' + end_time + '\n'
f = open("./ftpuser", "a")
f.write(ftpuserinfo)
f.close


