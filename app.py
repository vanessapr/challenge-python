import jinja2
from flask import Flask
from flask_injector import FlaskInjector
from environment_config import EnvironmentConfig
from web.configuration import configure_web_route, configure_web_binding
from use_cases.configuration import configure_use_case_binding

template_folders = [
    './web/templates'
]

ROUTING_MODULES = [
    configure_web_route
]

modules_list = [
    configure_web_binding,
    configure_use_case_binding
]


def create_app(template_folders_list=template_folders, modules=modules_list):
    application = Flask(__name__)

    application.config['SECRET_KEY'] = EnvironmentConfig.SECRET_KEY

    for routing in ROUTING_MODULES:
        routing(application)

    application.jinja_loader = jinja2.ChoiceLoader([
        application.jinja_loader,
        jinja2.FileSystemLoader(template_folders_list)
    ])

    FlaskInjector(app=application, modules=modules)

    return application


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=EnvironmentConfig.PORT, debug=EnvironmentConfig.MODE_DEBUGGER)
