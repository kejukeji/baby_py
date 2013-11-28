from flask import render_template, request
from baby.services.more_service import get_tracking


def to_grow_line(id):
    types = request.args.get('type', 'weight')
    tracking = get_tracking(id, types)
    return render_template('baby/grow_line.html',
                           tracking=tracking,
                           types=types)


def to_raise():
    return render_template('baby/raise.html')


def to_record():
    return render_template('baby/visit_record.html')


def to_raise_dir():
    return render_template('baby/raise_dir.html')


def to_baby_detail():
    return render_template('baby/detail_info.html')
