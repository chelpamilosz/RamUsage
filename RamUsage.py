#!/usr/bin/python3

import time
import os
import pandas as pd


def ramusage():
    pipe = os.popen("free -m")
    df = pd.read_csv(pipe, delim_whitespace=True)

    total_mem = df.at['Mem:', 'total']
    used_mem = df.at['Mem:', 'used']

    usage = (used_mem / total_mem) * 100

    print("RAM USAGE: " + str(round(usage)) + "%", end='\r')


os.system("clear")

try:
    while True:
        ramusage()
        time.sleep(0.5)  # iteration every 0.5 second
except KeyboardInterrupt:
    pass
