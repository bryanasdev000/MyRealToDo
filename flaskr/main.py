#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, Response, jsonify
from sqlite3 import connect


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/api/v1.0/tasks')
def getTasks():
    conn = connect("db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos')
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    conn.close()
    return jsonify(tasks = r)
    

@app.route('/healtcheck')
def healthcheck():
    return Response("Awake and Alive", status=200, mimetype='text/plain')


