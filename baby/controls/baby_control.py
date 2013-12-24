from flask import render_template, request
from baby.services.more_service import *
from baby.util.others import set_session_user, get_session


def to_grow_line(baby_id):
    record, record_count, baby = get_visit_record(baby_id)
    show_data_way = check_baby_is_week_or_month(baby)
    types = request.args.get('type', 'weight')
    select_type = request.args.get('select_type', 'doctor')
    set_session_user('select_type', select_type, '','')
    if baby:
        baby.select_type = select_type
    way = request.args.get('way', 'week')
    tracking = get_tracking(baby_id, types, show_data_way)
    grow_p3, grow_p15, grow_p75, grow_p95 = get_who_standard(baby_id, types)
    if show_data_way == 'week' and way == 'week':
        if types == 'weight':
            if baby.is_compare == 40:
                grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3 = get_fen_tong_standard(baby_id, types)
                return render_template('baby/grow_line_fentong_weight.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3)
            return render_template('baby/grow_line.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)
        if types == 'height':
            return render_template('baby/grow_line_height_week.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)
        if types == 'head':
            return render_template('baby/grow_line_head_week.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)
    else:
        grow_p3, grow_p15, grow_p75, grow_p95 = get_who_standard_month(baby_id, types)
        if types == 'weight':
            if baby.is_compare == 40:
                grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3 = get_fen_tong_standard(baby_id, types)
                return render_template('baby/grow_line_fentong_weight.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3)
            return render_template('baby/grow_line_month.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)
        if types == 'height':
            return render_template('baby/grow_line_height_month.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)
        if types == 'head':
            return render_template('baby/grow_line_head_month.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95)


def to_nine_grow_line(baby_id):
    record, record_count, baby = get_visit_record(baby_id)
    show_data_way = check_baby_is_week_or_month(baby)
    types = request.args.get('type', 'weight')
    way = request.args.get('way', 'week')
    select_type = get_session('select_type')
    if baby:
        baby.select_type = select_type
    tracking = get_tracking(baby_id, types, show_data_way)
    grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3, grow_negative2, grow_negative1 = get_nine_standard(baby_id, types)
    if types == 'weight':
            return render_template('baby/grow_line_nine.html',
                                   tracking=tracking,
                                   types=types,
                                   user_id=get_session('baby_id'),
                                   entrance=get_session('entrance'),
                                   baby=baby,
                                   grow_p3=grow_p3,
                                   grow_p15=grow_p15,
                                   grow_p75=grow_p75,
                                   grow_p95=grow_p95,
                                   grow_negative3=grow_negative3,
                                   grow_negative2=grow_negative2,
                                   grow_negative1=grow_negative1)
    if types == 'height':
        return render_template('baby/grow_line_nine_height.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3,
                               grow_negative2=grow_negative2,
                               grow_negative1=grow_negative1)
    if types == 'head':
        return render_template('baby/grow_line_nine_head.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3,
                               grow_negative2=grow_negative2,
                               grow_negative1=grow_negative1)


def to_fen_tong_grow_line(baby_id):
    record, record_count, baby = get_visit_record(baby_id)
    show_data_way = check_baby_is_week_or_month(baby)
    types = request.args.get('type', 'weight')
    way = request.args.get('way', 'week')
    select_type = select_type = get_session('select_type')
    if baby:
        baby.select_type = select_type
    tracking = get_tracking(baby_id, types, show_data_way)
    grow_p3, grow_p15, grow_p75, grow_p95, grow_negative3 = get_fen_tong_standard(baby_id, types)
    if types == 'weight':
        return render_template('baby/grow_line_fentong_weight.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3)
    if types == 'height':
        return render_template('baby/grow_line_fentong_height.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3)
    if types == 'head':
        return render_template('baby/grow_line_fentong_head.html',
                               tracking=tracking,
                               types=types,
                               user_id=get_session('baby_id'),
                               entrance=get_session('entrance'),
                               baby=baby,
                               grow_p3=grow_p3,
                               grow_p15=grow_p15,
                               grow_p75=grow_p75,
                               grow_p95=grow_p95,
                               grow_negative3=grow_negative3)


def to_grow_bar(baby_id):
    analysis = get_analysis_data(baby_id)
    breastfeeding, formula_feeding  = get_tracking_bar(baby_id, None)
    return render_template('baby/grow_bar.html',
                           user_id=get_session('baby_id'),
                           entrance=get_session('entrance'),
                           analysis=analysis,
                           breastfeeding=breastfeeding,
                           formula_feeding=formula_feeding)


def to_raise():
    #get_tracking_test(1, 'weight', 'week')
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
    record, record_count, baby = get_visit_record(baby_id)
    return render_template('baby/grow_rate.html',
                           user_id=get_session('baby_id'),
                           baby=baby)