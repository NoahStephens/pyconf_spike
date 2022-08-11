from configparser import ConfigParser
from genericpath import exists
from pathlib import Path
import os

class Config:
	def __init__(self, filepath=".spike", filename="config"):
		self.config = ConfigParser()
		self.path = str(Path.home()) + "/" + filepath
		self.filename = filename
		
		# check if there is a config, create one if there is not one
		if not os.path.exists(self.path):
			os.makedirs(self.path)
			self._update_config()

		# load the config.ini to config obj
		self._load_config()
			

	def _load_config(self):
		"""loads config.ini into ConfigParser """
		self.config.read(os.path.join("src", "config.ini"))

	def _update_config(self):
		"""updates users config file with current"""
		with open(os.path.join(self.path, self.filename), 'w') as file:
			self.config.write(file)
			file.flush()
			file.close()

	def add(self, attribute):
		""" adds formatted key into config
			section.key.value"""
		section, key, value = attribute.split(".")
		self.config.set(section, key, value)
		self._update_config()
		return "{}.{}.{}".format(section, key, value)

	def delete(self, attribute):
		""" removes formatted key into config
			section.key"""
		section, key = attribute.split(".")
		self.config.remove_option(section, key)
		self._update_config()

	def get(self, attribute):
		section, key = attribute.split(".")
		value = self.config.get(section, key)
		return "{}.{}.{}".format(section, key, value)

if __name__ == "__main__":
	config = Config(".spike_test", "config_test")