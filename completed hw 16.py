from dms2dec.dms_convert import dms2dec
from geopy.geocoders import Nominatim


def reverse_geocode(coords):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.reverse((coords[0], coords[1]))

    res = f"Output data: \n" \
          f"Location: {location.raw['display_name']}\n" \
          f"Google Maps URL: https://www.google.com/maps/search/?api=1&query={coords[0]},{coords[1]}"
    return res


if __name__ == "__main__":
    f = open("input_data.txt", "r")
    raw_data = f.read()
    data = raw_data.split(";")
    coordinates = dms2dec(data[0]), dms2dec(data[1])
    print(f"Input data: {raw_data}")
    print(reverse_geocode(coordinates))
