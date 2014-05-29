#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  form.py
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
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, RadioField , SelectField
from wtforms.validators import Required , Optional
import os , sys
import subprocess
import locale

class ksForm(Form):
    check=[]
    chk_res={}
    time_zone = SelectField(u'Select time zone',validators = [Optional()])
    select_locale=SelectField(u'Select locale',validators = [Optional()])
    select_kyemap=SelectField(u'Select keymap',validators = [Optional()])
    
    def __init__(self,*args,**kwargs):
        super(ksForm,self).__init__(*args,**kwargs)
        self.check=self.create_dicc() # armo la lista de valores para el checkbox 
        self.time_zone.choices=self.create_time_zone("app/static/timezones_list.txt")
        self.select_locale.choices=self.create_locale("app/static/locale.txt")
        self.select_kyemap.choices=self.create_keymap("app/static/teclado.txt")
        
    def create_locale(self,FILE):
        """ Function doc """
        list_loc=[]
        f=open(FILE,"r")
        for value in f:
            aux=value.split("16")
            list_loc.append((aux[1].decode('utf-8'),aux[1].decode('utf-8'))) 
        return list_loc
            
    def create_keymap (self,FILE):
        """ Function doc """
        list_key=[]
        f=open(FILE,"r")
        for value in f:
            list_key.append((value.decode('utf-8'),value.decode('utf-8'))) 
        return list_key
        
    def create_time_zone (self,FILE):
        """ Function doc """
        list_time=[]
        f=open(FILE,"r")
        for value in f:
            list_time.append((value.decode('utf-8'),value.decode('utf-8'))) 
        return list_time
        
    def create_dicc(self):
        internal_check=[]
        f=open("app/static/yum.txt","r")
        for value in f:
            aux=value.split("#")
            dat0=aux[0].strip(" ")
            dat1=aux[1].strip(" ")

            internal_check.append((dat0,dat1))
            self.chk_res[dat0]=None
        f.close()
        internal_check.sort()
        return internal_check



