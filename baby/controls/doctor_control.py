from flask import request, render_template



def to_meeting():
    return render_template('doctor/meeting.html')


def to_academic():
    return render_template('doctor/add_visit_record.html')


def to_formula_milk():
    return render_template('doctor/formula_milk.html')

def to_create_baby_account():
    return render_template('doctor/create_baby_account.html')


def to_yy_need():
    return render_template('doctor/yy_need.html')


def to_meeting_notice():
    return render_template('doctor/meeting_notice.html')
