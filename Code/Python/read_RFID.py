# ---------------------------------- make2explore.com----------------------------------------------------#
# Tutorial          - Raspberry Pi and EM-18 RFID Reader Interfacing - Read RFID Codes
# Created By        - info@make2explore.com
# Version - 1.0
# Last Modified     - 07/02/2022 15:00:00 @admin
# Software          - Python, Thonny IDE, Standard Python Libraries
# Hardware          - Raspberry Pi 4 model B, FTDI Serial Adaptor Module, EM-18 RFID Reader, Level Converter
# Sensors Used      - EM-18 RFID Reader
# Source Repo       - github.com/make2explore
# -------------------------------------------------------------------------------------------------------#

import time
import serial
          
      
data = serial.Serial(
                    port='/dev/ttyAMA0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print (" ")
          
try:     
   while 1:
         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         
         print ("Place the card")
         x=data.read(12) #print upto 10 data at once and the 
                         #remaining on the second line
         output = str(x, 'UTF-8')
         print ("RFID Card No : ",output)
         print (" ")

except KeyboardInterrupt:
       data.close()
