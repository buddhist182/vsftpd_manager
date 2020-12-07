import sys
import os
import string
import time

def check_to_del(uinfo):
    str = uinfo
    user = str.split()[0]
    start_time = str.split()[2]
    end_time = str.split()[3]
    now_time = time.strftime("%Y%m%d", time.localtime())
    '''
    year = time.strftime("%Y", time.localtime())
    month = time.strftime("%m", time.localtime())
    date = time.strftime("%d", time.localtime())

    y = end_time.split('-')[0]
    m = end_time.split('-')[1]
    d = end_time.split('-')[2]
    if (int(year) > int(y)):
        os.system('userdel' + ' ' + user)
    elif (int(year) == int(y) and int(month) > int(m)) :
        os.system('userdel' + ' ' + user)
    elif (int(year) == int(y) and int(month) == int(m) and int(date) > int(d)) :
        os.system('userdel' + ' ' + user)
    '''
    print('user = ' + user + ', now_time = ' + now_time + ", end_time = " + end_time)
    if (int(now_time) > int(end_time)) :
        return 0
    return 1

def deluserFromFile(file, user):
    ret = 0
    file_back = file + "_back"
    with open(file, "r") as f:
        userinfo = f.readlines()
    with open(file_back, "w") as fw:
        for line in userinfo:
            u = line.split()[0]
            if (u == user):
                print("Delete " + user + " in " + file)
                ret = 1
                continue
            fw.write(line)
    os.system("cp " + file_back + " " + file)
    return ret

def deluser(user):
    os.system('userdel ' + user)
    deluserFromFile("./ftpuser", user)
    deluserFromFile("/etc/allowed_users", user)
    os.system("service vsftpd restart")



if __name__ == '__main__':
    if (len(sys.argv) > 0):
        ftpuser = sys.argv[1]
        print("Static Delete " + ftpuser)
        deluser(ftpuser)
    else:
        while 1:
            with open("./ftpuser", "r") as f:
                userinfo = f.readlines()

            for line in userinfo:
                print(line)
                if (check_to_del(line) == 0) :
                    user = line.split()[0]
                    print("Delete " + user)
                    deluser(user)
            time.sleep(7200)


       
