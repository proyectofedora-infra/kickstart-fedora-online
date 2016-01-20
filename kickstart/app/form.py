#!/usr/bin/env python
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
import json
class ksForm(Form):
    check=[]
    chk_res={}
    dicc_locale={}
    check_group=[]
    time_zone = SelectField(u'Select time zone',validators = [Optional()])
    select_locale=SelectField(u'Select locale',validators = [Optional()])
    select_kyemap=SelectField(u'Select keymap',validators = [Optional()])
        #tegno que crear un dicc para el keyboard, timezone, y lang
    def __init__(self,*args,**kwargs):
        super(ksForm,self).__init__(*args,**kwargs)
        self.check=self.create_dicc() # armo la lista de valores para el checkbox 
        self.time_zone.choices=self.create_time_zone("app/dat/timezones_list.txt")
        self.select_locale.choices=self.create_locale("app/dat/locale.json")
        self.select_kyemap.choices=self.create_keymap("app/dat/teclado.txt")
        self.check_group=self.create_group_list()
        self.dicc_locale=self.locale_dicc("app/dat/locale.json")

    def locale_dicc(self,FILE):
        dicc={}
        json_f=open(FILE,'r')
        dicc=json.load(json_f)
        return dicc
    def create_locale(self,FILE):
        """ Function doc """
        dicc_loc={}
        lis_dicc=[]
        file_json=open(FILE,"r")
        #for value in f:
        #    aux=value.split("16")
        #    list_loc.append((aux[1].decode('utf-8'),aux[1].decode('utf-8'))) 
        dicc_loc=json.load(file_json)
        for dicc_key in dicc_loc:
            lis_dicc.append((dicc_loc[dicc_key],dicc_key))
        order_list= sorted(lis_dicc,key=lambda value: value[1])
        #print order_list

        return order_list 

            
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
        file_json=open("app/dat/groups.json","r")
        json_dat=json.load(file_json)
        #print json_dat 
        #json_key=json_dat.keys()
        #json_key.sort()
        #for key in json_key:
        #    key_low=key.lower()
        #    list_grp=[]
        #    dic_grp_info={}
        #    for dato_grp in json_dat[key]:
        #        dic_grp_info[dato_grp]="soy un tool tip"
        #        list_grp.append(dic_grp_info)
                
        #    internal_check.append([key_low.replace(" ","-"), dic_grp_info ])
             
        return json_dat 
    def create_group_list(self):
        """

        """
        internal_grp_list=[]
        for category_dic in  self.check:
            for grp_dicc in self.check[category_dic]:
                for grp_dicc_aux in grp_dicc:
                    internal_grp_list.append(grp_dicc_aux)
        #print internal_grp_list
        return internal_grp_list


