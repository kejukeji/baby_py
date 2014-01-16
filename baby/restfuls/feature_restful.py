# coding: UTF-8


from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.feature_service import insert_formula
from baby.util.others import success_dic, fail_dic
from baby.services.more_service import insert_visit_record


class AddFormula(restful.Resource):
    """
    增加配方奶
       court_id： 院内，院外
       bran_id： 品牌
       kind： 种类
       energy: 能量
       protein: 蛋白质
       carbohydrates: 碳化合物
       fat: 脂肪
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('court_id', type=str, required=True, help=u'court_id 必须')
        parser.add_argument('brand_id', type=str, required=True, help=u'brand_id 必须')
        parser.add_argument('kind', type=str, required=True, help=u'type 必须')
        parser.add_argument('energy', type=str, required=False, help=u'energy 必须')
        parser.add_argument('protein', type=str, required=False, help=u'protein 必须')
        parser.add_argument('carbohydrates', type=str, required=False, help=u'carbon_compound 必须')
        parser.add_argument('fat', type=str, required=False, help=u'axunge 必须')

        args = parser.parse_args()

        court_id = args['court_id']
        brand_id = args['brand_id']
        kind = args['kind']
        energy = args['energy']
        protein = args['protein']
        carbohydrates = args['carbohydrates']
        fat = args['fat']

        success = success_dic().dic
        fail = fail_dic().dic

        is_ture = insert_formula(court_id, brand_id, kind, energy, protein, carbohydrates, fat)

        if is_ture:
            success['msg'] = '添加成功'
            return success
        else:
            fail['msg'] = '添加失败'
            return fail


class AddVisitRecord(restful.Resource):
    """
    新增随访记录
    """
    @staticmethod
    def post():
        """
        参数
        baby_id  婴儿id
        measure_date: 测量日期
        weight: 体重
        height: 身长
        head: 头围
        breastfeeding: 母乳喂养
        location: 院内/外
        brand: 品牌
        kind: 种类
        nutrition: 配方奶营养量
        add_type: 添加类型(baby,doctor如果时妈妈端登陆添加的就是baby，医生端登陆添加的就是doctor)
        """
        parser = reqparse.RequestParser()
        parser.add_argument('baby_id', type=str, required=True, help=u'baby_id 必须')
        parser.add_argument('measure_date', type=str, required=True, help=u'measure_date 必须')
        parser.add_argument('weight', type=str, required=True, help=u'weight 必须')
        parser.add_argument('height', type=str, required=True, help=u'height 必须')
        parser.add_argument('head', type=str, required=True, help=u'head 必须')
        parser.add_argument('breastfeeding', type=str, required=True, help=u'breastfeeding 必须')
        parser.add_argument('location', type=str, required=True, help=u'location 必须')
        parser.add_argument('brand', type=str, required=True, help=u'brand 必须')
        parser.add_argument('kind', type=str, required=True, help=u'kind 必须')
        parser.add_argument('nutrition', type=str, required=True, help=u'nutrition 必须')
        parser.add_argument('add_type', type=str, required=False)

        args = parser.parse_args()

        success = success_dic().dic
        fail = fail_dic().dic

        baby_id = args['baby_id']
        measure_date = args['measure_date']
        weight = args['weight']
        height = args['height']
        head = args['head']
        breastfeeding = args['breastfeeding']
        location = args['location']
        brand = args['brand']
        kind = args['kind']
        nutrition = args['nutrition']
        add_type = args['add_type']

        is_ture = insert_visit_record(baby_id, measure_date, weight, height, head, location, brand,
                                      breastfeeding, kind, nutrition, add_type)
        if is_ture:
            success['msg'] = '添加成功'
            return success
        else:
            fail['msg'] = '添加失败'
            return fail