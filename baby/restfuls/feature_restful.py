# coding: UTF-8


from flask.ext import restful
from flask.ext.restful import reqparse
from baby.services.feature_service import insert_formula
from baby.util.others import success_dic, fail_dic


class AddFormula(restful.Resource):
    """
    增加配方奶
       court_id： 院内，院外
       bran_id： 品牌
       type： 种类
       energy: 能量
       protein: 蛋白质
       carbon_compound: 碳化合物
       axunge: 脂肪
       name: 配方奶名称
    """
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('court_id', type=str, required=True, help=u'court_id 必须')
        parser.add_argument('brand_id', type=str, required=True, help=u'brand_id 必须')
        parser.add_argument('kind', type=str, required=True, help=u'type 必须')
        parser.add_argument('energy', type=str, required=True, help=u'energy 必须')
        parser.add_argument('protein', type=str, required=True, help=u'protein 必须')
        parser.add_argument('carbohydrates', type=str, required=True, help=u'carbon_compound 必须')
        parser.add_argument('fat', type=str, required=True, help=u'axunge 必须')

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