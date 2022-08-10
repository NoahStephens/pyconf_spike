import argparse
import sys

class Parser:
	def __init__(self, config):
		self.config = config # set config

		self.parser = self.main_parser()

		# if there are no arguments given print the help
		# fixes a issue with python giving a false error
		if len(sys.argv) == 1:
			self.parser.print_help()
			self.parser.exit()
	
	def parse(self):
		"""function parses arguments"""
		args = self.parser.parse_args()
		args.func(args)

	def _create(self, args):
		print("create")

	def _explain(self, args):
		print("explain")

	def _config_view(self, args):
		print(self.config.get(args.attribute))

	def _config_set(self, args):
		self.config.add(args.attribute)
		print("({},{}) = {}".format(args.attribute.split(".")))

	def _config_unset(self, args):
		self.config.remove(args.attribute)
		print(args.attribute)

	def main_parser(self):
		"""parser object that handles arguments"""
		parser = argparse.ArgumentParser(description="A test CLI meant to test pythons configparser")

		subparser = parser.add_subparsers()

		create_parser = subparser.add_parser("create")
		create_parser.set_defaults(func=self._create)

		explain_parser = subparser.add_parser("explain")
		explain_parser.set_defaults(func=self._explain)


		config_parser = subparser.add_parser("config")
		config_subparser = config_parser.add_subparsers()
		view_config_parser = config_subparser.add_parser("view")
		view_config_parser.add_argument("attribute")
		view_config_parser.set_defaults(func=self._config_view)

		set_config_parser = config_subparser.add_parser("set")
		set_config_parser.add_argument("attribute")
		set_config_parser.set_defaults(func=self._config_set)

		unset_config_parser = config_subparser.add_parser("unset")
		unset_config_parser.add_argument("attribute")
		unset_config_parser.set_defaults(func=self._config_unset)


		# set_config_parser = config_parser.add_argument("set")
		# unset_config_parser = config_parser.add_argument("unset")

		return parser

if __name__ == "__main__":
	from src.conf import Config
	parser = Parser(Config(".spike_test", "config_test"))
	parser.parse()