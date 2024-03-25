# pico_scope_setup.py
# Date: February 2024
# Author: Jane Cohen

## This code allows for data collection from one scope

import os, sys
os.environ['PATH'] += r'C:\Program Files\Pico Technology\SDK\lib'

import ctypes
import numpy as np
from picosdk.ps4000 import ps4000 as ps
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico_ok
import csv
import pico_scope_class as psc

## USER CONTROLS ##
curr_dir = "C:/Users/501ALabPC/Desktop/ENPH455-JC-main/"
scope_num = 1
save_data_to_desktop = True
save_data_to_gui = True
###################

pscope = psc.PScope()
pscope.load_settings_to_scope(f"{curr_dir}GUI/scope_settings/scope_{scope_num}_settings.csv")
print("Settings loaded")
pscope.open_pico()
print("Scope opened")
pscope.setup_trigger()
print("Trigger set")
pscope.return_timebase()
print("Timebase loaded")
v1, v2 = pscope.collect_data()
time = pscope.get_time_data() 
print("Time data collected")
pscope.close_scope()
print("Scope closed")

# save data to file
file_path = pscope.get_path(scope_num)
pscope.save_to_csv(curr_dir, file_path, scope_num, time, v1[:], v2[:], save_data_to_desktop, save_data_to_gui)







