from flask import render_template
from flask.views import MethodView


class HomeView(MethodView):

    def __init__(self):
        pass

    def get(self):
        return render_template('home.html')
