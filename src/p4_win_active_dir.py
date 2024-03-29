class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        print('Warning: you\'re not passing a valid group!')
        return False
    if user in group.get_users():
        return True
    if len(group.groups):
        for subg in group.groups:
            if is_user_in_group(user, subg):
                return True
    return False


print(is_user_in_group(sub_child_user, sub_child))  # Return True
print(is_user_in_group(sub_child_user, child))  # Return True
print(is_user_in_group(sub_child_user, parent))  # Return True


print()
print(is_user_in_group(sub_child_user, None))  # Return False and print a warning message!

print()
print(is_user_in_group(None, parent))  # If user is an invalid object it simply not found in the user lists
