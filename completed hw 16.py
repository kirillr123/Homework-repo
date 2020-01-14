from dms2dec.dms_convert import dms2dec
from geopy.geocoders import Nominatim

f = open("input_data.txt", "r")
raw_data = f.read()
data = raw_data.split(";")

locator = Nominatim(user_agent='myGeocoder')
location = locator.reverse((dms2dec(data[0]),dms2dec(data[1])))

res = f"Input data: {raw_data}\nOutput data: \n" \
      f"Location: {location.raw['display_name']}\n" \
      f"Google Maps URL: https://www.google.com/maps/search/?api=1&query={dms2dec(data[0])},{dms2dec(data[1])}"

f1 = open("output_data.txt", "w")
print(res)
f1.write(res)