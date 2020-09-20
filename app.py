import jinja2
from flask import Flask
from flask_injector import FlaskInjector
from environment_config import EnvironmentConfig
from web.configuration import configure_web_route, configure_web_binding

template_folders = [
    './web/templates'
]

ROUTING_MODULES = [
    configure_web_route
]

modules_list = [
    configure_web_binding
]


def create_app(template_folders_list=template_folders, modules=modules_list):
    application = Flask(__name__)

    for routing in ROUTING_MODULES:
        routing(application)

    application.jinja_loader = jinja2.ChoiceLoader([
        application.jinja_loader,
        jinja2.FileSystemLoader(template_folders_list)
    ])

    FlaskInjector(app=application, modules=modules)

    return application


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=EnvironmentConfig.PORT, debug=EnvironmentConfig.MODE_DEBUGGER)
