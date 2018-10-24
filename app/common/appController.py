#! /usr/bin/env python

__author__ = "Andy Tsang"
__credits__ = ["Andy Tsang"]
__version__ = "0.0.0"
__maintainer__ = "Andy Tsang"
__email__ = "atc1992andy@gmail.com"

class AppController():
	def __init__(self, settings, logger, **kwargs):
		self.settings = settings
		self.__logger=logger

		self.sth = "STH YOU IMPORT"

	def start(self):
		self.sth.start()
