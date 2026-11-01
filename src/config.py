import configparser
import os

config = configparser.ConfigParser()
# SIGNALING EXTENSION: the config file can be chosen with the IDS_CONFIG
# environment variable (e.g. IDS_CONFIG=signaling_toy.conf). If it is not set,
# the original behaviour is kept and 'project.conf' is read.
config.read(os.environ.get('IDS_CONFIG', 'project.conf'))

#print(config.getint('parameter', 'max_episodes'))
