# -*- coding: utf-8 -*-

from dateutil import parser

class Analyst:

    def __init__(self, temperature_upper_limit=2.0, precipitation_lower_limit=5.0):
        self.temperature_upper_limit = temperature_upper_limit
        self.precipitation_lower_limit = precipitation_lower_limit

    def get_recommendation(self, data, location):

        recommendations = []

        for elem in data.keys():

            symbol = data[elem]["symbol"]
            precipitation = data[elem]["precipitation"]
            temperature = data[elem]["temperature"]

            snow = 0
            for i in range(len(symbol)):
                if temperature[i] <= self.temperature_upper_limit:
                    snow += precipitation[i]

	    if snow >= self.precipitation_lower_limit:
                dow = parser.parse(elem).strftime("%a")
                recommendations.append("Powder alarm @ " + str(location) + ": " + str(snow) + " mm (" + str(dow) + ", " + str(elem) + ")")
        return recommendations
