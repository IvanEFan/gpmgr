import os

NAME = 'gpmgr'
DESCRIPTION = 'A command line tool to help you manage your local git profiles.'
VERSION = '1.0.0'

AUTHOR = 'IvanEFan'


usr_home = os.path.expanduser('~')

GPMGRCONF_PATH = os.path.join(usr_home, '.gpmgrconf')

