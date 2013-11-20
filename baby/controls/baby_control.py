from flask import render_template, request


def to_grow_line():
    return render_template('baby/grow_line.html')


def to_raise():
    return render_template('baby/raise.html')
