
This is a python&&shell script to manager vsftpd user and analyse the vsftpd log.

## 1.Add a vsftpd user:
sudo python3 ftp_adduser.py  user passwd

## 2.Delete a vsftpd user:
sudo python3 ftp_deluser.py user

## 3.Run the delete script in the background to del the user when the user's period of validity has expired.
sudo pythone3 ftp_deluser.py

## 4.analyse the vsftpd log
python3 ftp_log_analyse.py year month

for example:
python3 ftp_log_analyse.py 2020 Dec


