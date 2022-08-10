import argparse
import sys

def create(args):
	print("create")
def explain(args):
	print("explain")
def config_view(args):
	print("view")
def config_set(args):
	print("({},{})".format(args.attribute, args.value))

def config_unset(args):
	print(args.attribute)


def main_parser():
	"""parser object that handles arguments"""
	parser = argparse.ArgumentParser(description="A test CLI meant to test pythons configparser")

	subparser = parser.add_subparsers()

	create_parser = subparser.add_parser("create")
	create_parser.set_defaults(func=create)

	explain_parser = subparser.add_parser("explain")
	explain_parser.set_defaults(func=explain)


	config_parser = subparser.add_parser("config")
	config_subparser = config_parser.add_subparsers()
	view_config_parser = config_subparser.add_parser("view")
	view_config_parser.set_defaults(func=config_view)

	set_config_parser = config_subparser.add_parser("set")
	set_config_parser.add_argument("attribute")
	set_config_parser.add_argument("value")
	set_config_parser.set_defaults(func=config_set)

	unset_config_parser = config_subparser.add_parser("unset")
	unset_config_parser.add_argument("attribute")
	unset_config_parser.set_defaults(func=config_unset)


	# set_config_parser = config_parser.add_argument("set")
	# unset_config_parser = config_parser.add_argument("unset")

	return parser

def main():
	parser = main_parser()

	# if there are no arguments given print the help
	# fixes a issue with python giving a false error
	if len(sys.argv) == 1:
		parser.print_help()
		parser.exit()
	
	args = parser.parse_args()
	args.func(args)

if __name__ == "__main__":
    main()
