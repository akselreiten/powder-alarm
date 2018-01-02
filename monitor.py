# -*- coding: utf-8 -*-

import urllib2
import xmltodict

class WeatherMonitor:

    def __init__(self, location, url):
        self.location = location
        self.url = url
        self.data = None

    def __update_weather_data(self):
        try:
            file = urllib2.urlopen(self.url)
            raw_data = file.read()
            raw_data = xmltodict.parse(raw_data)
            file.close()
            self.data = raw_data["weatherdata"]["forecast"]["tabular"]["time"]
        except:
            print "An error occured when fetching data from www.yr.no for " + self.data
            self.data = None

    def get_daily_data(self, limit=None):

        self.__update_weather_data()
        if self.data == None:
            return None

        weather_data = {}
        included_days = set([])
        limit_count = 0
        for elem in self.data:

            day = elem["@from"].split("T")[0]
            if limit != None and limit_count <= limit:
                if day not in included_days:
                    limit_count += 1
                included_days.add(day)
            if day not in weather_data:
                weather_data[day] = {"symbol" : [],"precipitation" : [],"temperature" : [] }

            symbol = elem["symbol"]["@name"]
            temperature = elem["temperature"]["@value"]
            precipitation = elem["precipitation"]["@value"]

            weather_data[day]["symbol"].append(symbol)
            weather_data[day]["temperature"].append(float(temperature))
            weather_data[day]["precipitation"].append(float(precipitation))

        if isinstance(limit,int) and limit < len(weather_data) and limit >= 0:
            weather_data_limited = {}
            for key in included_days:
                weather_data_limited[key] = weather_data[key]
            return weather_data_limited
        else:
            return weather_data

