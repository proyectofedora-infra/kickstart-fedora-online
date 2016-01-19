#!/usr/bin/env python
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
#        self.ksparser = KickstartParser(makeVersion())

        
    def start(self):
        self.ksparser = KickstartParser(makeVersion())

    def load(self,data):
        print data
        if data=="terminal":
            self.ksparser.readKickstart("ks/fedora-live-base.ks")
        if data=="gnome":
            self.ksparser.readKickstart("ks/fedora-live-workstation.ks")
        if data=="kde":
            self.ksparser.readKickstart("ks/fedora-live-kde.ks")
        if data=="xfce":
            self.ksparser.readKickstart("ks/fedora-live-xfce.ks")
        if data=="lxde":
            self.ksparser.readKickstart("ks/fedora-live-lxde.ks")
    def print_screen(self):
        #print type(self.ksparser.handler.__str__())
        return self.ksparser.handler.__str__().decode("ascii")
        
    def add_pkg(self,data):
        print "pkg"
        try:
            self.ksparser.handler.packages.add(["@"+str(data)])
            return True
        except Exception, ex:
            return False
    def lang_time_key(self,key,lang,time):
        """docstring for lang_time_key"""
        self.ksparser.handler.keyboard.keyboard=key
        self.ksparser.handler.lang.lang=lang
        self.ksparser.handler.timezone.timezone=time
        return True

