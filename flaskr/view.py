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
from flaskr import app



@app.route('/')
def show_user_blogs():
    cur = g.db.execute('select title, text from user_blog WHERE user_id = ? order by id desc','1')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_user_blogs.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into user_blog (title, text,user_id) values (?, ?,?)',
                 [request.form['title'], request.form['text'],'1'])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_user_blogs'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_user_blogs'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_user_blogs'))
