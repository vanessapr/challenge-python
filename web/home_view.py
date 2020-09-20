from flask import render_template, request, flash
from flask.views import MethodView
from injector import inject
from use_cases.i_list_use_case import IListUseCase
from use_cases.exceptions import InvalidEntryList


class HomeView(MethodView):

    @inject
    def __init__(self, list_use_case: IListUseCase):
        self.list_use_case = list_use_case

    def get(self):
        return render_template('home.html')

    def post(self):
        input_user = request.form.get('input')

        try:
            result = self.list_use_case.flatten_list(input_user)
            return render_template('home.html', result=result), 200
        except InvalidEntryList:
            flash('Invalid input list. Please try again!', 'error')
            return render_template('home.html'), 400

