#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-15 00:10:41
# @Author  : zheng guang (zzglfh@gmail)
# @Link    :
# @Version : $Id$

# all the imports
import sqlite3
import os
from flask import Flask, request, session, g,jsonify, redirect, url_for, abort, render_template, flash
from flaskr import app


@app.route('/user')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
