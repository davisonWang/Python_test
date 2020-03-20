### Example 动手试一试(before 2.3字符串)
##First_one

# message = "I will be a winner!"
# print(message)
#
# message_1 = "I will be a winner"
# print(message_1)
# message_2 = "Not sometime, it is all the time"
# print(message_2)
# message_3 = "Hope yor be a champion through a whole life"
# print(message_3)



### Example 动手试一试(before 2.4 number)
## 2-3  个性化消息
# name_Eri = "Eric"
# print('“ ' + "Hello " + name_Eri +", would you like to learn some Python today" + ' ？”。')

## 2-4  调整名字的大小写(title(); upper(); lower())
# n = "eric"
# print(n.title())
# print(n.upper())
# print(n.lower())

## 2-5 名言
# first_name = 'albert'
# last_name = 'einstein'
# full_name = first_name.title() + " " + last_name.title()
# message_1 = ' once said, “ '
# message_2 = 'A person who never made a mistake never tried anything new.”'
# print(full_name.title() + message_1.lower() + message_2)
#
# ## 2-6  名言 2
# famous_person = 'albert einstein'
# message_1 = ' once said, “ '
# message_2 = 'A person who never made a mistake never tried anything new.”'
# message = famous_person.title() + message_1.lower() + message_2
# print(message)


## 2-7  剔除人名中的空白
# famous_name  = "\t\tDavison\t\n" + "\tWang\t"
# print(famous_name)
# print(famous_name.strip())
# print(famous_name.rstrip())
# print(famous_name.lstrip())

## 动手试一试 3-1  姓名
# names = ['Dumas pére', 'Socrates', 'Benjamin Franklin', 'Ho Chi Minh']
# # for name in names:
# #     print(name)
# ## 3-2  问候语： 继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
# message_1 = "Hello, " + names[0] + "nice to meet you."
# message_2 = "Hello, " + names[2] + "nice to meet you."
# message_3 = "Hello, " + names[-2] + "nice to meet you."
# message_4 = "Hello, " + names[-1] + "nice to meet you."
# print(message_1)
# print(message_2)
# print(message_3)
# print(message_4)

## 3-3  自己的列表：
# Commuter = ['buy', 'airplane', 'bicycle', 'motorcycle']
# message_1 = "“I would like to own a " + Commuter[-1] + "”"
# message_2 = "“I would like to own a " + Commuter[-2] + "”"
# message_3 = "“I would like to own a " + Commuter[1] + "”"
# message_4 = "“I would like to own a " + Commuter[0] + "”"
# commuter_way = [message_1, message_2, message_3, message_4]
# for c in commuter_way:
#     print(c)


### 动手试一试
## 3-4  嘉宾名单  如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用
## 这个列表打印消息，邀请这些人来与你共进晚餐。
# flatPeach_party = ['南海观音', '五百罗汉', '上八洞神仙', '中八洞神仙', '下八洞神仙', '东海龙王']
# message = str(flatPeach_party) + "天上神仙俱都邀请，共赴蟠桃盛宴！"
# print(message)
# ## 3-5  修改嘉宾名单
# New_name = flatPeach_party.pop()
# message_1 = New_name + '因故不能参加 '
# print(message_1)
# ## 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# flatPeach_party[-1] = '镇元大仙'
# print(flatPeach_party)
# ## 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
# for new in flatPeach_party:
#     print(new + "-邀请共赴蟠桃盛宴！")
# ### 3-6  添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# print('\n找到了一个更大的餐桌')
# flatPeach_party.append('如来佛祖')
# flatPeach_party.append('地府十阎')
# flatPeach_party.append('孙悟空')
# print(flatPeach_party)
# ## 使用 insert() 将一位新嘉宾添加到名单开头
# flatPeach_party.insert(0, '唐王李世民')
# print(flatPeach_party)
# ## 使用 insert() 将另一位新嘉宾添加到名单中间
# flatPeach_party.insert(5, '净坛使者')
# print(flatPeach_party)
# ## 使用 append() 将最后一位新嘉宾添加到名单末尾
# flatPeach_party.append('东海龙王')
# print(flatPeach_party)
# ## 打印一系列消息，向名单中的每位嘉宾发出邀请
# for new_n in flatPeach_party:
#     print(new_n + "-邀请共赴蟠桃盛宴！")
# ## 3-7  缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# print('只能邀请两位嘉宾共进晚餐')
# message_2 = '很抱歉，无法邀请共进晚餐'
# a = flatPeach_party.pop()
# print(a + message_2)
# b = flatPeach_party.pop()
# print(b + message_2)
# c = flatPeach_party.pop()
# print(c + message_2)
# d = flatPeach_party.pop()
# print(d + message_2)
# e = flatPeach_party.pop()
# print(e + message_2)
# f = flatPeach_party.pop()
# print(f + message_2)
# g = flatPeach_party.pop()
# print(g + message_2)
# h = flatPeach_party.pop()
# print(h + message_2)
# i = flatPeach_party.pop()
# print(i + message_2)
#
# attend_flatPeach_pa = '南海观音'
# flatPeach_party.remove(attend_flatPeach_pa)
# print(flatPeach_party)
# print(attend_flatPeach_pa + '您依然在受邀人之列')
#
# attend_flatPeach_pb = '唐王李世民'
# flatPeach_party.remove(attend_flatPeach_pb)
# print(flatPeach_party)
# print(attend_flatPeach_pb + '您依然在受邀人之列')
#
# name = []
# name.append('南海观音')
# name.append('唐王李世民')
# print(name)
# del name[0]
# print(name)
# del name[0]
# print(name)

### 动手试一试
## 3-8  放眼世界 ：想出至少 5 个你渴望去旅游的地方。
# area = ['China', 'Russia', 'Japan', 'Germany', 'American']
# ## 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始 Python 列表。
# print('\nHere is the original list:')
# print(area)
# ## 使用 sorted() 按字母顺序打印这个列表，同时不要修改它。
# print(sorted(area))
# ## 再次打印该列表，核实排列顺序未变。
# print('\nHere is the original list again:')
# print(area)
# ## 使用 sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
# print(sorted(area, reverse=True))           # sorted()，临时倒序列表可向函数sorted( , reverse=True)
# print(area)
# ## 使用 reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# area. reverse()
# print(area)
# ## 使用 reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序
# area.reverse()
# print(area)
# ## 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了
# area.sort()
# print(area)
# ## 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了
# area. sort(reverse=True)
# print(area)
#
# print(len(area))

### 3-10  尝试使用各个函数 ：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列
### 表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
# river = ['yellow', 'amazon', 'thames', 'ganges', 'nile']
# print(river)
# print(sorted(river))
# print(river)
# print(sorted(river, reverse=True))
# print(river)
# river.reverse()
# print(river)
# river.reverse()
# print(river)
# river.sort()
# print(river)
# river.sort(reverse=True)
# print(river)
# print(len(river))

### 动手试一试
## 4-1  比萨 ：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用 for 循环将每种比萨的名称都打印出来
# pizzas = ['pepperoni pizza', 'tomato pizza', 'bacon pizza']
# for pizza in pizzas:
#     print(pizza.title())
#     print('I like ' + pizza + ".\n")
#
# print("I really love pizza.")
#
# ## 4-2  动物 ：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用 for 循环将每种动物的名称都打印出来
# animes = ['dog', 'cat', 'tortoise']
# for anime in animes:
#     print(anime)
#     print('A ' + anime + ' would make a great pet.\n')
#
# print(' “Any of these animals would make a great pet!” ')

### 动手试一试
### 4-3  数到 20
# for value in range(1, 21):
#     print(value)
# ### 4-4  一百万
# for value in range(1, 1000001):
#     print(value)
### 4-5  计算 1~1 000 000 的总和
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
### 4-6  奇数
# for value in range(1, 21, 2):
#     print(value)
# ### 4-7 3 的倍数
# for value in range(3, 31, 3):
#     print(value)
# ### 4-8  立方
# squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for square in squares:
#     value = square **3
#     print(value)
# ### 4-9  立方解析
# square = []
# squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in squares:
#     value = number**3
#     square.append(value)
# print(square)

### 动手试一试  4-10  切片 ：
# squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('The first three items in the list are: ')
# print(squares[:3])  # 使用切片来打印列表的前三个元素, 用3取到2
# print('Three items from the middle of the list are: ')
# print(squares[3: 6])
# print('The last three items in the list are: ')
# print(squares[-3: ])

### 4-11  你的比萨和我的比萨 ：
# my_food = ['pizza', 'falafel', 'carrot pizza']
# friends_pizza = my_food[: ]
# ## 在原来的比萨列表中添加一种比萨
# my_food.append('bacon pizza')
# friends_pizza.insert(1, 'tomato pizza')
#
# for my_foods in my_food:
#     print('My favorite pizza are: ' + my_foods)
#
# for friends_pizzas in friends_pizza:
#     print("My friend's favorite pizzas are: " + friends_pizzas)

### 动手试一试
# ### 4-13  自助餐 ：
# buffets = ('noodle', 'salad', 'cheese', 'beef', 'chicken')
# for buffet in buffets:
#     print(buffet)
#
# # buffets[1] = 'cake'
# # for buffet in buffets:
# #     print(buffet)
#
# buffets = ('\nnoodle', 'chips', 'cheese', 'cook', 'hamburger')
# for buffet in buffets:
#     print(buffet)

### 动手试一试
# ## 5-1  条件测试 ：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("Is car == 'audi'? I predict False.")
# print(car == 'audi')
#
# ### 创建至少 10 个测试，且其中结果分别为 True 和 False 的测试都至少有 5 个
# ## The_first
# pizza = 'tomato_pizza'
# print("Is the topping for pizza == 'tomato'? I predict True")
# print(pizza == 'tomato_pizza')
#
# print("Is the topping for pizza == 'bacon'? I predict False")
# print(pizza == 'bacon')
# ##------------------------------------------------------------------------------------------------------------
# pet = 'dog'
# print("Is good pet == 'dog'? I predict True")
# print(pet == 'dog')
# print("Is good pet == 'cat'? I predict False")
# print(pet == 'cat')
# ##----------------------------------------------------------------------------------------------------
# car = 'audi'
# print("Is car == 'BMW'? I predict False")
# print(car == 'BMW')
# print("Is car == 'audi'? I predict True")
# print(car == 'audi')
# ##----------------------------------------------------------------------------------------------------
# noodle = 'beef noodle'
# print("Is noodle == 'beef noodle'? I predict True")
# print(noodle == 'beef noodle')
# print("Is noodle == 'tomato noodle'? I predict False")
# print(noodle == 'tomato noodle')
# ##----------------------------------------------------------------------------------------------------
# sports = 'Your life'
# print("Sports mirror your life ?  I predict True")
# print(sports == 'Your life')
# print("Sports microcosm your life? I predict False")
# print(sports == 'Your own')
# ##----------------------------------------------------------------------------------------------------
# gym = 'Kangfu'
# print("Kongfu is sports? I predict True")
# print(gym == 'Kangfu')
# print("Kongfu is gymnastics? I predict False")
# print(gym == 'sports')
#
# ### 5-2  更多的条件测试 ：你并非只能创建 10 个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到 conditional_tests.py 中。
# city = 'new york'
# print("Is 'New York city' ? I predict True")
# print(city == "New York".lower())
#
# number_0 = 21
# number_1 = 19
#
# print(number_0 == 21)
# print(number_0 != 21)
# print(number_0 > 21)
# print(number_0 >= 21)
# print(number_0 < 21)
# print(number_0 <= 21)
#
# print(number_0 <= 21 and number_1 < 19)
# print(number_0 <= 21 or number_1 <= 45 )
#
# requested_toppings = ['deer', 'rose']
# print('deer' in requested_toppings)
#
# if 'mushroom' not in requested_toppings:
#     print('rose'.title() + ' I love u!')

# ### 动手试一试 5-3  外星人颜色 #1
# alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print("Player gains 5 scores.")
#
# if 'white' in alien_color:
#     print("Player gains 5 scores.")
#
# ## 5-4  外星人颜色 #2  ：像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
# alien_color = ['green', 'yellow', 'red']
# alien = 'green'
# print(alien.title())
# if alien == 'green':
#     print("Player gains 5 scores.")
# else:
#     print("Player gains 10 scores")
#
#
# alien_color = ['green', 'yellow', 'red']
# alien = 'red'
# print(alien.title())
# if alien == 'green':
#     print("Player gains 5 scores.")
# else:
#     print("Player gains 10 scores")
#
# ### 5-5  外星人颜色 #3
# alien_color = ['green', 'yellow', 'red']
# alien = 'red'
# print(alien.title())
# if alien == 'green':
#     print("Player gains 5 scores.")
# elif alien == 'yellow':
#     print("Player gains 10 scores")
# else:
#     print("Player gains 15 scores.")
# ## -------------------------------------------------------------------------------------------------
# alien_color = ['green', 'yellow', 'red']
# alien = 'yellow'
# print(alien.title())
# if alien == 'green':
#     print("Player gains 5 scores.")
# elif alien == 'yellow':
#     print("Player gains 10 scores")
# else:
#     print("Player gains 15 scores.")
# ## ---------------------------------------------------------------------------------------------------
# alien_color = ['green', 'yellow', 'red']
# alien = 'green'
# print(alien.title())
# if alien == 'green':
#     print("Player gains 5 scores.")
# elif alien == 'yellow':
#     print("Player gains 10 scores")
# else:
#     print("Player gains 15 scores.")
#
# ### 5-6  人生的不同阶段 ：
#
# age = input("Please input the age")
# age = int(age)
#
# if age < 2:
#     print("He is a baby.")
#
# elif age < 4:
#     print("He learning walk.")
#
# elif age < 13:
#     print("He is a children.")
#
# elif age < 20:
#     print("He is a teenager.")
#
# elif age < 65:
#     print("He is a adult.")
#
# else:
#     print("He is a old man.")
#
# ### 5-7  喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的 if 语句，检查列表中是否包含特定的水果
# favorite_fruits = ['banana', 'apple', 'orange', 'mango', 'strawberry']
# if 'mango' in favorite_fruits:
#     print("I really like mango.")
#
# if 'banana' in favorite_fruits:
#     print("I really like banana.")
#
# if 'grape' in favorite_fruits:
#     print("I dislike grape.")
#
# if 'watermelon' in favorite_fruits:
#     print("I dislike watermelon.")
#
# if 'peach' in favorite_fruits:
#     print("I dislike peach.")

### 动手试一试
### 5-8  以特殊方式跟管理员打招呼
users_list = ['tom', 'eric', 'admin', 'dick', 'joe']
for user_list in users_list:
    if user_list == 'admin':
        print("Hello " + user_list.title() + ", would you like to see a status report ?")

    elif user_list == 'tom':
        print("Hello " + user_list.title() + ", thank you for logging in again.")

    elif user_list == 'eric':
        print("Hello " + user_list.title() + ", thank you for logging in again.")

    elif user_list == 'dick':
        print("Hello " + user_list.title() + ", thank you for logging in again.")

    elif user_list == 'joe':
        print("Hello " + user_list.title() + ", thank you for logging in again.")

### 5-9  处理没有用户的情形
    del users_list[0]
    del users_list[1]
    del users_list[2]
    del users_list[0]
    del users_list[0]
    print(users_list)

    users_list = []
    for user_list in users_list:
        if user_list == 'admin':
            print("Hello " + user_list.title() + ", would you like to see a status report ?")

        elif user_list == 'tom':
            print("Hello " + user_list.title() + ", thank you for logging in again.")

        elif user_list == 'eric':
            print("Hello " + user_list.title() + ", thank you for logging in again.")

        elif user_list == 'dick':
            print("Hello " + user_list.title() + ", thank you for logging in again.")

        elif user_list == 'joe':
            print("Hello " + user_list.title() + ", thank you for logging in again.")
    else:
        print("We need some users.")

### 5-10  检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式
current_users = ['Tom', 'JOHN', 'Tone', 'Candy', 'Mark']
new_users = ['john', 'Andy', 'Dick', 'Trump', 'Candy']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("You must use other user name.")

    else:
        print("This user name not use.")

### 5-11  序数 ：序数表示位置，如 1st 和 2nd 。大多数序数都以 th 结尾，只有 1 、 2 和 3 例外
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for number in numbers:
    if number == "1":
        print(number + " st")
    elif number == "2":
        print(number + " nd")
    else:
        print(number + " th")

### 动手试一试
### 6-1  人 ：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键 first_name 、 last_name 、 age 和 city 。将存储在该字典中
### 的每项信息都打印出来。
dictionary_name = {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'city': 'New York'}
print(dictionary_name['first_name'])
print(dictionary_name['last_name'])
print(dictionary_name['age'])
print(dictionary_name['city'])

### 6-2  喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存
### 储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。

favorite_nums = {
    'jen': 32,
    'sarah': 65,
    'edward': 24,
    'phil': 68,
    }
print("Favorite number is " + str(favorite_nums['jen']) + ".")
print("Favorite number is " + str(favorite_nums['sarah']) + ".")
print("Favorite number is " + str(favorite_nums['edward']) + ".")
print("favorite number is " + str(favorite_nums['phil']) + ".")

### 6-3  词汇表 ： Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
Vocabolary = {'pop': '删除最后一位',
              'del': '永久删除特定元素',
              'remove': '特定清除元素',
              'append': '添加元素',
              '.sort': '排序列表,car.sort(reverse=True)',
              'sorted': '临时排序',
              'insert': '[0, "Tom"]在列表中插入元素',
              'reverse': '永久性的修改列表元素', }

print("pop: \n\t" + Vocabolary['pop'])
print("del: \n\t" + Vocabolary['del'])
print("remove: \n\t" + Vocabolary['remove'])
print("append: \n\t" + Vocabolary['append'])
print(".sort: \n\t" + Vocabolary['.sort'])
print("sorted: \n\t" + Vocabolary['sorted'])
print("insert: \n\t" + Vocabolary['insert'])
print("reverse: \n\t" + Vocabolary['reverse'])

### 动手试一试
### 6-4  词汇表 2
vocabolary = {'pop': '删除最后一位',
              'del': '永久删除特定元素',
              'remove': '特定清除元素',
              'append': '添加元素',
              '.sort': '排序列表,car.sort(reverse=True)',
              'sorted': '临时排序',
              'insert': '[0, "Tom"]在列表中插入元素',
              'reverse': '永久性的修改列表元素', }

for key, value in vocabolary.items():
    print("Key: ", key)
    print("value: ", value)

vocabolary['adding'] = "添加元素，alien_0['x_position'] = 25 , alien_0['color'] = 'yellow'"
vocabolary['slice'] = 'alien[: 30]'
vocabolary['for in'] = 'for 循环遍历数组'
vocabolary['not in'] = '不在数组中'

for key, value in vocabolary.items():
    print("Key: ", key)
    print("Value: ", value)

### 6-5  河流
river_nation = {'nile': 'egypt', 'yellow river': 'china', 'amazon': 'brazil'}
for key, value in river_nation.items() :
    print("The " + key.title() + " runs though " + value.title() + ".")

for key in river_nation.keys():
    print("River: " + key)

for value in river_nation.values():
    print("Nation: " + value)

### 6-6  调查

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

users_list = ['trump', 'joe', 'mark', 'sarah', 'phil']
keys = []
for key in favorite_languages.keys():
    keys.append(key)

print(users_list)

for users in users_list:
    if users in keys:
        print("Thank you join")

    else:
        print("hope you take our poll")

## 动手试一试
### 6-7  人
dictionary_name = {'first_name': 'Donald', 'last_name': 'Trump', 'age': 65, 'city': 'New York'}
dictionary_name_2 = {'first_name': 'Joe', 'last_name': 'Biden', 'age': 75, 'city': 'New York'}
dictionary_name_3 = {'first_name': 'Mike', 'last_name': 'Pompeo', 'age': 56, 'city': 'new York'}

people = [dictionary_name, dictionary_name_2, dictionary_name_3]
for people_info in people:
    print(people_info)

### 6-8  宠物

for range_number in range(0, 30):
    if range_number < 1:
        dogs = {'type': 'dog', 'owner': 'Trump', }
        cats = {'type': 'cats', 'owner': 'Biden', }
        rats = {'type': 'rats', 'owner': 'Pompeo',}
        pets = [dogs, cats, rats]
        for pet in pets:
            print(pet)

### 6-9  喜欢的地方
favorite_places = {'Trump': ['New York', 'England', 'Pair'],
                   'Biden': ['Australia', 'Canada', 'Japan'],
                   'Pompeo':['Europe']
                   }

for users, places in favorite_places.items():
    if len(places) > 2:
        print("\n" + users.upper() + "'s favorite place are: ")
        for place in places:
            print("\t" + place.upper())

    else:
        print("\n" + users.upper() + "'s favorite place is: C")

### 6-10  喜欢的数字
favorite_nums = {
    'jen': [32, 34],
    'sarah': [65, 56, 78],
    'edward': [24, 45, 68],
    'phil': [68, 20, 30],
    }

for users, nubs in favorite_nums.items():
    print("User: " + users + "'s favorite numbers are: ")
    for nub in nubs:
        print(nub)

### 6-11  城市
cities = {'New York': {'country': 'USA', 'popular': 230, 'fact': 'I am grown up in.'},
          'BeiJing': {'country': 'China', 'popular': 357, 'fact': 'beijing located in east China.'},
          'New Delhi': {'country': 'India', 'popular': 246, 'fact': 'One of big city in this world', }
         }

for key, values in cities.items():
    print('\n-City: ' + key.title())
    country = values['country']
    popular = values['popular']
    fact = values['fact']
    print("\tLocated in: " + country +"." + '\n\t\tLiving in: ' + str(popular) +"Million" + '\n\t\t\tFact is:' + fact +".")

### 动手试一试
### 7-1  汽车租赁
print("What type of car do you want to rend? ")
car = input()

if car.title() == 'Subaru':
    print("Let me see if I can find you a Subaru")
else:
    print("Okay")

### 7-2  餐馆订位
nums = input("How many people eating? ")
nums = int(nums)
if nums <= 8:
    print("有空桌")
else:
    print("没有空桌")

### 7-3 10 的整数倍
numbers = input("Please enter a number: ")
numbers = int(numbers)

if numbers % 10 == 0:
    print("是10的整数倍")

else:
    print("不是10的整数倍")

### 动手试一试
### 7-4  比萨配料
prompt = "\nPlease writing your favorite pizza's toppings. "
prompt += "\nYour favorite toppings are: \n"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("\n\tWe will adding this topping " + message + " in pizza.")

### 7-5  电影票
prompt = "\nHow old are you ? \n"
prompt += "Enter your real age: \n"

active = True
while active:
    message = input(prompt)
    message = int(message)

    if message <= 0:
        print("System quits")
        break

    if message < 3:
        print("You are free. ")

    elif (message >= 3 and message < 12):
        print("You must pay $10. ")

    else:
        print("You must pay $15. ")

## 7-6  三个出口 ：
## 7-7  无限循环 ：
x = 3
while x <= 7:
    print(x)
    x += 1

### 动手试一试
sandwich_orders = ['tuna sandwich', 'ham sandwich', 'bacon sandwich', 'turkey sandwich']
finished_sandwich = []

while sandwich_orders:
    current = sandwich_orders.pop()
    finished_sandwich.append(current)
    print("I made your sandwich " + current.title() + ".")

print("\nAfter you've made all sandwich\n")
for finished_sandwichs in finished_sandwich:
    print(finished_sandwichs.title())

###    7-9  五香烟熏牛肉（ pastrami ）## remove('pastrami')
sandwich_orders = ['tuna sandwich', 'pastrami', 'ham sandwich', 'pastrami', 'bacon sandwich', 'turkey sandwich', 'pastrami']
print("\nThe deli is out of pastrami.\n ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')      # .remove('pastrami') 定点清除pastrami

print("------Sold Results------\n")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())

###     7-10  梦想的度假胜地 ：
### 可使用 while 循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以
### 便将回答同被调查者关联起来：
responses = {}

respond_active = True
while respond_active:

    name = input("Please enter your name: ")
    print("Thanks for you cooperation.")
    print("\n---------- 2nd Question ----------\n")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place     ## 将 name 与 place 关联，并存储在 responses 中。

    message = input("Would you want to finish this poll? (yes/no)")
    if message == 'yes':
        respond_active = False

print("---------- Poll Results ----------\n")
for name, place in responses.items():
    print(name + " could visit " + place + " in this world !")

### 动手试一试
### 8-1  消息
def display_message():
    """ 本章学习"""
    print("函数调用，实参、形参")

display_message()

### 8-2  喜欢的图书
def favorite_book(title):
    """形参title 实参 爱丽丝梦游仙境"""
    print("One of my favorite book is " + title)

favorite_book('Alice in Wonderland')

### 动手试一试
###  8-3 T 恤

def make_shirt(shirt_size, shirt_words):
    for char in shirt_words.split():
       allChar = []
       for y in range(12, -12, -1):
           lst = []
           lst_con = ''
           for x in range(-30, 30):
                formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
                if formula <= 0:
                    lst_con += char[(x) % len(char)]
                else:
                    lst_con += ' '
           lst.append(lst_con)
           allChar += lst
       print('\n'.join(allChar))

    print("The T-shirt's size :" + str(shirt_size) + ".")

make_shirt(32, "Apple")


###   8-4  大号 T 恤
def make_shirt(shirt_size='B', shirt_words='I love Python'):
    print("------------------I have a Size-" + shirt_size + " T-shirt---------------------------")
    print("\n\tPrinting “ " + shirt_words + " ” Size-" + shirt_size + " T-shirt.\n")

make_shirt()
make_shirt('M')
make_shirt(shirt_words='I love C#')

###    8-5  城市
def describe_city(city, nation='iceland'):
    print(city.title() + " is in " + nation.title())

describe_city('reykjavik')
describe_city(nation='iceland', city='dhhssja')
describe_city(nation='Japan', city='tokyo')

###   动手试一试
###   8-6  城市名
def city_country(city, country):
    c_country = '"' + city +", " + country + '"'
    return c_country.title()

describe_city= city_country('santiago', 'chile')
print(describe_city)

describe_city = city_country('tokyo', 'japan')
print(describe_city)

describe_city = city_country('nijing', 'china')
print(describe_city)

###    8-7  专辑
def make_album(musician, album, year=''):
    mus_alb = {'Musician: ':musician, 'Album: ':album}
    if year:
        mus_alb['year'] = year
    return  mus_alb

album_message = make_album('Taylor Swift', 'love story',)
print(album_message)

album_message = make_album('Charlie Puth', 'see you again', 2013)
print(album_message)

album_message = make_album('Troye sylvan maylie', 'for them')
print(album_message)

###  8-8  用户的专辑
def make_album(musician, album, music_num=' '):
    mak_alb_info = {'Musician': musician, 'Album': album, }
    if music_num:
        mak_alb_info['Music album numbers']=music_num
        full_music_info = "Musician: " + musician + "'s album 《" + album + "》music numbers " + music_num
        return full_music_info
    else:
        full_music_info = "Musician: " + musician +"'s album 《" + album + "》"
        return full_music_info

while True:
    print("--------------------------------------------------")
    print("\n--------------Favorite Musician --------------")
    print("\n\t\t\tPlease answer our poll")
    print("If you input 'q' at any time to quit")
    mus_inp = input("\nPlease enter your favorite musician's name: ")
    if mus_inp == 'q':
        break

    alb_inp = input("\nPlease enter musician's core album: ")
    if alb_inp == 'q':
        break

    mus_inp_numbs = input("\nPlease enter musician's album numbers: ")
    if mus_inp_numbs == 'q':
        break

    mus_message = make_album(mus_inp, alb_inp, mus_inp_numbs)
    print(mus_message)

### 动手试一试
###    8-9  魔术师

def show_magicians(names):
    for name in names:
        print(name)

magician_names = ['Beethoven', 'Mozart', 'Gandalf', 'Saruman']
show_magicians(magician_names)

###   8-10  了不起的魔术师-----------------------------------------------------------------------------------------------
def make_great(names, new_magician_name):
    while names:             ### while为True有 值就 执行，直到没有
        current_list = names.pop()
        new_list = "the Great " + current_list
        new_magician_name.append(new_list)

def show_magicians(new_magician_name):
    for name in new_magician_name:
        print(name)

magician_names = ['Beethoven', 'Mozart', 'Gandalf', 'Saruman']
new_magician_name = []
make_great(magician_names, new_magician_name)
show_magicians(new_magician_name)

### 8-11  不变的魔术师

def make_great(names, new_magician_name):
    while names:             ### while为True有 值就 执行，直到没有
        current_list = names.pop()
        new_list = "the Great " + current_list
        new_magician_name.append(new_list)

def show_magicians(new_magician_name):
    for name in new_magician_name:
        print(name)

magician_names = ['Beethoven', 'Mozart', 'Gandalf', 'Saruman']
new_magician_name = []
make_great(magician_names[:], new_magician_name)    ##   make_great(magician_name[:], new_magician_name)
show_magicians(new_magician_name)
print(magician_names)

### 动手试一试
### 8-12  三明治

def make_sandwish(*toppings):        ### 只有一个  *
    print(toppings)

    # for topping in toppings:
    #     print(topping)

make_sandwish('green peppers')
make_sandwish('chile', 'extra cheese', 'tomato')

###    8-13  用户简介
def build_profile(first, last, **user_info):
    """创建空列表"""
    profile = {}
    profile['First name'] = first
    profile['Last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_info = build_profile('Davison', 'Wang', location='princeton', field='Internet technology', heigh=182)
print(user_info)

#### 8-14  汽车
def make_car(name, area, **car_info):
    print("\nThe information of car:")
    profile = {}
    profile['Name'] = name
    profile['Place of production'] = area
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)

###    动手试一试
###    8-15  打印模型 ：将示例 print_models.py 中的函数放在另一个名为 printing_functions.py 的文件中；在 print_models.py
# 的开头编写一条 import 语句，并修改这个文件以使用导入的函数。

###    8-16  导入


###    动手试一试
##     9-1  餐馆
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """初始化命令restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """模拟描述餐馆信息"""
        print(self.restaurant_name.title() + " is the biggest west restaurant.")

    def open_restaurant(self):
        """描述餐馆正在营业"""
        print(self.restaurant_name.title() + " is opening. ")


class Restaurant():
    restaurant = Restaurant('Burger King', 'west')
    print("This restaurant's name is " + restaurant.restaurant_name.title() + ".")
    print("The cuisine type is " + restaurant.cuisine_type + ".")

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

###    9-2  三家餐馆

    restaurant = Restaurant('Mcdonald', 'fried foods')
    print("This restaurant's name is " + restaurant.restaurant_name.title() + ".")
    print("The cuisine type is " + restaurant.cuisine_type + ".")

###    9-3  用户
class User():

    def __init__(self, first_name, last_name):
        """初始化first_name和last_name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Users' name: " + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ",nice to meet you !")

class User():
    my_users = User('Donald', 'Trump')
    print("Full name: " + my_users.first_name + " " + my_users.last_name)

    my_users.describe_user()
    my_users.greet_user()

    your_users = User('Warry', 'Buffett')
    print("Full name: " + your_users.first_name + ' ' + your_users.last_name)

    your_users.describe_user()
    your_users.greet_user()

    his_user = User('Steven', 'jobs')
    print("Full name: " + his_user.first_name + " " + his_user.last_name)

    his_user.describe_user()
    his_user.greet_user()


###     动手试一试
###    9-4  就餐人数

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is the biggest " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening ")

    def restaurant_numbers(self):
        print(str(self.number_served) + " people have eaten in this restaurant")

    def set_number_served(self, numbers):
        if numbers >= self.number_served:
            self.number_served = numbers
        else:
            print("Don't roll back")
        # self.number_served = numbers

    def increment_number_served(self, serves):
        self.number_served += serves

restaurant = Restaurant('全聚德', 'traditional chinese dish')
print("The restaurant's name is " + restaurant.restaurant_name)
print("The restaurant cuisine type is " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.restaurant_numbers()

restaurant.number_served = 26
restaurant.restaurant_numbers()

restaurant.set_number_served(32)
restaurant.restaurant_numbers()

restaurant.increment_number_served(6)
restaurant.restaurant_numbers()

###    9-5  尝试登录次数
class User():

    def __init__(self, first_name, last_name):
        self.frist_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("Users' information " + self.frist_name + ' ' + self.last_name)

    def greet_user(self):
        print(self.frist_name + ' ' + self.last_name + ", nice to meet you.")

    def increment_login_attempts(self, increment_login):
        if increment_login == 1:
            self.login_attempts += increment_login
        else:
            print("Please enter 1")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def login_attempts_reading(self):
        print("Attempt login times: " + str(self.login_attempts))

my_user = User('Donald', 'Trump')
print("Full name: " + my_user.frist_name + " " + my_user.last_name)
my_user.describe_user()
my_user.greet_user()

my_user.increment_login_attempts(1)
my_user.login_attempts_reading()

for value in range(1, 5):
    my_user.increment_login_attempts(1)
    my_user.login_attempts_reading()

my_user.reset_login_attempts()
my_user.login_attempts_reading()

current_numbers = 1
while current_numbers <= 8:
    my_user.increment_login_attempts(1)
    my_user.login_attempts_reading()
    current_numbers += 1

my_user.reset_login_attempts()
my_user.login_attempts_reading()

new_list = [1, 2, 3, 4, 5, 6, 7]
for c in new_list[:5]:
    my_user.increment_login_attempts(1)
    my_user.login_attempts_reading()

###    动手试一试
##    9-6  冰淇淋小店
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name + " is the biggest " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening.")

    def number_served_reading(self):
        print("Have " + str(self.number_served) + " people eaten in here.")

    def set_number_served(self, reset_eaten_number):
        if reset_eaten_number >= 36:
            self.number_served = reset_eaten_number

        else:
            print("Your information not accurate !")

    def increment_number_served(self, increment_numbers):
        self.number_served += increment_numbers

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['草莓冰激凌', '坚果冰淇淋', '西瓜冰淇淋', '龙舌兰冰激凌']

    def read_icecream(self):
        for flavor in self.flavors:
            print(flavor)

        # print(self.flavors[:4])


restaurant = Restaurant('全聚德', 'traditional chinese dish.')

print("Restaurant's name is: " + restaurant.restaurant_name)
print("Restaurant's cuisine type: " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 27
restaurant.number_served_reading()

restaurant.set_number_served(36)
restaurant.number_served_reading()

restaurant.increment_number_served(3)
restaurant.number_served_reading()

icecream_restaurant = IceCreamStand('阿迪达斯', 'delicious ice cream.')
icecream_restaurant.describe_restaurant()
icecream_restaurant.read_icecream()

###     9-7 管理员
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        return full_name.title()

    def greet_user(self):
        print(self.describe_user() + " nice to meet you !")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def reading_login_attempts(self):
        print("Attempt login times: " + str(self.login_attempts))

class Privileges():
    def __init__(self):            # def __init__(self, privileges):去掉形参 privileges
        # self.privileges = privileges
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print("Administrator privileges : " + privilege.upper())


class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()


my_user = User('donald', 'trump')
print(my_user.describe_user())
my_user.greet_user()

for value in range(1, 5):
    my_user.increment_login_attempts(1)
    my_user.reading_login_attempts()

my_user.reset_login_attempts()
my_user.reading_login_attempts()

# current_numbers = 1
# while current_numbers <= 5:
#     my_user.increment_login_attempts(1)
#     my_user.reading_login_attempts()
#     current_numbers += 1

your_user = Admin('joe', 'biden')
print(your_user.describe_user())
your_user.greet_user()


##9-8  权限
your_user.privileges.show_privileges()

###    9-9  电瓶升级
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer! ")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery. ")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 280

        elif self.battery_size == 85:
            range = 300

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge. "
        print(message)
        self.upgrade_battery()

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        # self.battery_size = 70
        self.battery_size = Battery()

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank !")


my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.fill_gas_tank()

my_tesla.battery_size.get_range()
my_tesla.battery_size.get_range()

###    动手试一试
##  9-10  导入 Restaurant 类 ：将最新的 Restaurant 类存储在一个模块中。在另一个文件中，导入 Restaurant 类，
# 创建一个 Restaurant 实例，并调 用 Restaurant 的一个方法，以确认 import 语句正确无误。

##  9-11  导入 Admin 类 ：

##  9-12   多个模块：
##  将 User 类存储在一个模块中，并将 Privileges 和 Admin 类存储在另一个模块中。再创建一个文件，在其中创建一个
# Admin 实例，并对其调用方法 show_privileges() ，以确认一切都依然能够正确地运行。

###    动手试一试
##   9-13  使用 OrderedDict

vocabolary = {'pop': '删除最后一位',
              'del': '永久删除特定元素',
              'remove': '特定清除元素',
              'append': '添加元素',
              '.sort': '排序列表,car.sort(reverse=True)',
              'sorted': '临时排序',
              'insert': '[0, "Tom"]在列表中插入元素',
              'reverse': '永久性的修改列表元素', }

for key, value in vocabolary.items():
    print("Key: ", key)
    print("value: ", value)

vocabolary['adding'] = "添加元素，alien_0['x_position'] = 25 , alien_0['color'] = 'yellow'"
vocabolary['slice'] = 'alien[: 30]'
vocabolary['for in'] = 'for 循环遍历数组'
vocabolary['not in'] = '不在数组中'

for key, value in vocabolary.items():
    print("Key: ", key)
    print("Value: ", value)

##----------------------------------------------------------------------------------------------------------------

from collections import OrderedDict

vocabolary = OrderedDict()

vocabolary = {'pop': '删除最后一位',
              'del': '永久删除特定元素',
              'remove': '特定清除元素',
              'append': '添加元素',
              '.sort': '排序列表,car.sort(reverse=True)',
              'sorted': '临时排序',
              'insert': '[0, "Tom"]在列表中插入元素',
              'reverse': '永久性的修改列表元素', }

for key, value in vocabolary.items():
    print("Key: ", key)
    print("value: ", value)

vocabolary['adding'] = "添加元素，alien_0['x_position'] = 25 , alien_0['color'] = 'yellow'"
vocabolary['slice'] = 'alien[: 30]'
vocabolary['for in'] = '遍历数组'
vocabolary['not in'] = '不在数组中'

for key, value in vocabolary.items():
    print("Key :", key)
    print("Value: ", value)

###    9-14  骰子 ：------------------------------------------------------------------------------------------------

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, sides):
        for times in range(1, 11):
            self.sides = randint(1, sides)
            print("A random number between the face of a die: point " + str(self.sides))

my_die = Die()
my_die.roll_die(6)
print("--------------------------------------------------------------")

your_die = Die()
my_die.roll_die(10)
print("==============================================================")

his_die = Die()
my_die.roll_die(20)

###    动手试一试
###    10-1 Python 学习笔记
with open('text_files/python_learn.txt') as file_object:
    # content = file_object.read()
    # print(content)

    for lines in file_object:
        print(lines.rstrip())

filename = 'text_files/python_learn.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

list = []
"""strip()删除行左的空格，rstrip()删除换行符"""
for line in lines:
    list.append(line.strip())

print(list)

###    10-2 C 语言学习笔记
"""将txt文档存储在变量filename中"""
filename = 'text_files/python_learn.txt'

"""使用with代码块打开文档,并逐行读取文档"""
with open(filename) as file_object:
    lines = file_object.readlines()

file_strig = " "
for line in lines:
    file_strig += line

print(file_strig.replace('Python', 'C'))


###    动手试一试
##    10-3 访客
enter_name = 'guest.txt'

with open(enter_name, 'w') as file_object:

    for value in range(1, 6):
        message = str(input("Please enter your name:"))
        file_object.write("\n")
        file_object.write(message)

##     10-4  访客名单
enter_name = 'guest_book.txt'

string_name = ''
with open(enter_name, 'w') as file_object:
    while True:
        message = input("What's your name ?")
        if message == 'q':
            break
        else:
            string_name += message.title()
            string_name += ",nice to see you.\n"
            print(string_name)
"""Python 只能将字符串 写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。"""

    file_object.write(str(string_name))


###    10-5  关于编程的调查
filename = 'guest_book.txt'
string_name = ''

with open(filename, 'a') as file_object:

    while True:
        content = str(input("Why you love programing ?"))
        if content == 'q':
            break
        else:
            string_name += content
            string_name += "\n"
            print(string_name)

    file_object.write(string_name)


###    动手试一试
##  10-6   加法运算
###   10-7  加法计算器

while True:
    first_num = input("Provide first numerical input: ")
    if first_num == 'q':
        break
    second_num = input("Provide second numerical input: ")
    if second_num == 'q':
        break

    try:
        sum = int(first_num) + int(second_num)

    except ValueError:
        print("Please enter a number! ")

    else:
        print(sum)

###   10-8  猫和狗
filename_dog = 'dogs.txt'
filename_cat = 'cats.txt'

def append_animal(filename):
    with open(filename_dog, 'a') as file_object:
        file_object.write(str(filename))

def append_animal(filename):
    with open(filename_cat, 'a') as file_object:
        file_object.write(str(filename))


filename_dogs = ['Toney\n', 'Tank\n', 'willian\n']
for filename_d in filename_dogs:
    append_animal(filename_d)

filename_cats = ['Tom\n', 'LiLi\n', 'Andy\n']
for filename_d in filename_cats:
    append_animal(filename_d)
#--------------------------------------------------READING---------------------------------------------------------
filename = 'cats.txt'

with open(filename) as filename_object:
    content = filename_object.read()
    print(content)


filename = 'dogs.txt'
try:
    with open(filename) as filename_object:
        msg = filename_object.read()

except FileNotFoundError:
    print("This file does not exit")

else:
    print(msg)


###    10-9 沉默的猫和狗
filename = 'dogs.txt'
filename = 'cats.txt'

try:
    with open(filename) as filename_object:
        msg = filename_object.read()

except FileNotFoundError:
    pass

try:
    with open(filename) as filename_object:
        content = filename_object.read()

except FileNotFoundError:
    print("This file does not found!")

else:
    print(content)


###  10-10 常见单词
filename = 'alice.txt'

with open(filename) as filename_object:
    line = filename_object.read()
    words = line.split()
    print(len(words))
    print(words.count('The'))

    msg = str(words).lower()
    print(msg.count('the'))


###    动手试一试
##   10-11  喜欢的数字
import json

filename = 'fav_num.json'

content = input("Please enter your favorite numbers: ")

try:
    with open(filename, 'w') as f_obj:
        json.dump(int(content), f_obj)

except ValueError:
    print("Please enter a number! ")

else:
    print("I know your favorite number! It's " + content + ".")

import json

filename = 'fav_num.json'

with open(filename) as f_obj:
    msg = str(json.load(f_obj))
    print("I know your favorite number! It's " + msg + ".")


###    10-12  记住喜欢的数字
import json

def read_favorite_number():
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            user_info = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_info

def get_stored_favorite_number():
    user_info = input("What's your favorite number? ")
    filename = 'fav_num.json'
    with open(filename, 'w') as fav_obj:
        json.dump(user_info, fav_obj)
    return user_info


def greet_user():
    """问候用户，并指出其喜欢的数字"""

    user_info = read_favorite_number()
    if user_info:
        print("I remember your favorite number is " + user_info + ".")
    else:
        user_info = get_stored_favorite_number()
        print("We'll remember your number," + user_info + " thanks for your cooperation")

for value in range(0,2):
    greet_user()


#













##    10-13  验证用户
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as filename_object:
            username = json.load(filename_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as filename_object:
        json.dump(username, filename_object)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        msg = input("Are you define your name is " + username + "?  y/n")
        if msg == "y":
            print("Welcome back, " + username)
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()


###    动手试一试














































































