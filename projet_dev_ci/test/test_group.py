"""
Module used to test the Group class
"""

import unittest

from model.group import Group
from model.user import User


class GroupTest(unittest.TestCase):
    """
    Class used to test the Group class
    """

    def test_group_creation(self) -> None:
        """
        Test if a group can be created
        """
        sut = Group(10)
        self.assertIsInstance(sut, Group)

    def test_group_add_user(self) -> None:
        """
        Test if an user can be added to a group
        """
        user = User("test")
        sut = Group(1)
        sut.add_user(user)
        self.assertEqual(user, sut.get_users()[0])

    def test_group_add_too_many_users(self) -> None:
        """
        Test if the group max size works properly when adding too many users to a group
        """
        group_size = 5
        sut = Group(group_size)
        for i in range(0, 10):
            sut.add_user(User("test" + str(i)))
        self.assertEqual(group_size, len(sut.get_users()))

    def test_group_add_null_user(self) -> None:
        """
        Test if an null user can de added to a group
        """
        user = None
        sut = Group(1)
        sut.add_user(user)
        self.assertEqual(0, len(sut.get_users()))

    def test_group_negative_size(self) -> None:
        """
        Test if a group can be created with a negative size
        """
        with self.assertRaises(ValueError):
            Group(-10)

    def test_group_get_max_size(self) -> None:
        """
        Test if the max size getter works properly
        """
        group_size = 5
        sut = Group(group_size)
        self.assertEqual(group_size, sut.get_max_size())

    def test_group_get_current_size(self) -> None:
        """
        Test if the get current size getter works properly
        """
        sut = Group(10)
        sut.add_user(User("test"))
        sut.add_user(User("test"))
        self.assertEqual(2, sut.get_current_size())


if __name__ == '__main__':
    unittest.main()
