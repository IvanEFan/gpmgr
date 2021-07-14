import os
from gpmgr import constant

# Create .gpmgrconf file is it is not exist
if not os.path.isfile(constant.GPMGRCONF_PATH):
    with open(constant.GPMGRCONF_PATH, 'w+'):
        pass
