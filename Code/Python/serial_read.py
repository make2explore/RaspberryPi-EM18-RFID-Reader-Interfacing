# ---------------------------------- make2explore.com----------------------------------------------------#
# Tutorial          - Raspberry Pi UART - Read Serial data available on Port
# Created By        - info@make2explore.com
# Version - 1.0
# Last Modified     - 07/02/2022 15:00:00 @admin
# Software          - Python, Thonny IDE, Standard Python Libraries
# Hardware          - Raspberry Pi 4 model B, FTDI Serial Adaptor Module, EM-18 RFID Reader, Level Converter
# Sensors Used      - EM-18 RFID Reader
# Source Repo       - github.com/make2explore
# -------------------------------------------------------------------------------------------------------#

import serial
from time import sleep

ser = serial.Serial ("/dev/ttyAMA0", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially 
