# -*- coding: utf-8 -*-

from time import gmtime, strftime
import time
from monitor import WeatherMonitor
from analyst import Analyst
from communicator import send_message

url = "https://www.yr.no/sted/"
monitors = {
    "Storlidalen" : WeatherMonitor("Storlidalen", url + "Norge/Sør-Trøndelag/Oppdal/Storlidalen/varsel.xml"),
    "Sunndalsøra": WeatherMonitor("Sunndalsøra", url + "Norge/Møre_og_Romsdal/Sunndal/Sunndalsøra/varsel.xml"),
    "Isfjorden": WeatherMonitor("Isfjorden", url + "Norge/Møre_og_Romsdal/Rauma/Isfjorden/varsel.xml"),
    "Midsund" : WeatherMonitor("Midsund", url + "Norge/Møre_og_Romsdal/Midsund/Nord-Heggdal~189330/varsel.xml"),
    "Ruten": WeatherMonitor("Ruten", url + "Norge/S%C3%B8r-Tr%C3%B8ndelag/Orkdal/S%C3%B8vatnet/varsel.xml"),
    "Åre" : WeatherMonitor("Åre", url + "Sverige/J%C3%A4mtland/%C3%85re/varsel.xml")
}

analyst = Analyst()
limit = 4

while True:

    try:
        print "Fetching data, making rec. and sending data... (" + strftime("%Y-%m-%d %H:%M", gmtime()) + ")"
        start_time = time.time()
        recommendations = []

        for elem in monitors.keys():

            data = monitors[elem].get_daily_data(limit)
            local_recommendations = analyst.get_recommendation(data, elem)
            recommendations.extend(local_recommendations)

        send_message(recommendations)
        print "Finalized in " + str(time.time() - start_time) + " seconds."
        for r in recommendations: print "\t" + r

    except:
        print "Something went wrong.. warning sent to slack"
        send_message(["Something went wrong.."])

    print "Sleeping until next update...\n"
    time.sleep(21600) # sleeps for 6 hours