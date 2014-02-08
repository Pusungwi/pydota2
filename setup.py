#!/usr/bin/env python
"""
    pydota2
    ~~~~~~

    A module for Dota 2 WebAPI.

    :copyright: (c) 2014 by Yi 'Pusungwi' Yeon Jae
    :license: New BSD License, see LICENSE for more details.
"""

from distutils.core import setup

import os

def get_build():
	path = "./.build"
	
	if os.path.exists(path):
		fp = open(path, "r")
		build = eval(fp.read())
		if os.path.exists("./.increase_build"):
			build += 1
		fp.close()
	else:
		build = 1
	
	fp = open(path, "w")
	fp.write(str(build))
	fp.close()
	
	return str(build)

setup(name = "pydota2",
      version = "0.3." + get_build(),
      author = "Yi Yeon Jae <pusungwi@gmail.com>",
	  description = "A Python module for DOTA 2 WebAPI",
      author_email = "pusungwi@gmail.com",
      url = "http://github.com/pusungwi/pydota2/",
      py_modules = ("pydota2",),
	  license = "BSD"
	)
