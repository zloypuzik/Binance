import time 
import datetime 
import json 
import websocket 
from threading import * 
from binance.client import Client 


def f_minqty_size_up(kolichestvo, stepSize): 

	def adjust_to_step(value, step, increase=True): 
		return ((int(value * 100000000) - int(value * 100000000) % int( 
			float(step) * 100000000)) / 100000000) + (float(step) if increase else 0) 
	sell_amount_a = adjust_to_step(kolichestvo, stepSize) 
	return sell_amount_a 


def f_minqty_size_down(kolichestvo, stepSize): 

	def adjust_to_step(value, step, increase=False): 
		return ((int(value * 100000000) - int(value * 100000000) % int( 
			float(step) * 100000000)) / 100000000) + (float(step) if increase else 0) 
	sell_amount_a = adjust_to_step(kolichestvo, stepSize) 
	return sell_amount_a 


api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG' 
secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA' 

client = Client(api_key, secret_key) 

usdt_count = float(0.01) 

all_pribil = float(0.0) 

