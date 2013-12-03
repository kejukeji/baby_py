from flask import render_template, request
from baby.services.more_service import get_tracking, get_visit_record, get_baby_by_id, get_tracking_bar
from baby.util.others import set_session_user, get_session


def to_grow_line(baby_id):
    types = request.args.get('type', 'weight')
    tracking = get_tracking(baby_id, types)
    return render_template('baby/grow_line.html',
                           tracking=tracking,
                           types=types,
                           user_id=get_session('baby_id'),
                           entrance=get_session('entrance'))


def to_grow_bar(baby_id):
    types = request.args.get('type', 'weight')
    breastfeeding, formula_feeding  = get_tracking_bar(baby_id, types)
    return render_template('baby/grow_bar.html',
                           user_id=get_session('baby_id'),
                           entrance=get_session('entrance'),
                           types=types,
                           breastfeeding=breastfeeding,
                           formula_feeding=formula_feeding)


def to_raise():
    return render_template('baby/raise.html')


def to_record(baby_id):
    entrance = str(request.args.get('entrance_type', 'doctor'))
    record, record_count, baby = get_visit_record(baby_id)
    login_id = 0
    if entrance == 'baby':
        set_session_user('entrance', entrance,'user_id', baby_id)
        login_id = get_session('user_id')
    else:
        set_session_user('entrance', entrance,'baby_id', baby_id)
        login_id = get_session('baby_id')
    return render_template('baby/visit_record.html',
                           record=record,
                           record_count=record_count,
                           baby=baby,
                           user_id=login_id,
                           entrance=entrance)


def to_raise_dir():
    return render_template('baby/raise_dir.html')


def to_baby_detail(baby_id):
    baby = get_baby_by_id(baby_id)
    return render_template('baby/detail_info.html',
                           baby=baby,
                           user_id=get_session('baby_id'),
                           entrance=get_session('entrance'))


def to_grow_rate(baby_id):
    return render_template('baby/grow_rate.html',
                           user_id=get_session('baby_id'))