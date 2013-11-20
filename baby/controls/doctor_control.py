from flask import request, render_template



def to_meeting():
    return render_template('doctor/meeting.html')
