from conf import Config
from cli import Parser

CONFIG_FILENAME = "config"
CONFIG_FILEPATH = ".spike"

if __name__ == "__main__":
	config = Config(CONFIG_FILEPATH, CONFIG_FILENAME)
	parser = Parser(config)
	parser.parse()