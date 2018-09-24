from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
if not len(sys.argv) == 3:
    print ("Invalid number of arguments.")
    sys.exit()
APIKEY=sys.argv[1]
BusLine=sys.argv[2]
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + APIKEY + "&VehicleMonitoringDetailLevel=calls&LineRef="+ BusLine
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
print("Bus Line: " + BusLine)
if(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0].get("VehicleActivity")) :
    print("Number of Active Buses: " + str(len(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])))
    leng=len(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    for j in range(0,leng):
        print("Bus " +  str(j) + " is at latitude " + str(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]) + " and longtiude " + str(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))

else :
    print("Number of Active Buses: 0 ")


