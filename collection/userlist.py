# USER LIST

from collections import UserList


class MyUniqueList(UserList):

    def add_in_middle(self, item):
        count = -1
        for i in self:
            count += 1

        self[int(count / 2)] = item


my_list = MyUniqueList([1, 2, 3, 4, 5])
print(my_list)

my_list.add_in_middle("CFG")
print(my_list)