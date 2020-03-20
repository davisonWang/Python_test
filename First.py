### Coursr_One Hello world

# print("Hollo Python world!")
# #input(Welcome to Python world!)
# input("Welcome to Python world!")

### 变量 Course_two 尝试在代码中使用一个变量，添加一个名为message的变量，每一个变量都存储了一个值
###————与变量相关联的信息，在这里储存的值为文本“Hello Python Crash Course Reader”
# message="Hello Python Crash Course Reader"
# print(message)

### 且在程序中可随时修改变量的值，而Python将始终记录变量的最新值
# message="Hello Python crash course reader"
# print(message)
# message="Hello Python world!"
# print(message)

### 2.2.1 变量的命名和使用

# message_1 = "变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，列如，可将变量命名为message_1,但不能命名为1_message。"
# message_2 = "变量名不能包含空格，但可使用下划线来分隔其中的单词。列如，变量名greeting_message可行，但变量名greeting message会引发错误。"
# message_3 = "不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print(请参见附录A.4)。"
# message_4 = "变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。"
# message_5 = "慎用小写字母I和大写字母O，因为它们可能被人错看成数字1和0。"
# a = [message_1, message_2, message_3, message_4, message_5]
# for message in a:
#  print(message)

### String 大多数程序都定义并收集某种数据，然后使用它们来做些有意义的事情。
## Describe 字符串 就是一系列字符。在Python中，用引号括起来的都是字符串，其中的引号可以是引号，也可以是双引号。
# a = 'This is also a string.'
# b = "This is a string"
# print(a, b)

#### 这种灵活性能够在字符串中包含引号和撇号
# 'I told my friend, "Python is my favorite language."'
# "The language 'Python' is named after Monty Python, not the snake. "
# "One of Python's strengths is its diverse and supportive community."


### 2.3.1 使用方法修改字符串大小写
# name = "ada lovelace"
# print(name.title())        # 开头大写
# print(name.upper())        # 全大写
# print(name.lower())        # 全小写

### 2.3.2 合并字符串
##有时我们想将  不同的字符串  保存在  不同的变量 中，这种方法称作 拼接 ，通过拼接可使用储存在变量中的信息
##来创建完整的消息
# first_name = "Davison"
# last_name = "Wang"
# full_name = first_name + " " + last_name
# print(full_name)

# first_name = "ada"
# last_name = "Lovelace"
# full_name = first_name + " " + last_name
#
# print("Hello " + full_name.title() + "!")


# first_name = "davison"
# last_name = "wang"
# full_name = first_name + " " +last_name
# message = ("Hello " + full_name.title() +"!")
# print(message)


### 2.3.3 换行符\n 和 制表符\t

# print("Python")
# print("\tPython")
#
# n = "language"
# m = n.title()
# print(m + "\nPython, \nC, \nJavaScript")
#
# n = "language"
# m = n.title()
# print(m + "\n\tPython, \n\tC, \n\tJavaScript")


### Python 能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法 rstrip()。
# favorite_language = ' python '
# print(favorite_language)
#
# favorite_language.rstrip()           # 结尾
# print(favorite_language.rstrip())
#
# favorite_language.lstrip()           # 开头
# favorite_language = favorite_language.lstrip()
# print(favorite_language)
#
# favorite_language.strip()            # 开头和结尾
# favorite_language = favorite_language.strip()
# print(favorite_language)


### 2.3.5 使用字符串时避免语法错误
# message = "One of Python's strengths is its community."
# print(message)

## #message = 'One of Python's strengths is its community.'


### 2.4 Numbers
# 在终端会话中Python直接返回运算结果，Python使用两个 ** 号表示乘方运算（3 **2  9）

###2.4.2 浮点数 float

### 2.4.3 使用函数 Str() 避免类型错误
# age = 28
# message = "Happy " + str(age) + "th birthday !"
# #message = int("Happy ") + age + int("th birthday !")
# print(message)


### 动手试一试
### 2-8  数字 8 ： 编写 4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字 8 。为使用 print 语句来显示结果，务必将这些表达式用括号括起来，也
### 就是说，你应该编写 4 行类似于下面的代码：

# print(3+5)
# print(10-2)
# print(2*4)
# print(40/5)


#### Python 之禅
# import this
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

#### 3 列表
## 列表 由一系列按特定顺序排列的元素组成。在Python中，用 [] 来表示列表，并用逗号来分隔其中的元素
# bicycles = ['treck', 'cannondale', 'redline', 'specialized']
# print(bicycles)

### 3.1.1 访问列表元素
## 列表是有序集合， 因此要访问列表的任何元素，只需要将该元素的位置或索引告诉Python即可。
# bicycle = ["treck", 'cannondale', 'redline', 'specialized']
# print(bicycle[0].title())
# ### 3.1.2 索引从0而不是1开始，而通过-1，-2可依次倒取倒数第一和第二个结果
# print(bicycle[1].lower())
# print(bicycle[3].upper())
#
# print(bicycle[-1].lower())
# print(bicycle[-2].upper())
# message = "My first bicycle was " + bicycle[0].title() + "."
# print(message)

### 3.2 　修改、添加和删除元素
## 3.2.1 修改列表元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# motorcycles[0] = 'ducati'
# print(motorcycles)

## 3.2.2 在列表中添加新元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
#
# motorcycles = []
# motorcycles.append('suzuki')
# motorcycles.append('yamaha')
# motorcycles.append('honda')
# motorcycles.append('ducati')
# print(motorcycles)

## 2.在列表中插入元素
# motorcycles = ['ducati', 'suzuki', 'yamaha', 'honda']
# motorcycles.insert(0, 'nisang')
# print(motorcycles)
# motorcycles.insert(-1, 'freedom')
# print(motorcycles)
#
# ### 3.2.3 从列表中删除元素
# ## del 将值在列表中永久删除，[0]位置始终是以删除后的为准
# motorcycles = ['ducati', 'suzuki', 'yamaha', 'honda']
# del motorcycles[0]
# del motorcycles[0]
# del motorcycles[-1]
# print(motorcycles)
#
# ## 使用pop() 删除元素
# ## 方法pop() 可删除列表 末尾 的元素，并让你能够接着使用它。术语 弹出（pop）源自这两的类比：列表就像一个栈，
# ## ，而删除列表末尾的元素相当于弹出栈顶元素。
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
#
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycle = ['honda', 'yamaha', 'suzuki']
# last_motorcycle = motorcycle.pop()
# message = "The last motorcycle i owned was a " + last_motorcycle.upper() + "."
# print(message)

### 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法 remove().
## 假如要从列表motorcycles中删除'ducati' 。
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove("suzuki")
# print(motorcycles)
# motorcycles.remove('yamaha')
# print(motorcycles)

### 使用remove() 从列表中删除元素时，也可接着使用它的值。下面删除值'ducati'
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + ' is too expensive for me.')

### 3.3 　组织列表
## 在创建列表时元素的顺序往往是无法预测的，因为你并非总能控制用户提供数据的顺序，但经常需要以特定的顺序呈现信息
## 有时候，你希望保留列表元素最初的排列顺序，而有时候有需要调整排列顺序。Python提供了很多组织列表的方式，可根据情况选用
## 3.3.1 使用方法 sort() 队列表进行永久排序
## Python方法sort() 让你能够较为轻松的对列表进行排序，假设你有一个汽车列表，并想让列表中是汽车按照字母大小写排列，
## 这里为简化排列任务，假设列表中的所有值都是小写。
# ## sort()
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
#
# ## reverse = True反方向排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)
#
# ## 3.3.2 使用函数 sorted() 对列表进行临时排序
# ## 要保留列表元素原来的排列顺序， 同时以特定的顺序呈现他们，可使用函数 sorted()。可使用函数 sorted()。函数sorted()
# ## 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))
#
# print("Here is the original list again:")
# print(cars)
#
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()    #永久性地修改列表元素的排列顺序，但可随时恢复原来的排列顺序，为此只需要再次调用 reverse()即可。
# print(cars)
#
# cars.reverse()
# print(cars)
#
# ## 3.3.4 确定列表的长度
# ## 在Python 中使用len() 可快速获悉列表长度
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# len(cars)
# print(len(cars))
#

### 3.4 　使用列表时避免索引错误

#### 3.4 　使用列表时避免索引错误

# ### 4.1 遍历整个列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
#
# ### 4.1.2 在for 循环中执行更多的操作
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a trick! ")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
#
# print("Thank you everyone")
#
# message = "Hello, python world"
# print(message)

### 4.2.1 忘记缩进

### 4.3  创建数值列表
## 4.3.1 使用函数 range()
## Python 可以让你轻松生成一系列数字，例如，像下面这样使用函数 range() 来打印一系列的数字。
# for value in range(1, 5):
#     print(value)
#
# for value in range(1, 6):
#     print(value)

## 使用 range() 创建数字列表
## 要创建数字列表，可使用函数  list()  将 range() 的结果直接转换为列表。在前一节，我们打印了一系列数字。要将
## 这些数字转换为一个列表， 可使用 list():
# numbers = list(range(1, 6))
# print(numbers)
#
# ## 使用函数range()时，还可以指定步长。例如，下面的代码打印1~10以内的偶数：
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

## 使用函数 range() 几乎能够创建任何需要的数字集，例如，如何创建一个列表，其中包含前 10 个整数（即 1~10 ）的平方
# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#     print(squares)
#
# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
#     print(squares)

### 4.3.3 对数字列表执行简单的统计计算
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(digits)
# print(min(digits))
# print(max(digits))
# print(sum(digits))
#
# ### 4.3.4 列表解析
# squares = [value**2 for value in range(1, 11)]
# print(squares)

### 4.4 　使用列表的一部分
## 在第三章，你学习了如何访问单个列表元素。在本章中，你一直在学习如何处理列表的所有元素。你还可以处理列表的部分元素——Python称之为 切片
## 4.4.1 切片 与函数 range() 一样，Python 在到达你指定的第二个索引前面的元素后停止。要输出列表中的前三个元素，需要
## 指定索引 0~3，这将输出分别为0、1和2的元素。

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0: 3])
# print(players[1: 4])
#
# ## 如果你没有指定第一个索引Python 将自动从列表开头开始：
# print(players[: 4])
# print(players[2: ])
# print(players[-3: ])
#
# print("Here are the first three players on my team: ")
# for player in players[:3]:
# print(player.title())
#
# ## 4.4.3 复制列表
# ## 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始和终止索引([:]),使Python创建一个始于第一个元素
# ## 终于最后一个元素的切片，即复制整个列表。
# my_food = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_food[: ]
# print("My favorite foods are: ")
# print(my_food)
# print("\nMy friend favorite foods are: ")
# print(friend_food)
#
# my_food = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_food[: ]
# friend_food.append('ica cream')
# my_food.append('cannoli')
# print('My favorite foods are: ')
# print(my_food)
# print('\nMy friend favorite foods are: ')
# print(friend_food)

### 4.5 　元组
## 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表等至关重要。 然而，有时候你需要
## 创建一系列不可修改的元素，元组可以满足这种需求。
## 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)
#
# ## 4.5.3 修改元组变量
# ## 虽然不能修改元组的元素，但可以给存储的变量赋值。因此如果要修改前述矩阵的尺寸，可重新定义整个元组。
# dimensions = (200, 50)
# print("Original dimension: ")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400, 100)
# print("\nModified dimension: ")
# for dimension in dimensions:
#     print(dimension)

### 5.1 简单示例
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# ### 5.2 　条件测试
# ###     5.2.3 检查是否不相等
#
# ## 要判断两个值是否不相等， 可结合使用惊叹号和等号（!=），其中！表示 不
# requested_topping = 'mushroom'
# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')

## 5.2.4 　比较数字
# answer = 17
# if answer != 42:
#     print("That is not correct answer. Please try again!")

### 5.2.5 　检查多个条件  in

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

### 5.2.7 检查特定值是否不包含在列表中   not in
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
#
# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish!")
#
# game_active = True
# can_edit = False

# age = 19
# if age >= 18:
#     print("You are old enough to vote! ")
#     print("Have you registered to vote yet ？")

#### 5.3.2 if-else 语句
## if-else 语句块 类似于简单句的 if语句，但其中的else语句让你能够指定条件测试未通过时要执行的操作。
# age = 17
# if age >= 18:
#     print("You are old enough to vote !")
#     print("Have you registered to vote yet ?")
#
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

###   5.3.3 if-elif-else 结构
## 经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构。Python只执行if-elif-else 结构中的一个代码块，它依次检查
## 每个条件测试，直到遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试
# age = 12
#
# if age < 4:
#     print("You admission cost is $0.")
#
# elif age < 18:
#     print("You admission cost is $5.")
#
# else:
#     print("You admission cost is $10.")

### 5.3.6 测试多个条件
# requested_topping = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_topping:
#     print("Adding mushrooms. ")
# if 'pepperoni' in requested_topping:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_topping:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

# requested_topping = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_topping:
#     print("Adding mushrooms. ")
# elif 'pepperoni' in requested_topping:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_topping:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

### 5.4 使用 if 语句处理列表
### 5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza! ")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now. ")

    else:
        print("Adding" + requested_topping + ". ")

print("\nFinished making your pizza! ")

### 5.4.2 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")

else:
    print("Are you sure you want a plain pizza?")

#### 5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

###  5 　设置 if 语句的格式

### 第六章 字典
### 6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

### 6.2 使用字典
## 在python中， 字典 是一系列 键——值 对。每个键 都与一个 值 相关联，你可以使用键来访问与之相关的值。与键相关联的值
## 可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的 值。
## 在Python 中，字典用放在 花括号{}中的 一系列 键——值 对表示，

### 键——值 对是两个相关联的值。指定键时，Python将返回与知悉相关联的值。键和值之间用 冒号 分隔， 而 键——值
## 对之间用 逗号 分隔。在字典中，你先存储多少个 键——值 对都可以。 最简单的字典只有一个 键——值 对
alien_0 = {'color': 'green'}

### 6.2.1 访问字典中的值
## —— 要获取与 键 相关联的 值，可依次指定 字典名 和 放在 方括号内的 键
alien_0 = {'color': 'green'}
print(alien_0['color'])

## —— 字典中可包含任意数量的 键——值 对。
alien_0 = {'color': 'green', 'point': 5}
new_points = alien_0['point']
print("You just earned " + str(new_points) + " points!")

### 6.2.2 添加 键——值 对
## 字典 是一种动态结构，可随时在其中添加 键——值 对。要添加 键——值 对，可依次指定字典名、用方括号括起的键和相关联的值
##下面在字典alien_0 中添加两项信息：外星人的x坐标和y坐标，让我们能够在屏幕的特定位置显示该外星人。我们将这个外星人放在
##屏幕左边缘，且离屏幕上边缘25像素的地方。由于屏幕坐标系的原点通常为左上角，因此要将该外星人放在屏幕左边缘，可将x坐标设置
## 为0；要将该外星人放在离屏幕顶部25像素的地方，可将y坐标设置为25，
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'yellow'
alien_0['points'] = '6'
print(alien_0)

## 使用字典存储用户提供的数据或在编写能自动生成大量 键——值 对的代码时，通常都需要先定义一个空字典。

### 6.2.4 修改字典中的值
### 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关的新值。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print(" The alien is " + alien_0['color'] +".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

## 向右移动外星人
## 根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increase = 1

elif alien_0['speed'] == 'medium':
    x_increase = 2

else:
    x_increase = 3

## 新位置等于老位置加上增重
alien_0['x_position'] = alien_0['x_position'] + x_increase
print("New x_pisition: " + str(alien_0['x_position']))

### 6.2.5 删除 键——值 对
### 对于字典中不再需要是信息，可使用del语句将相应的 键——值 对彻底删除。使用del语句时，必须制定字典名和要删除的键
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

## 6.2.6 由类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarach's favorite language is: " + favorite_language['sarah'].title() + ".")

### 6.3 　遍历字典
### 一个Python字典可能包含几个键——值对，也可能包含数百万个键——值对。鉴于字典可能包含大量的数据，Python支持对字典遍历。
### 字典可用于各种方式存储信息，因此有多种遍历字典的方式： 可遍历字典的所有键——值对、键或值。

 ### 6.3.1 　遍历所有的键 — 值对
 user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
        }
 for key, value in user_0.items():
     print('\nKey: ' + key)
     print('Value: ' + value)

### 要编写用于遍历字典的for循环，可声明两个变量，用于存储 键——值 对中的键和值。对于这两个变量，可使用任何名称。
###  使用简单的代码也完全可行。
for k, v in user_0.items():

favorite_language = {'jen': 'python',
                     'sarah': 'c',
                     'edward': 'ruby',
                     'phil': 'python',
                     }

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

### 6.3.2  遍历字典中的所有键
for name in favorite_language.keys():       ### 在不需要使用字典中的值时，方法 keys() 很有用。
    print(name.title())

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_language[name].title() + "!")

### 你还可以使用key() 确定某人是否接受了调查。下面的代码确定Erin 是否接受了调查：
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_language.keys():
    print('Erin, please take our poll !')

### 6.3.3 　按顺序遍历字典中的所有键

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'tom' not in favorite_language.keys():
    print("I will be a winner")

for name in sorted(favorite_language.keys()):
    print(name.title() + " thank you for taking the poll!")

### 6.3.4 遍历字典中所有的值
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

#### 这种做法提取字典中所有的值，但没有考虑还否重复。 涉及的值很少时，这也许不是问题， 但如果被调查者很多，最终的列表
#### 可能包含大量的重复项。 为剔除 重复项， 可使用  集合（set）。 集合 类似于列表，但是  美国元素都必须是独一无二的：
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have benn mentioned: ")
for value in set(favorite_language.values()):
    print(value.title())

### 6.4 　嵌套
### 有时候，需要将一系列字典存储在列表中， 或将 列表 作为值存储在 字典 中，这称为 嵌套。你可以在列表中 嵌套 字典、
### 在 字典 中 嵌套 列表甚至在 字典 中嵌套 字典。

### 6.4.1 字典列表
## 字典alien_0 包含一个外星人的各种信息，但无法储存第二个外星人的信息， 嵌套    ：

alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'green', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

### 更符合现实的情况是，外星人不止3个，且每个外星人都是代码自动生成的。在下面的实例中，我们使用 range()
### 生成了 30个 外星人：

# 创建一个用于存储外星人的空列表

aliens = []
#创建30个绿 外星人
for alien_number in range(30):
## range() 返回一系列数字，其唯一的用途是告诉 Python 我们要重复这个循环多少次。每次执行这个循环时，都创建一个外星人，并将其附加到列表aliens末尾。
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
    print("...")

print("Total number of aliens: " + str(len(aliens)))

## 创建一个用于存储外星人的空列表
aliens = []
## 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0: 3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[0: 5]:
    print(alien)

print("...")

### 在字典中存储列表
### 6.4.2 在字典中存储列表
### 有时候需要将列表存储在字典中，而不是将字典存储在列表中
### 在下面的示例中，存储了披萨的两方面信息：外皮类型和配料列表。其中的配料列表是有个与 键'toppings'相关联的值。
### 要访问该列表，我们使用字典名 和 键'toppings'，就像访问字典中的其它值一样。这将返回一个配料列表：

## 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

## 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

### 每当需要在字典中将一个 键 关联到 多个 值 时，都可以在字典中嵌套一个列表，与每个被调查者相关联的都是一个语言
### 列表， 而不是一种语言；因此，在遍历该字典的for循环中，我们需要再使用一个for循环来遍历与被调查者相关联的语言列表：
favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
    }

for name, languages in favorite_language.items():
    if len(languages) == 2:
        print("\n" + name.title() + "'s favorite language are: ")
        for language in languages:
            print("\t" + language.title())

    else:
        print("\nSarah's favorite language is C")

### 6.4.3 　在字典中存储字典
user = {'aeinstein': {'first': 'albert',
                      'last': 'einstein',
                      'location': 'princeton',
                      },

        'mcurie':{'first': 'marie',
                  'last': 'curie',
                  'location': 'paris',
                  },
        }

for username, user_info in user.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\nFull name: " + full_name.title())
    print("\tLocation: " + location.title())

##### 函数input()的工作原理
### 函数input() 让程序暂停运行，等待输入一些文本

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

### 7.1.1 编写清晰度程序
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name ?"

name = input(prompt)
print("\nHello, " + name + "!")

###   7.1.2 使用 int() 来获取数值输入
### 使用函数 input() 时，Python将用户输入解读为字符串。
height = input('How tall are you?, in inches ?')
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

### 7.1.3 求模运算符
### 处理数值信息时， 求模运算符 （%）是一个有用的工具，他将 两个数字相处并返回余数：
print(4 % 3)
### 求模运算符 不会之处一个数是另一个数的多少倍， 而只指出 余数 是多少
### 如果一个数可被另一个数整除，余数就为 0 ，因此求模运算符将返回0，你可以利用这一点来判断一个数是 奇数 还是 偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even. ")
else:
    print("\nThe number " + str(number) + " is odd.")

### 7.2 　while 循环简介
### for 循环用于针对集合中的每个元素都一个代码块， 而while循环不断地运行，直到指定的条件不满足为止。
### 7.2.1 使用while 循环
## 可以使用while 循环来数数，while循环从1到5：
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

### 7.2.2 让用户选择何时退出
prompt = "\nTell me somrthing, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

### 7.2.3 使用标志
## 在要求很多条件都满足才能继续运行的程序中，可定义一个 变量，用于判断整个程序是否处于 活动状态。这个变量
## 被称为 标志，充当了程序的交通信号灯，你可让程序在 标注 为 True时继续运行， 并在任何事件导致标志的值为
## False时让程序停止运行。这样，在while语句中就只检查一个条件——标志 的值当前是否为 True, 并将所有测试（
## 是否发生了应将标志设置为 False 的事件）都放在其它地方，

## 接下来在程序中添加一个标志。 我们把这个标志命名为 active
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

### 7.2.4使用 break 退出循环
### 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何， 可使用 break 语句。 break语句用于
### 控制程序的流程，可使用它来控制那些代码将执行 ，哪些不执行，
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to "+ city.title() + "! ")

### 以 while True 打头的循环将不断运行，直到 break

### 7.2.5 在循环中使用 continue
### 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用 continue 语句，它不像 break 语句那样不再
### 执行余下的代码并退出整个循环。 从 1 数到 10，但只打印其中偶数的循环：
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue          # 忽略接下来的程序，返回程序开头

    print(current_number)

### 7.2.6 避免无限循环
### 每个 while循环 都必须有停止运行的途径，这样才不会每晚没了地执行下去。
x = 1
while x < 5:
    print(x)
    x += 1

x = 1
while x <= 5:
    print(x)

### 使用 while 循环来处理列表和字典
### 7.3.1 　在列表之间移动元素
## 假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
## 一个办法是使用 while 循环， 在验证用户的同时将其中从未验证用户列表中提取出来，再将其加入到另一个已验证用户
## 列表中。

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

###   7.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

### 7.3.3 使用用户输入来填充字典
## 可使用 while循环 提示用户输入任意数量的信息。
responses = {}

## 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
## 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")

    responses[name] = response

    #看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n----Poll Results----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

## 在本章中，你学习了：如何在程序中使用input() 来让用户提供信息：如何处理文本和数字的输入，以及如何使用while循环让程序按用户的要求不断运行：
## 多控制while循环流程的方式：设置活动标志、使用break语句以及使用continue语句；如何使用while循环在列表之间移动元素，以及如何从列表中删除所有包含特定值的元素
## .pop 或 remove(' ') ，如何结合使用while循环和字典。

### 第八章 函数
## 你将学习函数。函数让你能够将程序分成多个很小的部分，其中每个部分都负责完成一项具体任务。你可以根据需要调用同一个函数任意次，
## 还可以将函数存储在独立的文件中。使你的程序 效率更高。

### 在本章中，你将学习编写 函数。函数是带名字的代码块，用于完成具体工作。
### 8.1 定义函数

def greet_user():
    """ 显示简单的问候语 """     # 文档字符串的注释，文档字符串用三引号括起
    print("Hollo !")
greet_user()


### 用关键词 def 来告诉Python你要定义一个函数。 这是--函数定义，向Python指出函数名，还可能在括号中指出
###函数为完成其任务需要什么样的信息。函数名为greet_user(), 它不需要任何信息就能完成其工作，因此括号是空的
###（即便如此，括号也必不可少）。最后定义以冒号结尾。
###-------------------------------------------------------------------------------------------------------------------------------------
### 调用函数 让Python执行函数的代码。要 调用 函数，由于这个函数不需要任何信息，因此 调用 他时只需要输入greet_user()即可。

###    8.1.1    向函数传递信息
### 将用户的名字用作 抬头。 可在函数定义 def greet_user() 的括号内添加 username。通过在这里添加 username,就可让函数接受你给
### username 指定的任何值。现在，这个函数要求你调用它时给 username 指定一个值。 调用 greet_user()时， 可将一个名字传递给它。

def greet_user(username):
    """ 显示问候语"""
    print("Hello, " + username.title() + "! ")

greet_user('trump')

### username 是一个形参，'Trump' 是一个实参

###     8.2 传递实参
###  鉴于函数定义中可能包含多个  形参  ，因此函数调用中也可能包含  多个实参。向函数传递实参的方式很多，可使用  位置实参，这要求 实参
###  的顺序与 形参的顺序相同；也可使用 关键字实参 ，其中每个实参都由  变量名 和 值 组成；还可使用 列表 和 字典。

###  8.2.1  位置实参
### 在调用函数时，Python必须将函数调用中的每个 实参 都关联到函数定义中的一个 形参。为此，最简单的关联方式是基于实参的顺序。这种方式
### 被称为  位置实参 。。。

## ---------------------------------------------------------------------------------------------------------------------

def describe_pet(animal_type, pets_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pets_name.title() + ".")

describe_pet('hamster', 'harry')
"""多次调用"""
describe_pet('dog', 'willie')
describe_pet('cat','tom')

##  2. 位置实参的顺序很重要
### 8.2.2 关键字实参
### 关键字实参 是传递给函数的名称—— 值对。 你直接在实参中将 名称 和 值 关联起来，
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name = 'jerry', animal_type = 'hamster')


###     8.2.3 默认值
###   编写函数时，可给每个形参指定  默认值。在调用函数中给形参提供了实参 时,python将使用指定的实参值；否则使用 形参的默认值。 因此，
###   给形参 指定 默认值后，可在函数调用中 省略相应的 实参。 使用默认值可简化 函数调用。
def describe_animal(pet_name, animal_type = 'dog'):
    """指定形参 默认值"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_animal(pet_name = 'willie')
# ### 由于animal_type指定了默认值，无需通过 实参 来指定动物类型，因此在函数调用中只包含一个 实参——然而Python仍然将这个实参视为 位置实
# ### 参，这个实参将关联到函数定义中的  第一个 形参。
# """指定实参以后忽略默认‘dog’"""
# describe_animal(pet_name= 'jerry', animal_type='hamster')
#
# ### 8.2.4 等效的函数调用
# ### 鉴于可混合使用位置实参、关键字 实参和默认值，通常有多种等效的函数调用方式。
# ### 基于这种定义，在任何情况下都必须给pet_name 提供实参；指定该实参可使用 位置方式，也可使用 关键字方式
describe_animal('willie')
describe_animal(pet_name='willie')

describe_animal('jarry', 'hamster')
describe_animal(pet_name='jerry', animal_type='hamster')
describe_animal(animal_type='hamster', pet_name='jerry')

### 8.3 　返回值
##函数并非总是直接显示输出，相反，它可以处理一些数据，并返回 一个或一组 值 。函数返回的值被称为 返回值。在函数中，可使用
## return 语句将 值 返回到调用函数的代码行。 返回值让你能够将程序的大部分繁重工作移到函数中去完成，
### 8.3.1  返回简单值

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

###---------------------------------------------------------------------------------------------------------------------
"""Python将非空字符串解读为True"""

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name :     # 判断是否有值输入，有为True。没有的话 middle_name=' '为 空，False, 执行 else命令。
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()

message = get_formatted_name('jimi', 'carter')
print(message)

message = get_formatted_name('john', 'lee', 'hooker')
print(message)

### 8.3.3 返回字典
### 函数可返回任何类型的值，包括 列表 和 字典 等较复杂的数据结构。
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi', 'carter')
print(musician)

##--------------------------------------------------------------------------------------------------------------------------------------------
def build_person(first_name, last_name, age=" "):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name,}
    if age:
        person['age'] = age
        return person

message = build_person('Mike', 'Pomepo', 56)
print(message)

# ###   8.3.4结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
# while True:
#     print("\nPlease tell your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

##------------------------------------------------------------------------------------------------------
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    users = get_formatted_name(f_name, l_name)
    print("\nHello " + users + "!")

###---------------------------------------------------------------------------------------------------------------------
### 8.4 　传递列表
### 你经常发现，向函数传递列表很有用，这种列表可能包含 名字、数字、更复杂的对象（字典）。将列表传递给函数后，函数就能直接访问其内容。
## 接下来使用函数来提高处理列表的效率。

def greet_users(names):
    """传递列表，即向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

### ====================================================================================================================
###    8.4.1 在函数中修改列表
###    将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。
unprinted_designs = ['iphone case', 'robot case', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_printed = unprinted_designs.pop()
    print("Printing models include about: " + current_printed)
    completed_models.append(current_printed)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

"""-----------------------------------------------------------------------------------------------"""
def print_models(unprinted_model, completed_model):
    while unprinted_model:
        current_model = unprinted_model.pop()
        completed_model.append(current_model)
        print('Printing models include about: ' + current_model)
        """return current_model"""

def show_peinting(completed_model):
    print("\nThe following models have been printed:")
    for completed_models in completed_model:
        print(completed_models)
"""只要看看主程序更容易理解，只要看主程序，你就知道这个程序的功能容易看清的多"""
unprinted_model = ['iphone case', 'robot case', 'dodecahedron']
completed_model = []

print_models(unprinted_model[:], completed_model)
show_peinting(completed_model[:])

"""这个程序还演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个显示打印好的模型；这优于使用一个
函数来完成两项工作。编写函数时，如果你发现它执行的任务太多，请尝试将这些代码划分到两个函数中。别忘了，总是可以在一个函数中调用另一个函
数，这有助于将复杂的任务划分成一系列的步骤。"""

### --------------------------------------------------------------------------------------------------------------------
###     8.4.2  禁止函数修改列表
"""通过切片法[:]创建列表的副本。在调用中，如果过不想清空未打印的设计列表，function_name(list_name[:]) """

print_models(unprinted_model[:], completed_model)
"""这样函数 print_model() 依然能够完成其工作，因此它获得了所有未打印的设计的名称，但它使用的是 列表 unprinted_model的副本，而不是
列表 本身 。 但是，虽然向函数传递列表的副本可保留原始的内容，但除非有充分的理由需要传递副本, 否则还是应该建原始列表传递给函数，因为让
函数使用现成列表可避免花时间和内存创建副本，从而提高效率"""

###    8.5 　传递任意数量的实参
"""有时候，你预先不知道函数需要接受多少个 实参 ，好在Python允许函数从调用语句中收集任意数量的  实参。"""

"""例如，来看一个制作披萨的函数，他需要接受很多配料，下面的函数只有一个形参 *toppings ,但不管调用语句中提供了
多少实参，这个 形参 都将它们统统收入囊中："""

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

"""------------------------------------------------------------------------------------------------------------------"""
## 形参名 *toppings 中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。

def make_pizza(*toppings):
    """概要制作的比萨"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
"""不管收到的实参是多少，这个语法都管用"""
make_pizza('pepperoni')
make_pizza('mushroon', 'green peppers', 'extra cheese')

###    8.5.1  结合使用位置实参和任意数量实参
###  如果要让函数接受不同类型的实参，必须在函数定义中将 接纳任意数量 实参 的 形参 放在最后。
###  Python先匹配  位置实参   和   关键字实参，在将  余下的实参  都收集到  最后一个形参中。

"""如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在 实参 *toppings 的前面 """
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

## 基于上述定义，Python将收到的第一个值存储在 形参size中，并将其它的所有值都 存储在 元组toppings中。在函数调用中，
## 首先指定表示  披萨尺寸size的实参，然后根据需要指定  任意数量  的配料。

##======================================================================================================================
##  8.5.2 使用  任意数量   的  关键字实参
"""有时候需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息，在这种情况下，可将函数编写为可以接受任意数量的——键--值对
调用语句提供了多少就接受多少"""

def bulid_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_info = bulid_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_info)

### 函数build_profile() 的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称——值对。
### 形参 **user_info 中的 两个星号 让python 创建一个名为 user_info的 空字典，并将收到的所有名称——值对 都
### 封装到这个字典中。在这个函数中 可以像其它字典那样 访问user_info中的名称—— 值对。
"""在 build_profile() 的函数体内，我们创建了一个名为 profile的空字典，用于存储用户简介。我们遍历字典user_info
中的 键——值对，并将每个 键——值对 都加入到字典 profile中。最后，我们将字典profile 返回 给  函数调用行，我们
调用build_peofile(), 向它传递（'albert'）、姓（'einstein'）和 两个键——值对（location='princetion' 和
field='physics'）并将返回的profile存储在变量user_profile中，在打印这个变量： """

## 编写函数时，你可以混合使用各种方式 位置实参、关键字实参 和 任意数量的实参。

###  8.6   将函数存储在模块中
## 函数的有点之一是： 使用它们可将  代码块  和  主程序  分离。通过给函数指定描述性名称，可让主程序容易理解的多，
## 还可以更进一步， 将函数存储在被称为  模块的 独立文件中，再将模块  导入到主程序中。import语句允许在当前运行的
## 程序文件中使用模块中的代码。

## 8.6.1 导入整个模块
import pizza
pizza.make_pizza(16, 'pepperoni')

###    8.6.2 导入特定的函数
"""语法如下"""
from module_name import function_name

"""通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数："""
from module_name import function_0, function_1, function_2

###     8.6.3  使用 as 给函数指定别名
"""如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的  别名—— 函数的另一个名称，类似于外号。
要给函数指定这种特殊外号，需要在导入它时这样做。 """
### 下面给函数make_pizza() 指定别名 mp()。这是在import语句中使用make_pizza as mp 实现的，

from module_name import function_name as fn

"""上面的import语句将函数make_pizza() 重命名为mp()；在这个程序中，每当需要调用make_pizza()时，都可简写为mp(),而Python将运行
make_pizza() 中的代码， 这可避免也这个程序可能包含的函数make_pizza()混淆。"""

###     8.6.4 使用as给模块指定别名
###   你还可以给模块指定 别名。 通过给模块指定简短的别名（如给模块pizza 指定别名 p）,让你能够更轻松地调用模块中的函数。
###   相比于pizza.make_pizza(), p.make_pizza() 更为简洁：
import module_name as mn

### 8.6.5   导入模块中的所有函数
"""使用（*）运算符可让Python 导入模块中所有的函数"""

###      8.7  函数编写指南
""" 1. 编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中  使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么
给模块命名时也应遵守上述约定。"""

""" 2. 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其它程序员只需要阅读
文档字符串的描述就能够使用它：他们完全可以相信代码 如描述的那样运行； 只要知道函数的名称、需要的实参以及 返回值 的类型，就能在自己
的程序中使用它"""

"""给形参指定默认值时，等号两边不要有  空格 """
def function_name(parameter_0, parameter_1='default value'):

"""对于函数调用中的关键字实参，也应遵循 以上约定"""
function_name(value_0, parameter_1='value')

"""PEP 8(https://www.python.org/dev/peps/pep-0008/) 建议代码行的长度不要 超过79字符，这样只要编辑器窗口适中，就能看到整行代码。
如果形参很多，导致 函数 定义的长度超过了 79字符 ，可在函数定义中输入 左括号 后按回车，并在下一行按 两次 Tab键， 从而
将形参列表和只缩进一层的函数体区分开来。"""

def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body ...

"""如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样就更容易知道 前一个函数 在什么 地方结束 ，下一个函数 从什么地方开始"""

"""所有的 import语句 都应放在文件开头，唯一例外的情况是，在文件开头使用了 注释 来描述整个程序。"""

## 你将学习编写类。类将函数和数据整洁地封装起来，让你能够 灵活 而 高效 的使用它们。

###     9 章. 类
###  9.1 　创建和使用类
## 面向对象编程 是最有效的软件编写方法之一。在面向对象编程中，你 编写表现 现实世界中的事物 和 情景 的类，并基于这些类来创建 对象。
## 编写类时，你定义一大类对象都有的通用行为。基于 类 创建 对象时，每个对象都具备这种 通用行为，然后可根据需要赋予每个对象独特的个性。
## 使用面向对象编程可模拟现实情境，

## 根据类来创建 对象 被称为 实例化

##  9.1.1   创建Dog类


## 我们定义了一个名为 Dog 的类，在Python中首字母大写的名称指的是 类，这个类定义中的括号是空的，因此我们要从
## 空白创建这个类
# 1. 方法 _init_()
"""类中的函数称为 方法 ，方法_init_()定义成了包含三个实参：self、name和age，在这个方法的定义中
形参self必不可少，还必须位于其它形参前面。 为何必须在方法定义中包含形参self呢？ 因为Python调用这个
_init_()方法来创建Dog实例时，将自动转入实参self.每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用
，让实例能够访问 类中 的属性和方法。"""

###    9.2  使用 类 和 实例
###     9.2.1 Car 类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回简介的描述性信息"""
        long_name = str(self.year) + ' '+ self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


###     9.2.2 给属性指定默认值
###     类中的每个属性都必须 有初始值，哪怕 这个值是 0 或 空字符串。在有些情况下，如设置 默认值 时，在方法
# __init__()内指定这种 初始值 是可行的；如果你对某个属性这样做了，就无需包含为它提供 初始值 的形参。
class Car():

    def __init__(self, name, model, year):
        """初始化汽车的属性"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0
        """类中的每个属性都必须 有促使值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，
        在方法__init__()内指定这种 初始值 是可行的；如果你对某个属性这样做了，就无需包含为它提
        供 初始值 的形参。"""

    def get_descriptive(self):
        full_name = self.name + " " + self.model + " " + str(self.year)
        return full_name.title()

    def read_odometer(self):
        """打印一条指出汽车历程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())
my_new_car.read_odometer()

###     出售时里程表 读数位0的汽车并不多，因此我们需要一个修改该属性的值的途径。
###     9.2.3   修改属性的值
##  可以以三种不同的方式修改属性的值： 直接通过实例进行修改；通过方法进行设置；
##  通过方法进行递增（增加特定的值）。

"""1.  直接修改属性的值 """

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

"""2. 通过方法修改属性的值"""
class Car():

     def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0

     def get_descriptive_name(self):
         long_name = self.make + " " + self.model + " " + str(self.year) + "."
         return long_name.title()

     def read_odometer(self):
         print("The car has " + str(self.odometer_reading) + " miles on it.")

     def update_odometer(self, mileage):
         if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
         else:
             print("You can't roll back an odometer!")
     #    self.odometer_reading = mileage

my_new_car = Car('BMW', 'X7', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(27)       # mileage = 26

my_new_car.update_odometer(13)

my_new_car.read_odometer()

""" 3.   通过方法对属性的值进行递增. """
##  有时候需要将属性值 递增特定的量， 而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间
##  增加了100 英里的里程。

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.make + " " + self.model + " " + str(self.year) + "."
        return long_name.title()

    def read_odometer(self):
        print("The car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    #    self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car('BMW', 'X7', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)  # mileage = 23500
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

###     9.3 继承
"""
编写 类 时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用 继承。一个类 继承 另一个类时，
它将 自动获得 另一个类的所有属性和方法；原有的 类 称为 父类，而 新类 称为 子类。子类 继承了 其父类的所有属性和方法，
，同时还可以定义自己的 属性 和 方法。
"""
###    9.3.1   子类的方法 __init__()
##  创建子类的实例时，Python首先需要完成的任务是给 父类的所有属性赋值。为此，子类的方法__init__() 需要父类施以援手。

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading():
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer !")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#
# my_tesla = ElectricCar('tesla', 'model s', 2020)
# print(my_tesla.get_descriptive_name())

"""
super().__init__ 是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar 的父类的
方法__init__(), 让 ElectricCar实例包含父类的所欲属性。父类 也称为超类(superclass)，名称super因此而得名。
"""

###    9.3.2 Python 2.7中的继承
##     函数 super() 需要两个 实参：子类名和对象 self。

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)

###    9.3.3 给子类定义属性和方法
# 让一个类继续继承另一个类后，可添加区分子类和父类所需的新属性和方法。

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.batter_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.batter_size) + "-kWh battery. ")

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

###     9.3.4   重写父类的方法
"""
对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的
方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个 父类方法，而只关注你在子类中定义的相
应方法
"""
    def ElectricCar(Car):

        def fill_gas_tank():
            """电动汽车没有油箱"""
            print("This car doesn't need a gas tank!")       ###   在ElectricCar(Car)中重新定义

###   9.3.5 将实例用作属性
"""使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，
可能需要将类的一部分作为一个 独立的类 提取出来。你可以将 大型类拆分成多个 协同工作 的 小类。"""

## 我们可将这些 属性 和 方法 提取出来，放到另一个，名为 Battery的 类中，并将一个 Battery实例用作ElectricCar类
# 的一个属性：

class Car():

    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading():
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer !")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery. ")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()

###     9.4 　导入类

"""
随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦是如此。为遵循Python的总体理念，应让文件尽可能
整洁。为在这方面提供帮助，Python允许你将类存储在模块中，然后在主程序中导入所需的模块。
"""
###     9.4.1 　导入单个类
"""
下面来创建一个包含 Car类的 模块。将Car类 存储在一个名为car.py的模块中，使用该模块的程序都必须使用更具体的文件名，
如 my_car.py。下面是模块car.py,其中包含Car类的代码：
"""
##  创建 car.py

###     9.4.2  在一个模块中存储  多个类
"""虽然同一个模块中的类之间应存在某些相关性，但可根据需要在一个模块中存储任意数量的类。类Battery
和ElectricCar都可帮助模拟汽车"""

## 现在可以新建一个名为my_electric_car.py 的文件

###     9.4.3   从一个 模块中 导入 多个类
"""
可根据需要在程序文件中导入任意数量的类。如果我们要在同一个程序中创建 普通汽车 和 电动汽车
需要导入 Car 和 ElectricCar
"""

###     9.4.4   导入整个模块
##     你还可以导入整个模块，再使用 句点表示法 访问需要的类。这种导入方法很简单，代码也易于阅读。由于创建类实例
#     的代码都包含 模块名，因此不会与当前文件使用的任何名称 发生冲突。


###     9.4.5   导入模块中的所有类

from module_name import *

###     9.4.6   在一个模块中导入另一个模块
"""
有时候，需要将类分隔到多个模块中，以免模块太大，或在同一个模块中存储 不相关的类。将 类 存储在多个模块中时，你
可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。
"""

###     9.4.7  自定义工作流程
"""
正如你看到的，在组织大型项目的代码方面，Python提供了很多选项。熟悉所有这些选项很重要，这样你才能确定那种项目组织
方式是最佳的，并能理解别人开发的项目。 一开始应让代码结构尽可能的简单。先尽可能在一个文件中完成所有的工作，确定
一切都能正确运行后，在将类移到独立的模块中。 如果你喜欢 模块 和 文件 的交互方式，可在项目开始时就尝试将  类  
存储到  模块中。 先找出让你能够 编写出 可行代码的方式，再尝试让代码 更为 组织有序。
"""

###    9.5  Python 标准库
"""Python标准库 是一组模块，安装的Python都包含它。 可以开始使用其它程序员编写好的模块了。可使用标准库中的
任何函数和类，为此 只需要在程序开头包含一条简单的 import语句。 

字典让你能够将信息关联起来，但它们不记录你添加 键——值对 的顺序。要创建字典并记录其中的 键——值对 的添加顺序，
可使用模块collections 中的 OrderedDict类。 
"""

###   9-15 Python Module of the Week  ：要了解 Python 标准库，一个很不错的资源是网站
###     Python Module of the Week 。请访问 http://pymotw.com/  并查看其中的目录，在其中找一个你感兴趣的模块进行探索


###    第 10 章   文件和异常
"""，你将学习处理文件，让程序能够快速地分析大量的数据；你将学习错误处理，避免程序在面对意外情形时崩溃；你将学习 异常, 
它们是 Python 创建的特殊对象，用于管理程序运行时出现的错误；你还将学习模块 json ，
它让你能够保存用户数据，以免在程序停止运行后丢失。
"""
"""
学习处理文件和保存数据可让你的程序使用起来更容易：用户将能够选择输入什么样的数据，以及在什么时候输入；用户使用你
的程序做一些工作后，可将程序关闭，以后再接着往下做。学习处理异常可帮助你应对文件不存在的情形，以及处理其他可
能导致程序崩溃的问题。这让你的程序在面对错误的数据时更健壮—— 不管这些错误数据源自无意的错误，还是源于破坏
程序的恶意企图。你在本章学习的技能可提高 程序的 适用性、可用性 和 稳定性。
"""

###    10.1 从文件中读取数据
"""文本文件可存储的数据量 多得难以置信：天气数据、交通数据、社会经济数据、文学作品等。没当需要分析或修改存储在
文件中的信息时，读取文件都很有用，的数据分析应用程序来说尤其如此。

例如，你可以编写一个这样的程序：读取一个文本文件的内容，重新设置这些数据的格式并将其写入文件，让浏览器能够
显示这些内容。

要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，
也可以以每次一行的方式逐步读取
"""

###    10.1.1   读取整个文件
##  也可从本书的配套网站（ https://www.nostarch.com/pythoncrashcourse/  ）下载该文件

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


###    10.1.2   文件路径
"""在文件路径中使用 反斜杠(\) 而不是斜杠(/)"""
"""相对路径"""
with open('text_files\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

##---------------------------------------------------------------------------------------------------------------------

"""绝对文件路径，用 斜杠 分隔 路径"""
file_path = 'D:/Program Files/JetBrains/PyCharm Community Edition 2019.3.3/jbr/bin/Python_test/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

###     10.1.3 逐行读取
"""
读取文件时，常常需要检查其中的每一行：你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
列如，你可能要遍历一个包含天气数据的文件，并使用天气描述中包含 字样sunny的行。在新闻报道中会查找包含标签
<headline>的行，并按特定格式设置它。 
"""


filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

###     10.1.4  创建一个包含文件各行内容的列表
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


###    10.1.5   使用文件的内容
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

line_string = ' '
for line in lines:
    line_string += line.rstrip()

print(line_string)
print(len(line_string))

"""在变量中pi_string存储的字符串中，包含原来位于每行左边的空格，为删除这些空格,可使用 strip() 而不是 rstrip()"""

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
 #   print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


"""读取文本文件时，Python将其中的所有文本都解读为 字符串。如果你读取的是数字，并要将其作为数值 使用，就必须使用
函数 int() 将其转换为整数，或使用 函数float()将其转换为 浮点数 。"""

###     10.1.6  包含一百万位的大型文件
filename = 'text_files/pi_digits_2.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_million_string = ' '
for line in lines:
    pi_million_string += line.strip()

print(pi_million_string[:56] + '...')
print(len(pi_million_string))


###     10.1.7  圆周率中包括你的生日吗
filename = 'text_files/pi_digits_2.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_million_string = ' '
for line in lines:
    pi_million_string += line.strip()

while True:
    birthday = input("Please enter your birthday, in the from mmddyy: ")
    if birthday == 'q':
        break

    else:
        if birthday in pi_million_string:
            print("Celebrate! your birthday appears in the first million digits of Pi.")

        elif birthday not in pi_million_string:
            print("Your birthday not appears in the first million digits of Pi.")


###    10.2 写入文件
"""
要将文本写入文件，你在调用open() 时需要提供另一个实参，告诉Python 你要写入打开的文件。为明白其中的工作
原理，我们来将一条简单的消息存储到文件中，而不是将其打印到屏幕上：
"""

"""创建 programming.txt 文档"""
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

""" 调用 open()时提供了两个 实参。第一个实参也是要打开的文件的名称；第二个实参('w')告诉Python,我们要以写入
模式 打开这个文件。打开文件时，可指定 读取模式('r')、 写入模式('w')、附加模式('a') 或让你能够读取和写入文件的模式
('r+')。 如果你忽略了 模式实参, Python将以默认的只读模式打开文件

如果你要写入的文件 不存在,函数open() 将自动创建它。然而，以写入('w')模式打开文件时千万要小心，因为如果指定文件已经存在,
Python将在返回文件对象前清空该文件。
"""

###    Python只能将字符串写入  文本文件  。要将数值数据存储到文本文件中，必须先使用函数str() 将其转换为字符串格式


###    10.2.2 写入多行
"""函数write() 不会在你写入的文本末尾添加 换行符,因此如果你写入多行时没有指定换行符"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming !\n")
    file_object.write("I love creating new game !\n")


###    10.2.3  附加到文件
"""
如果你要给文件添加内容，而不是覆盖原有的内容，可以 附加模式 打开文件。你以附加模式打开文件时，Python不会在
返回文件对象前 清空文件，而你写入到文件的行都将添加到文件末尾。如果指定的文件不存在，Python将为你创建一个空
文件
"""
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I alse love finding meaning in large dataset.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


###    10.3 异常
"""Python 使用被称为 异常 的特殊对象来 管理程序执行期间发生的错误。每当发生让Python不知所措的错误时，它
都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理, 程序将停止, 并
显示一个traceback,其中包含有关异常的报告。"""

"""异常 是使用 try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常
时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令
用户迷惑的traceback。"""

###    10.3.1  处理ZeroDivisionError异常

print(5/0)

"""
处指出的错误 ZeroDivisionError 是一个异常对象。 Python 无法按你的要求做时，就会创建这种对象。在这种
情况下， Python 将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。下面我们将告诉
 Python ，发生这种错误时怎么办；这样，如果再次发生这样的错误，我们就有备无患了。
 """


###     10.3.2 使用try-except 代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


###    10.3.3  使用异常避免崩溃
"""
发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤为重要了。这种情况经常会出现在要求用户提供输入的
程序中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不止于崩溃。
"""

###     10.3.4  else代码块
"""
通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。错误是执行除法运算的
代码行导致的, 因此我们需要try-except代码块中，这个示例还包含一个 else代码块 ；依赖于 try代码块 成功
执行的代码都应放到 else代码块中：
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by 0! ")

    else:
        print(answer)


###     10.3.5  处理FileNotFoudError异常
"""使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其它地方、文件名可能不正确或者这个文件根本
就不存在。对于所有这些情形，都可使用 try-except代码块 以直观的方式进行处理。"""


filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

###     10.3.6 分析文本
"""你可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。本
节使用的文本来自项目 Gutenberg （ http://gutenberg.org/  ）"""

"""方法 split() 以空格为分隔符将字符串 分拆成多个部分，"""
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "Sorry, the file" + filename + " does not exist. "
    print(msg)

else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


###    10.3.7 使用多个文件
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        msg = "Sorry, the file" + filename + " does not exist. "
        print(msg)

    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)



def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " not be found."
        print(msg)

    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filenames in filename:
    count_words(filenames)


###    10.3.8   失败时一声不吭
"""在前一个实例中，我们告诉用户有一个文件找不到。但并非每次捕获到异常时都需要告诉用户，有时候你希望程序
在发生异常时一声不吭  ， Python 有一个 pass语句，可在代码块中使用它来让Python什么都不要做："""

file_objs = 'missing_files.txt'

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        pass

    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filenames in filename:
    count_words(filenames)


###    10.4  存储数据
"""很多程序都要求用户输入某种信息，如让用户存储 游戏首选项或提供要可视化的数据。不管专注的是什么，程序都把
用户提供的信息存储在 列表 和 字典 等数据结构中。用户关闭程序时，你几乎总是要保持他们提供的信息；一种简单的
方式是使用 模块json 来存储数据。

模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用
json在Python程序之间分享数据。 JSON数据格式并非Python专用的,这让你能够将以JSON格式存储的数据与其他编程
语言的人分享。 这是一种轻便格式，很有用，也易于学习。

    warning: JSON(JavaScript Object Notation)格式最初是为JavaScript开发的，但随后成为了一种常见格式，
被包括Python在内的众多语言采用。
"""

###    10.4.1 使用 json.dump() 和 json.load()

"""我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。第一个程序将使用 json.dump()
来存储这些数字，而第二个程序将使用 json.load() 。 

函数json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象。"""

# 使用 json.dump() 来存储数字列表：

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)


###    json.load() 将这个列表读取到内存中：
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)

# print(numbers)


###    10.4.2  保存和读取用户生成的数据
import json

username = input("What's your name ?")

filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("We'll remember you when you come back " + username + "!")


import json

filename = 'username.json'
with open(filename) as f_obj:
    users = json.load(f_obj)
    print("Welcome back, " + users )


import json

filename = 'username.json'
try:
    with open(filename) as file_object:
        users = json.load(file_object)

except FileNotFoundError:
    users = input("What's your name ? ")
    with open(filename, 'w') as file_object:
        json.dump(users, file_object)
        print("We'll remember when you come back, " + users + ".")

else:
    print("Welcome back, " + users + '!')


###    10.4.3  重构
##  代码能够正常运行，但可做进一步的改进—— 将代码划分为一系列完成具体工作的函数。这样的过程被称为 重构

import json

def greet_user():
    """问候用户，并指出其名字"""
    filename = 'usersname.json'
    try:
        with open(filename) as file_object:
            contents = json.load(file_object)

    except FileNotFoundError:
        users = input("What's your name ? ")
        with open(filename, 'w') as file_object:
            json.dump(users, file_object)
            print("We'll remember you when you come back, " + users)

    else:
        print("Welcome back, " + contents)

greet_user()


"""下面来重构 greet_user(), 让它不执行这么多任务。为此我们首先将获取存储的用户名的代码移到 另一个 函数中"""
import json

def get_sorted_username():
    """如果存储了用户名，就获取它"""
    filename = 'usename.json'
    try:
        with open(filename) as file_object:
            msg = json.load(file_object)

    except FileNotFoundError:
        return None

    else:
        return msg

def greet_user():
    msg = get_sorted_username()

    if msg:
        print("Welcome back, " + msg)

    else:
        msg = input("What's your name? ")
        filename = 'usename.json'
        with open(filename, 'w') as file_object:
            json.dump(msg, file_object)
            print("We'll remember you when you come back " + msg)

greet_user()

"""新增的函数 get_stored_username() 目标明确，❶处的文档字符串指出了这一点。如果存储了用户名，这个函数就
获取并返回它；如果文件 username.json 不存在，这个函数就返回 None （见❷）。这是一种不错的做法：函数要么返
回预期的值，要么返回 None ；这让我们能够使用函数的返回值做简单测试"""


###    第 11  章　测试代码
"""将学习如何使用unittest中的工具来测试代码。学习编写测试用例，"""

##    11.1  测试函数
#   11.1.1  单元测试和测试用例

"""创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。要为函数
编写测试用例，可先导入 模块unittest 以及要测试的函数，再创建一个继承 unittest.TestCase的类， 并编写一
系列方法对函数行为的不同方面进行测试。"""

###    11.1.3   不能通过的测试

###    11.1.4   测试未通过时怎么办

###    11.1.5   添加新测试

###    11.2    测试类
"""在本章前半部分，你编写了针对单个函数的测试，下面来编写针对类的测试。很多程序中都会用到类，因此能够证明你
的类能够正确地工作会大有裨益。如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为"""

###     11.2.1各种断言方法
##  Python 在 unittest.TestCase类中提供了很多断言方法。
"""
assertEqual(a,b)                     核实 a == b
assertNotEqual(a,b)                  核实 a != b
assertTrue(x)                        核实 x为 True
assertFalse(x)                       核实 x为 False
assertIn(item, list)                 核实 item 在 list 中
assertNotIn(item, list)              核实 item 不在 list 中
"""

###    11.2.2  一个要测试的类

###    11.2.4  方法setUp()






