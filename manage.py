# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_script import Manager
from app import app
manager = Manager(app)


@manager.command
def start():
    app.run(port=5001, debug=True)

if __name__ == '__main__':
    manager.run()
