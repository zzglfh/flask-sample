#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-15 00:10:41
# @Author  : zheng guang (zzglfh@gmail)
# @Link    : 
# @Version : $Id$

# all the imports
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)



#TODO read config from file
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    app.logger.debug('database: %s',app.config['DATABASE'])
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    app.logger.debug('init sql: ')
    with closing(connect_db()) as db:
        with app.open_resource('init.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


def run():
    init_db()
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    print "init sql"
    init_db()
    print  "run"
    app.logger.setLevel("DEBUG")
    app.run()


import flaskr.view
