from harvesters.core import Harvester
import genicam
import cv2
import matplotlib.pyplot as plt 
import numpy as np 
import time
from datetime import date
from datetime import datetime
from zoneinfo import ZoneInfo
import os
def Run(camera_settings):
    """
    Basic function for capturing samples with the LHMP.

    :param camera_settings: dictionary containing the gain and exposure time camera settings as well as the acquisition duration 
    :type camera_settings: numpy dictionary        
    :return: dictionary of raw image data in digital number along with the image metadata of exposure time (us), gain, acquisition time (UTC), sensor temperature (degC)
    :rtype: numpy dictionary
    """  
    h = Harvester() # 1. Initialize Harvester
    h.add_file(camera_settings['CTI_path'])# Add the path to your GenTL Producer's CTI file (e.g., '/opt/sentech/lib/libstgentl.cti')
    h.update()
    image_data_list = [] # Store acquired images
    image_info_list = [] # Store acquired image meta info (Gain, Exposure Time, Acquisition Time, etc.,)
    if len(h.device_info_list)>0:
        start_time = time.time()

        print(f"Starting image acquisition for {camera_settings['acquisition_duration']} seconds...")
        ia = h.create(0) # Create an ImageAcquirer object (representing your camera)
        ia.start() # Start continuous acquisition
        #print(dir(ia.remote_device.node_map))
        ia_nm = ia.remote_device.node_map
        ia_nm.GainAuto.value = camera_settings['GainAuto']  #'Continuous'
        if ia_nm.GainAuto.value == 'Off':
            ia_nm.Gain.value = camera_settings['GainSetting']
        ia_nm.ExposureAuto.value = camera_settings['ExposureAuto'] 
        if ia_nm.ExposureAuto.value == 'Off':
            ia_nm.ExposureTime.value = camera_settings['ExposureTimeSetting']        
        while time.time() - start_time < camera_settings['acquisition_duration']: # Continuously fetch and process images
            try:
                buffer = ia.fetch(timeout=3)  # Fetch a buffer (which contains the image with a timeout in seconds
                payload = buffer.payload # Extract image data
                component = payload.components[0]  # Assuming a single image component
                width = component.width
                height = component.height
                data_format = component.data_format
                content = component.data.reshape(height, width)  # Reshape to a 2D array
                image_data_list.append(content.copy()) # Store the image data
                utc_now = datetime.now(ZoneInfo("UTC"))
                gainvalue = ia_nm.Gain.value
                exposuretimevalue = ia_nm.ExposureTime.value 
                DeviceT = ia_nm.DeviceTemperature.value #
                image_info_list.append([exposuretimevalue, gainvalue, utc_now.strftime('%Y%m%dT%H%M%S-%f'), DeviceT])
                # Optional: Process or save the image (e.g., using OpenCV)
                # imagename = f"Image_{exposuretimevalue}-{gainvalue}_{utc_now.strftime('%Y%m%dT%H%M%S-%f')}"
                #cv2.imwrite(f'{imagename}.png', content)
                buffer.queue()  # Queue the buffer for the next image acquisition, which is crucial for continuous acquisition 
            except genicam.gentl.TimeoutException:
                print("No buffer delivered within the timeout period. Continuing...")
                continue
            except Exception as e:
                print(f"Error during acquisition: {e}")
                break # Exit loop on unexpected errors
        ia.stop()# Stop acquisition and clean up
        ia.destroy()
        h.reset()
    output_dictionary = {}
    output_dictionary['image_data_list'] = image_data_list
    output_dictionary['image_info_list'] = image_info_list
    return output_dictionary
