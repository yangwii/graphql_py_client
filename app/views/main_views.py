# -*- coding: utf-8 -*-

from __future__ import absolute_import
import json
from app import app
from flask import render_template
from flask import request, jsonify
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/sendqlpost', methods=['POST'])
def sendqlpost():
    host = request.form.get('host')
    req = request.form.get('req')
    client = Client(
        retries=3,
        transport=RequestsHTTPTransport(url=host)
    )
    query = gql(req)
    response = client.execute(query)
    return jsonify(res=json.dumps(response), status=200)

