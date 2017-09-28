# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_script import Manager
from app import app

from app.utils import utils
manager = Manager(app)


@manager.command
def start():
    app.run(host='0.0.0.0', port=5001, debug=True)


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', default=5000)
@manager.option('-d', '--data', dest='data')
def send(host, port, data):
    print utils.send(host, port, data)


# script entry
def run():
    manager.run()

if __name__ == '__main__':
    manager.run()
