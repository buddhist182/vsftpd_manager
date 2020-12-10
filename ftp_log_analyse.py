import sys
import os
import string

def getXferlog(year, month):
    with open("/var/log/xferlog", "r") as f:
        log = f.readlines()
    user_dict = {};
    for line in log:
        m = line.split()[1];
        y = line.split()[4];
        if (m == month) and (y == year):
            log_dict = {};
            d = line.split()[2];
            t = line.split()[3];
            cost = line.split()[5];
            ip = line.split()[6];
            size = line.split()[7];
            file = line.split()[8];
            tmode = line.split()[9];
            in_out = line.split()[11];
            user = line.split()[13];

            time = y + " " + m + " " + d + " " + t
            log_dict["time"] = time;
            log_dict["user"] = user;
            log_dict["ip"] = ip;
            log_dict["file"] = file;
            log_dict["size"] = size;
            log_dict["in_out"] = in_out;

            if user_dict.get(user):
                log_list = user_dict[user];
                log_list.append(log_dict);
            else:
                loglist = [log_dict];
                user_dict[user] = loglist;
    return user_dict;

if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print("Too less args, please enter year and month")
        print("for example：python xxx.py 2020 Dec")
        sys.exit()
    year = sys.argv[1]
    month = sys.argv[2]
    print("year = " + year + " month = " + month)
    user_dict = getXferlog(year, month)
    report_file = "./report_" + year + month + ".csv";
    with open(report_file, "w") as f:
        f.write("action, user, IP addr, file name, size, in_out\n");
        f.write("upload,\n");
        for key in user_dict:
            print(key)
            f.write("," + key + ",\n")
            total = 0;
            for log_dict in user_dict[key]:
                if log_dict["in_out"] == "i":
                    write_cont = ", ,"
                    for log_key in log_dict:
                         write_cont = write_cont + log_dict[log_key] + ",";
                    total = total + int(log_dict['size']);
                    f.write(write_cont + "\n")
            f.write(', , , , , total,' + str(total) + '\n')
        f.write("download,\n");
        for key in user_dict:
            print(key)
            f.write("," + key + ",\n")
            total = 0;
            for log_dict in user_dict[key]:
                if log_dict["in_out"] == "o":
                    write_cont = ", , "
                    for log_key in log_dict:
                         write_cont = write_cont + log_dict[log_key] + ",";
                    total = total + int(log_dict['size']);
                    f.write(write_cont + "\n")
            f.write(', , , , , total,' + str(total) + '\n')


