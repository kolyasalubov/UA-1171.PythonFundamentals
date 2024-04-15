from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('64d8c4fd75d87984f685e491371e3050')
# API_KEY = OWM('64d8c4fd75d87984f685e491371e3050')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75


