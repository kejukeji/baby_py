# coding: UTF-8

from .hospital_model import *
from .baby_model import Baby
from .feature_model import *
from .standard import *
from .nine_standard import *
from .fentong_standard import *

from .database import db, Base, engine
# todo-lyw 如何实现更好的包导入规则，init里面的导入无法事项相对路径，这个文件 <-
# -> 夹里面的包可以使用.导入不能使用..导入，这个如何处理
#
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)  #