# -*- coding: utf-8 -*-
from kickstart.core.database import db
'''
Updated Models / Uploading ER diagram soon.
'''


class UserProfile(db.Model):
    __tablename__ = 'profile'

    user_id = db.Column(db.Integer, primary_key=True)
    open_id = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    about = db.Column(db.Text())
    date_registered = db.Column(db.DateTime())
    website = db.Column(db.String())

    def __init__(self, open_id, username,
                 email, about, date, website):
        self.open_id = open_id
        self.username = username
        self.email = email
        self.about = about
        self.date_registered = date
        self.website = website











