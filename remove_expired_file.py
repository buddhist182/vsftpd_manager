
import os
import sys
import time
import logging
import datetime
import shutil

def find_and_rm_file(file_dir, expire_time = 60):
    logging.info('file_dir [%s], expire_time [%s]' %(file_dir, expire_time))
    if not os.path.exists(file_dir):
        logging.info('file_dir [%s] does not exist'%file_dir)
        return None

    today = datetime.datetime.now()
    n_days = datetime.timedelta(days = int(expire_time))
    n_days_agos = today - n_days
    n_days_agos_timestamps = time.mktime(n_days_agos.timetuple())

    all_file = os.listdir(file_dir)
    for data_file in all_file:
        abs_file = os.path.join(file_dir, data_file)
        file_timestamp = os.path.getmtime(abs_file)
        if float(file_timestamp) <= float(n_days_agos_timestamps):
            logging.info('[%s] is expired' %abs_file)
            if os.path.isfile(abs_file):
                os.remove(abs_file)
                logging.info("Delete [%s]" %abs_file)
            if os.path.isdir(abs_file):
                shutil.rmtree(abs_file)
                logging.info("Delete [%s]" %abs_file)
        else:
            if os.path.isdir(abs_file):
                find_and_rm_file(abs_file, expire_time)

if __name__ == '__main__':
    find_and_rm_file('test', 20)




