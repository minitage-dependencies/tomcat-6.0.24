#!/usr/bin/env python

# Copyright (C) 2009, Mathieu PASQUET <mpa@makina-corpus.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'
import os
import shutil
def h(options=None,buildout=None):
    os.chmod(
        os.path.join(options['compile-directory'], 'configure'),
        0750)

def m(options=None,buildout=None):
    shutil.copy2(
        os.path.join(options['compile-directory'], 'jsvc'),
        os.path.join(
            buildout['buildout']['directory'],
            'parts', 'part', 'bin', 'jsvc'
        )
    )
# vim:set et sts=4 ts=4 tw=80:
