from flask import render_template, request
from baby.services.more_service import get_tracking


def to_grow_line(id):
    tracking = get_tracking(id)
    return render_template('baby/grow_line.html',
                           tracking=tracking)


def to_raise():
    return render_template('baby/raise.html')


def to_record():
    return render_template('baby/visit_record.html')


def to_raise_dir():
    return render_template('baby/raise_dir.html')


def to_baby_detail():
    return render_template('baby/detail_info.html')
