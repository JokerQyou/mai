#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.models import Role, User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app)


@manager.command
def test():
    '''Run unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
