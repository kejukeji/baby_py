from flask import request, render_template



def to_meeting():
    return render_template('doctor/meeting.html')


def to_academic():
    return render_template('doctor/academic.html')
