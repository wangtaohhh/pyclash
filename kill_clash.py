from operator import ge
import os


def kill_process_pid(processname="clash"):

    process_info_list = []
    process = os.popen("pidof %s" % processname)
    process_info = process.read().strip()
    for i in process_info.split(" "):
        if i != "":
            process_info_list.append(int(i))

    for pid_num in process_info_list:
        os.popen("kill -9 %d" % pid_num)

    return 0
