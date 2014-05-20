#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'FEDORA-DEMO'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                              'db_demo.db')
    SQLALCHEMY_ECHO = True
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "f3do$a"
    # UPLOADS_FOLDER = os.path.realpath('.') + '/uploads/'
    # ALLOWED_EXTENSIONS = ['ogv', 'avi', 'mpeg']


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'FEDORA-TEST'
