from user import User
from admin import Admin

my_user = User('joe', 'biden')
print(my_user.describe_user())
#---------------------------------------------------------------------------------------------------------------------
my_admin = Admin('Donald', 'Trump')
print(my_admin.describe_user())
my_admin.privileges.show_privileges()

