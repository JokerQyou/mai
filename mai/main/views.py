# -*- coding: utf-8 -*-
from flask import render_template

from . import main


@main.route('/', methods=('GET', ))
def view_index():
    return render_template('index.html')
