#what am actualy doing here is import
#a mouduel from another python file

import helpers
helpers.display('sample message', True)

from helpers import display
display('sample message')