#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, Response, request
from sqlite3 import connect


app = Flask(__name__)


@app.route("/")
def index():
    return Response("MyRealToDo", status=200, mimetype="text/plain")


@app.route("/api/v1.0/tasks", methods=["GET"])
def getTasks():
    conn = connect("db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    r = [
        dict((cur.description[i][0], value) for i, value in enumerate(row))
        for row in cur.fetchall()
    ]
    conn.close()
    return jsonify(tasks=r)


@app.route("/api/v1.0/tasks/<int:id>", methods=["GET"])
def getTask(id):
    conn = connect("db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos WHERE id=?", (id))
    r = [
        dict((cur.description[i][0], value) for i, value in enumerate(row))
        for row in cur.fetchall()
    ]
    conn.close()
    return jsonify(task=r)


@app.route("/api/v1.0/tasks", methods=["POST"])
def addTask():
    data = request.json
    if "nome" and "prioridade" and "status" and "depende" in data:
        conn = connect("db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO todos (nome, prioridade, status, depende) VALUES (?,?,?,?)",
            (data["nome"], data["prioridade"], data["status"], data["depende"]),
        )
        conn.commit()
        data["id"] = cur.lastrowid
        conn.close()
        return jsonify(data)
    else:
        return Response("Falta parametros!", status=400, mimetype="text/plain")


@app.route("/api/v1.0/tasks/<int:id>", methods=["PUT"])
def updateTask(id):
    return "updateTask()!"


@app.route("/api/v1.0/tasks/<int:id>", methods=["DELETE"])
def deleteTask(id):
    return "deleteTask()!"


@app.route("/healtcheck", methods=["GET"])
def healthcheck():
    return Response("Awake and Alive", status=200, mimetype="text/plain")
