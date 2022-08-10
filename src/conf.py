import configparser
from distutils.command.config import config

config_file = configparser.ConfigParser()

config_file.add_section("logger")
config_file.set("logger", "LogLevel", "Info")
config_file.set("logger", "LogFilePath", "/tmp")
config_file.set("logger", "LogFileName", "spike.log")


config_file.add_section("api_1")
config_file.set("default", "ApiKey", "test_key_1")
config_file.set("default", "User", "user_1")
config_file.set("default", "Password", "pass_1")

config_file.add_section("api_2")
config_file.set("default", "ApiKey", "test_key_2")
config_file.set("default", "User", "user_2")
config_file.set("default", "Password", "pass_2")

config_file.add_section("dev")
config_file.set("dev", "Host", "dev.example.com")
config_file.set("default", "Port", 37204)

config_file.add_section("orion")
config_file.set("orion", "Host", "orion.example.com")
config_file.set("default", "Port", 37204)

config_file.add_section("stage")
config_file.set("stage", "Host", "stage.example.com")
config_file.set("default", "Port", 37204)

config_file.add_section("prod")
config_file.set("prod", "Host", "prod.example.com")
config_file.set("default", "Port", 37204)