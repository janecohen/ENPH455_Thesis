# two_scope_setup.py
# Date: February 2024
# Author: Jane Cohen

## This code allows for data collection from two scope

import os, sys
os.environ['PATH'] += r'C:\Program Files\Pico Technology\SDK\lib'

from picosdk.ps4000 import ps4000 as ps
from picosdk.functions import adc2mV, assert_pico_ok
import pico_scope_class as psc

## USER CONTROLS ##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
curr_dir = "C:/Users/501ALabPC/Desktop/ENPH455-JC-main/"
save_data_to_desktop = True
save_data_to_gui = True
###################

scope_num_1 = 1
scope_num_2 = 2

pscope1 = psc.PScope()
pscope1.load_settings_to_scope(f"{curr_dir}GUI/scope_settings/scope_{scope_num_1}_settings.csv")
pscope2 = psc.PScope()
pscope2.load_settings_to_scope(f"{curr_dir}GUI/scope_settings/scope_{scope_num_2}_settings.csv")
print("Settings loaded")

pscope1.open_pico()
pscope2.open_pico()
print("Scope opened")

pscope1.setup_trigger()
pscope2.setup_trigger()
print("Trigger set")

pscope1.return_timebase()
pscope2.return_timebase()
print("Timebase loaded")

v1_scope1, v2_scope1 = pscope1.collect_data()
time_scope1 = pscope1.get_time_data() 
v1_scope2, v2_scope2 = pscope2.collect_data()
time_scope2 = pscope2.get_time_data()  
print("Time data collected")

pscope1.close_scope()
pscope2.close_scope()
print("Scope closed")

# save data to file
file_path1 = pscope1.get_path(scope_num_1)
file_path2 = pscope2.get_path(scope_num_2)
pscope1.save_to_csv(curr_dir, file_path1, scope_num_1, time_scope1, v1_scope1[:], v2_scope1[:], save_data_to_desktop, save_data_to_gui)
pscope2.save_to_csv(curr_dir, file_path2, scope_num_2, time_scope2, v1_scope2[:], v2_scope2[:], save_data_to_desktop, save_data_to_gui)








