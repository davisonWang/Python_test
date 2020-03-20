import unittest
from name_function import get_formatted_name

class NameTextCase(unittest.TestCase):       # 创建了一个名为NameTextCase的类，用于包含一系列针对get_formatted_name的测试，
  #名字任取，继承unittest.TestCase类
    """测试name_function.py"""

    def test_first_last_name(self):
    #NamesTestCase 只包含一个方法，用于测试 get_formatted_name() 的一个方面。我们将这个方法命名为 test_first_last_name()
        """能够正确的处理 donald trump这样的姓名吗？"""
        formatted_name = get_formatted_name('donald', 'trump')        #调用要测试的函数，并存储要测试的返回值
        self.assertEqual(formatted_name, 'Donald Trump')          #我们调用unittest的方法assertEqual(),并向它传递formatted_name, 'Donald Trump'

    def test_middle_last_name(self):
        formatted_name = get_formatted_name('donald', 'trump', 'dick')
        self.assertEqual(formatted_name, 'Donald Dick Trump')

"""代码行 unittest.main() 让Python运行这个文件中的测试"""
unittest.main()