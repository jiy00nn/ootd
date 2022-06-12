from pyowm import OWM
from geopy.geocoders import Nominatim
import configparser

class Weather:
    def __init__(self, address) -> None:
        geo_local = Nominatim(user_agent='South Korea')
        geo = geo_local.geocode(address)
        latitude = geo.latitude
        longitude = geo.longitude
        
        config = configparser.ConfigParser()
        config.read('config.ini')

        owm = OWM(config['API_KEY']['OPEN_API'])
        mgr = owm.weather_manager()
        self.weather = mgr.weather_at_coords(latitude, longitude).weather

    def get_temperature(self) -> dict:
        return self.weather.temperature('celsius')['temp']

    def get_humidity(self) -> int:
        return self.weather.humidity
