import time

import network

import machine as m

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)

sta_if.scan() # Scan for available access points

sta_if.connect("GatoConSombrero", "superclave1987") # Connect to an AP

sta_if.isconnected()

time.sleep(3)
