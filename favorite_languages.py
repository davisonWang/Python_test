from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'Python'
favorite_language['sarah'] = 'C'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#----------------------------------------------------------------------------------------------------------------------
favorite_language['jen'] = 'Python'
favorite_language['sarah'] = 'C'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

