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
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('court_id', type=str, required=True, help=u'court_id 必须')
        parser.add_argument('brand_id', type=str, required=True, help=u'brand_id 必须')
        parser.add_argument('type', type=str, required=True, help=u'type 必须')
        parser.add_argument('energy', type=str, required=True, help=u'energy 必须')
        parser.add_argument('protein', type=str, required=True, help=u'protein 必须')
        parser.add_argument('carbon_compound', type=str, required=True, help=u'carbon_compound 必须')
        parser.add_argument('axunge', type=str, required=True, help=u'axunge 必须')

        args = parser.parse_args()

        court_id = args['court_id']
        brand_id = args['brand_id']
        types = args['type']
        energy = args['energy']
        protein = args['protein']
        carbon_compound= args['carbon_compound']
        axunge = args['axunge']

        success = success_dic().dic
        fail = fail_dic().dic

        is_ture = insert_formula(court_id, brand_id, types, energy, protein, carbon_compound, axunge)

        if is_ture:
            return success
        else:
            return fail