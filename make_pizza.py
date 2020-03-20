# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
"""这就是一种导入方法： 只需要编写一条 import语句 并在其中 指定 模块名，就可以在程序中使用该模块中的所有函数"""
#------------------------------------------------------------------------------------------------------------------------
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#========================================================================================================================

# from pizza import make_pizza as mp
#
# mp(16, 'pepperoni')
# mp(12, 'mushroom', 'green peppers', 'extra cheese')

# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

""" * 号可以导入模块中所有函数 """
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
