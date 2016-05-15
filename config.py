# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL',
        'sqlite:///{}'.format(os.path.join(basedir, 'data-dev.sqlite'))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BOOTSTRAP_SERVE_LOCAL = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL',
        'sqlite:///{}'.format(os.path.join(basedir, 'data-test.sqlite'))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BOOTSTRAP_SERVE_LOCAL = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///{}'.format(os.path.join(basedir, 'data.sqlite'))
    )


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
