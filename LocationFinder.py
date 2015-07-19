from geopy import geocoders
import json, urllib

gmaps = geocoders.GoogleV3()

def findRepresentatives(latitude, longitude):
    latitude = 'latitude='+str(latitude)+'&'
    longitude = 'longitude=' + str(longitude)+'&'
    API_KEY = 'apikey=55bfc2ea51944ba58364c6f1d84103d1'
    baseURL = 'http://congress.api.sunlightfoundation.com/legislators/locate'
    return json.load(urllib.urlopen(baseURL + '?' + latitude + longitude + API_KEY))

def getReps(address):
    cords = list(gmaps.geocode(address)[1])
    repRes = findRepresentatives(cords[0], cords[1])
    repInfo = repRes['results']
    curList = []
    curDict = {}
    for i in range(0, repRes['count']):
        curDict[repInfo[i]['last_name'] + ', ' + repInfo[i]['first_name']] = repInfo[i]
    return curDict
