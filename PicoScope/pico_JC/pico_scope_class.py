# pico_scope_class.py
# Date: February 2024
# Author: Jane Cohen

## This class is defined to be used with PicoScopes for data collection
## Import this class to a scope running script to use

import ctypes
import numpy as np
from picosdk.ps4000 import ps4000 as ps
from picosdk.functions import adc2mV, assert_pico_ok
import csv
import os
from datetime import datetime

class PScope:
   def __init__(self): 
      pass

   collect_mapper = {"False":0, "True":1}
   range_mapper = {"0.01":0, "0.02":1, "0.05":2, "0.1":3, "0.2":4, "0.5":5, "1":6, "2":7, 
                        "5":8, "10":9, "20":10, "50":11, "100":12}
   rate_mapper = {"4":0, "8":1, "16":2, "32":3, "64":4, "128":5, "256":6, "512":7, "1024":8}
   direction_mapper = {"ABOVE":0, "BELOW":1, "RISING":2, "FALLING":3, "RISING_OR_FALLING":4}
   coupling_mapper = {"AC":0, "DC":1}

   # load_settings_to_scope() method
   # load settings from external csv file and set as attributes
   def load_settings_to_scope(self, csv_path_name):  

      # eead the contents of the CSV file
      with open(csv_path_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

      # channel A settings
      self.set_collect(rows[1][1], 'A')
      self.set_voltage_range(rows[2][1], 'A')
      self.set_timebase(rows[3][1])

      # channel B settings 
      self.set_collect(rows[7][1], 'B')
      self.set_voltage_range(rows[8][1], 'B')

      # trigger settings 
      self.set_autotrigger(rows[12][1])
      self.set_coupling_type(rows[13][1])
      self.set_threshold(rows[14][1])
      self.set_direction(rows[15][1])
      self.set_delay(rows[16][1])
      self.set_pre_trigger_samples(rows[17][1])
      self.set_post_trigger_samples(rows[18][1])
      self.set_downsample(rows[19][1])

   # setter methods
   def set_source(self, src, name):
      if (src == 'A'):
         self.source_A = 0
      elif (src == 'B'):
         self.source_B = 1
      else:
         print("Invalid channel name for ", name)

   def set_collect(self, coll, channel):
      if (channel == 'A'):
         self.enabled_A = self.collect_mapper.get(coll)
      else:
         self.enabled_B = self.collect_mapper.get(coll)

   def set_voltage_range(self, vol, channel):
      if (channel == 'A'):
         self.range_A = self.range_mapper.get(vol)
      else:
         self.range_B = self.range_mapper.get(vol)

   def set_timebase(self, timebase):
      self.timebase = timebase

   def set_threshold(self, thresh):
      self.threshold = thresh

   def set_coupling_type(self, couple):
      self.coupling = self.coupling_mapper.get(couple)

   def set_direction(self, dir):
      self.direction = self.direction_mapper.get(dir)

   def set_delay(self, delay):
      self.delay = delay

   def set_autotrigger(self, trig):
      self.trigger = trig
   
   def set_pre_trigger_samples(self, pre):
      self.presample = pre
      
   def set_post_trigger_samples(self, post):
      self.postsample = post

   def set_downsample(self, downsample):
      self.downsample = downsample
   
   def set_chandle(self, chandle):
      self.chandle = chandle
   
   def set_status(self, status):
      self.status = status

   def set_max_samples(self, preTriggerSamples, postTriggerSamples):
      self.maxSamples = preTriggerSamples + postTriggerSamples
   
   def set_time_intervals(self, type):
      self.timeIntervals = type

   def set_returned_max_samples(self, type):
      self.returnedMaxSamples = type
   
   def set_oversample(self, oversample):
      self.oversample = oversample
   
   # getter methods
   def get_source(self, src):
      if (src == 'A'):
         return 0
      else:
         return 1

   def get_collect(self, channel):
      if (channel == 'A'):
         return self.enabled_A
      else:
         return self.enabled_B

   def get_voltage_range(self, channel):
      if (channel == 'A'):
         return self.range_A
      else:
         return self.range_B
      
   def get_timebase(self):
      return int(self.timebase)

   def get_threshold(self):
      return int(self.threshold)

   def get_coupling_type(self):
      return int(self.coupling)

   def get_direction(self):
      return self.direction

   def get_delay(self):
      return int(self.delay)

   def get_trigger(self):
      return int(self.trigger)
   
   def get_pre_trigger_samples(self):
      return int(self.presample)
      
   def get_post_trigger_samples(self):
      return int(self.postsample)
   
   def get_downsample(self):
      return int(self.downsample)
   
   def get_time_intervals(self):
      return self.timeIntervals 
   
   def get_max_samples(self):
      return int(self.maxSamples)

   def get_oversample(self):
      return self.oversample

   def get_returned_max_samples(self):
      return self.returnedMaxSamples

   # open_scope() method
   # opens scope and sets up both channels
   def open_pico(self):
      # create chandle and status
      chandle = ctypes.c_int16()
      status = {}

      # open scope
      status["openunit"] = ps.ps4000OpenUnit(ctypes.byref(chandle))
      assert_pico_ok(status["openunit"])

      # set up channel A
      coupling = self.get_coupling_type() #for both channels
      source = self.get_source('A')
      enabled = self.get_collect('A')
      range1 = self.get_voltage_range('A')

      status["setChA"] = ps.ps4000SetChannel(chandle, source, enabled, coupling, range1)
      assert_pico_ok(status["setChA"])

      # set up channel B
      source = self.get_source('B')
      enabled = self.get_collect('B')
      range = self.get_voltage_range('B')

      status["setChB"] = ps.ps4000SetChannel(chandle, source, enabled, coupling, range)
      assert_pico_ok(status["setChB"])

      self.set_chandle(chandle)
      self.set_status(status)
   
   # setup_trigger() method
   # set up single trigger for scope
   def setup_trigger(self):
      enabled = 1
      source = PS4000_CHANNEL_A = 0
      threshold = self.get_threshold()
      direction = self.get_direction()
      delay = self.get_delay()
      trigger = self.get_trigger()
      self.status["trigger"] = ps.ps4000SetSimpleTrigger(self.chandle, enabled, source, threshold, 
                                                         direction, delay, trigger)
      assert_pico_ok(self.status["trigger"])

      preTriggerSamples = self.get_pre_trigger_samples()
      postTriggerSamples = self.get_post_trigger_samples()
      self.set_max_samples(preTriggerSamples, postTriggerSamples)

   # return_timebase() method
   # get timebase information
   def return_timebase(self):
      # segment index = 0
      timeIntervalns = ctypes.c_float()
      returnedMaxSamples = ctypes.c_int32()
      oversample = ctypes.c_int16(1)
      maxSamples = self.get_max_samples()
      self.set_timebase(25002)
      timebase = self.get_timebase()
      self.status["getTimebase2"] = ps.ps4000GetTimebase2(self.chandle, timebase, maxSamples, 
                                                          ctypes.byref(timeIntervalns), oversample, 
                                                          ctypes.byref(returnedMaxSamples), 0)
      self.set_time_intervals(timeIntervalns)
      self.set_returned_max_samples(returnedMaxSamples)
      self.set_oversample(oversample)
      assert_pico_ok(self.status["getTimebase2"])

   # collect_data() method
   # run block capture
   def collect_data(self):
      segment_index = 0
      lpReady = time_indisposed = pParameter = None 
      timebase = self.get_timebase()
      oversample = ctypes.c_int16(1)
      preTriggerSamples = self.get_pre_trigger_samples()
      postTriggerSamples = self.get_post_trigger_samples()
      self.status["runBlock"] = ps.ps4000RunBlock(self.chandle, preTriggerSamples, postTriggerSamples, timebase, oversample, 
                                                  time_indisposed, segment_index, lpReady, pParameter)
      assert_pico_ok(self.status["runBlock"])

      print("Block mode initiated")

      # check for data collection to finish using ps4000IsReady
      ready = ctypes.c_int16(0)
      check = ctypes.c_int16(0)
      while ready.value == check.value:
         self.status["isReady"] = ps.ps4000IsReady(self.chandle, ctypes.byref(ready))

      print("Data collection finished")

      # create buffers ready for assigning pointers for data collection
      maxSamples = self.get_max_samples()
      bufferAMax = (ctypes.c_int16 * maxSamples)()
      bufferAMin = (ctypes.c_int16 * maxSamples)() 
      bufferBMax = (ctypes.c_int16 * maxSamples)()
      bufferBMin = (ctypes.c_int16 * maxSamples)() 


      # set data buffer location for data collection from channel A
      # buffer length = maxSamples
      source = self.get_source('A')
      self.status["setDataBuffersA"] = ps.ps4000SetDataBuffers(self.chandle, source, ctypes.byref(bufferAMax), 
                                                          ctypes.byref(bufferAMin), maxSamples)
      assert_pico_ok(self.status["setDataBuffersA"])

      # set data buffer location for data collection from channel B
      # buffer length = maxSamples
      source = self.get_source('B')
      self.status["setDataBuffersB"] = ps.ps4000SetDataBuffers(self.chandle, source, ctypes.byref(bufferBMax), 
                                                               ctypes.byref(bufferBMin), maxSamples)
      assert_pico_ok(self.status["setDataBuffersB"])

      print("Buffers created")

      # create overflow location
      overflow = ctypes.c_int16()
      # create converted type maxSamples
      cmaxSamples = ctypes.c_int32(maxSamples)

      # retried data from scope to buffers assigned above
      start_index = 0
      downsample_ratio = 0
      downsample_ratio_mode = 0
      segment_index = 0
      self.status["getValues"] = ps.ps4000GetValues(self.chandle, start_index, ctypes.byref(cmaxSamples), downsample_ratio, 
                                                    downsample_ratio_mode, segment_index, ctypes.byref(overflow))
      assert_pico_ok(self.status["getValues"])

      print("Data retrieved from scope to buffers")

      # find maximum ADC count value
      # handle = chandle
      maxADC = ctypes.c_int16(32767)

      # convert ADC counts data to mV
      adc2mVChAMax =  adc2mV(bufferAMax, self.get_voltage_range('A'), maxADC)
      adc2mVChBMax =  adc2mV(bufferBMax, self.get_voltage_range('B'), maxADC)

      print("ADC counts converted to mV")
      print(len(adc2mVChAMax), "data points collected")

      return (adc2mVChAMax, adc2mVChBMax)
   
   # close_scope() method
   # stop the scope
   def close_scope(self):
      self.status["stop"] = ps.ps4000Stop(self.chandle)
      assert_pico_ok(self.status["stop"])

      # close unit and disconnect the scope
      self.status["close"] = ps.ps4000CloseUnit(self.chandle)
      assert_pico_ok(self.status["close"])

   # get_time_data() method
   # create time data
   def get_time_data(self):
      maxSamples = self.get_max_samples()
      timeIntervalns = self.get_time_intervals()
      cmaxSamples = ctypes.c_int32(maxSamples)

      # create converted type maxSamples
      cmaxSamples = ctypes.c_int32(maxSamples)
      time = np.linspace(0, (cmaxSamples.value - 1) * timeIntervalns.value, cmaxSamples.value)
      return time
   
   def get_path(self, scope_num):
      # specify the parent folder path
      parent_folder_path = r'C:\Users\501ALabPC\Desktop\ENPH455-JC-main'

      # check if the parent folder exists
      if not os.path.exists(parent_folder_path):
         os.makedirs(parent_folder_path)

      # get the current date
      current_datetime = datetime.now()
      year = current_datetime.year
      month = current_datetime.month
      day = current_datetime.day

      # create subfolder names based on year, month, and day
      year_folder = os.path.join(parent_folder_path, str(year))
      month_folder = os.path.join(year_folder, f"{month:02d}")  # Zero-padded month
      day_folder = os.path.join(month_folder, f"{day:02d}")  # Zero-padded day

      # create the subfolders if they don't exist
      for folder in [year_folder, month_folder, day_folder]:
         if not os.path.exists(folder):
               os.makedirs(folder)

      # use 'day_folder' as the base path for files
      file_name = f"data_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}_Scope{scope_num}.csv"
      file_path = os.path.join(day_folder, file_name)

      return file_path
   
   def save_to_csv(self, curr_dir, file_path, scope_num, time, channelA, channelB, flag_desktop, flag_gui):
      if(flag_desktop == True):
        # Combine the columns into rows
        rows = zip(time, channelA, channelB)
    
        # Write data to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(['Time (ns)', 'Voltage A (mV)', 'Voltage B (mV)'])

            # Write data rows
            for i, row in enumerate(rows):
                # Check if the index is a multiple of 100 (starting from 0)
                if i % 100 == 0:
                    # Write the row to the CSV
                    csv_writer.writerow(row)

            print(f"\n Data saved to: {file_path}")

      if(flag_gui == True):
         path = f"{curr_dir}GUI/collected_data/Scope {scope_num}/Channel A/data.csv"
         # Combine the columns into rows
         rows = zip(time, channelA)

         # Write data to the CSV file
         with open(path, 'w', newline='') as csv_file:
               csv_writer = csv.writer(csv_file)

               # Write header
               csv_writer.writerow(['Time (ns)', 'Voltage (mV)'])

               # Write data rows
               for i, row in enumerate(rows):
                  # Check if the index is a multiple of 100 (starting from 0)
                  if i % 100 == 0:
                     # Write the row to the CSV
                     csv_writer.writerow(row)

               print(f"\n Data saved to: {path}")

         path = f"{curr_dir}GUI/collected_data/Scope {scope_num}/Channel B/data.csv"
         # Combine the columns into rows
         rows = zip(time, channelB)

         # Write data to the CSV file
         with open(path, 'w', newline='') as csv_file:
               csv_writer = csv.writer(csv_file)

               # Write header
               csv_writer.writerow(['Time (ns)', 'Voltage (mV)'])

               # Write data rows
               for i, row in enumerate(rows):
                  # Check if the index is a multiple of 100 (starting from 0)
                  if i % 100 == 0:
                     # Write the row to the CSV
                     csv_writer.writerow(row)
                     
               print(f"\n Data saved to: {path}")