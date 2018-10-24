#! /usr/bin/env python
import time
import cv2
import argparse, json
from pyutil import basic_args, str2bool, PyLogger
from app import AppController

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

def run(arg):
	# import Setting
	setting_path = "setting.json"
	with open(setting_path) as setting_buffer:
		settings = json.loads(setting_buffer.read())
	# set arg to settings
	settings["app"]["dummy"] = arg.dummy
	settings["app"]["dummy2"] = arg.dummy2
	settings["app"]["dummy3"] = None if arg.dummy3 is None else arg.dummy3
	logger = PyLogger(log=True,debug=True)

	app = AppController(settings=settings, logger=logger)
	app.start()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Desc")
	parser = basic_args(parser)
	parser.add_argument("-d1", "--dummy", type=int, default=0,
						help="Dummy int please change.")
	parser.add_argument("-d2", "--dummy2", type=str2bool, nargs='?',
						const=True,
						help="Dummy bool please change.")
	parser.add_argument("-d3", "--dummy3", type=str, default=None,
						 help="Dummy str please change.")

	arg = parser.parse_args()
	st = time.time()
	run(arg)
	print("Finished:{}".format(time.time()-st))
