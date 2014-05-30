#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  KSP.py
#  
#  Copyright 2014 valentin basel <valentin@localhost.localdomain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from pykickstart.parser import *
from pykickstart.version import makeVersion


class KSP:
    """ Class doc """
    
    def __init__ (self):
        """ Class initialiser """
        self.ksparser = KickstartParser(makeVersion())
        
        
    def load(self,data):
        print data
        if data=="terminal":
            self.ksparser.readKickstart("/usr/share/spin-kickstarts/fedora-livecd-desktop.ks")
        
    def print_screen(self):
        return self.ksparser.handler.__str__()
        
    def add_pkg(self,data):
        print "pkg"
        try:
            self.ksparser.handler.packages.add(["@"+str(data)])
            return True
        except Exception, ex:
            return False


