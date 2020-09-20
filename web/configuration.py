from flask import Flask
from injector import Binder
from environment_config import IEnvironmentConfig, EnvironmentConfig
from web.home_view import HomeView


def configure_web_route(app: Flask):
    app.add_url_rule('/', view_func=HomeView.as_view('home'))
    

def configure_web_binding(binder: Binder):
    binder.bind(IEnvironmentConfig, EnvironmentConfig)
    return binder
