# import printing_functions
#
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# printing_functions.print_models(unprinted_models, completed_models)
# printing_functions.show_print_models(completed_models)

##----------------------------------------------------------------------------------------------------------------------
# from printing_functions import print_models
# from printing_functions import show_print_models
#
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_models, completed_models)
# show_print_models(completed_models)

##======================================================================================================================
# from printing_functions import print_models as pm
# from printing_functions import show_print_models as spm
#
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# pm(unprinted_models, completed_models)
# spm(completed_models)

##——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# import printing_functions as pf
#
# unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# pf.print_models(unprinted_models, completed_models)
# pf.show_print_models(completed_models)

##-------————---------————-------------————----------————-----------————------------————-----------————----------————---

from printing_functions import*              ## 使用（*）运算符 可让Python导入所有  函数

unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_print_models(completed_models)