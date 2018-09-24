from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys
if not len(sys.argv) == 4:
    print ("Invalid number of arguments.")
    sys.exit()
APIKEY=sys.argv[1]
BusLine=sys.argv[2]
FName=sys.argv[3]
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + APIKEY + "&VehicleMonitoringDetailLevel=calls&LineRef="+ BusLine
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
f = open(FName, "w")
f.write("Latitude, Longitude,Stop Name,Stop Status \n")
if(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0].get("VehicleActivity")) :
    length=len(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    for j in range(0,length) :
        var=dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["OnwardCalls"].get("OnwardCall")
        if (not var) :
            lat=dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            lot= dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            stopname="N/A"
            stopstatus="N/A"
            f.write(str(lat) + "," +str(lot) + "," + stopname + "," +  stopstatus + "\n")
        else :
            len2=len(dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"])
            for i in range(0,len2):
                lat=dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
                lot= dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
                stopname=dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][i]["StopPointName"]
                stopstatus=dataDict['Siri']["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][j]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][i]["Extensions"]["Distances"]["PresentableDistance"]

                f.write(str(lat) + "," +str(lot) + "," + stopname + "," + stopstatus + "\n")
else :
    print("Number of Active Buses: 0 ")

