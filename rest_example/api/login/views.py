# -*- coding: utf-8 -*-
import logging
from flask import request, render_template, flash, redirect, url_for
from flask_restplus import Resource
from api.restapi import api
from database.models import User
from ..login import login_manager
from database import db
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from .serializers import login_params, user_details

log = logging.getLogger(__name__)

ns = api.namespace('auth', description='Login Authentication')


@ns.route('/home')
class Home(Resource):
    def get():
        return render_template('home.html')


@ns.route("/login")
class LoginUser(Resource):

    @login_manager.user_loader
    def load_user(username):
        return User.query.get(username)

    @api.marshal_with(user_details)
    def get(self):
        form = LoginForm()
        if current_user.is_authenticated():
            flash('You are already logged in.')
            return redirect(url_for('auth.home'))
        return render_template('login.html', form=form)

    @api.expect(login_params)
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = request.form.get('username')
            password = request.form.get('password')

            try:
                User.try_login(username, password)
            except Exception as e:
                flash('Invalid username or password. Please try again.',
                      'danger')
                return render_template('login.html', form=form)

            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username, password)
                db.session.add(user)
                db.session.commit()
            login_user(user)
            flash('You have successfully logged in.', 'success')
            return redirect(url_for('auth.home'))

        if form.errors:
            flash(form.errors, 'danger')

        return render_template('login.html', form=form)


@ns.route('/logout')
class LogOut(Resource):
    @login_required
    def get():
        logout_user()
        return redirect(url_for('auth.home'))
