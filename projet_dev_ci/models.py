from typing import List

from django.db import models


# Create your models here.

class User(models.Model):
    """
    An user represent... an user.
    An user has a name
    """

    name = models.TextField()

    class Meta:
        db_table = "users"


class Group(models.Model):
    """
    A group represent a list of users.
    A group has a given max size and cannot be bigger than this size
    """

    max_size = models.PositiveIntegerField()
    current_size = models.PositiveIntegerField()
    users = models.TextField(null=True)
    list_users = []

    # region Methods

    def add_user(self, new_user: User) -> None:
        """
        Add a new user to this group
        :param new_user: an user to add to this group
        :type new_user: User
        """
        if new_user and isinstance(new_user, User):
            if self.max_size > self.current_size:
                self.list_users.append(new_user)
                self.current_size += 1

    # endregion

    # region Getters

    def get_users(self) -> List[User]:
        """
        Returns the list of the users of this group
        :return: This group users list
        :rtype: List[User]
        """
        return self.list_users

    # endregion
