"""
Module used to test the User class
"""

import unittest

from model.user import User


class UserTest(unittest.TestCase):
    """
    Class used to test the User class
    """

    def test_user_creation(self) -> None:
        """
        Test if an user can be created
        """
        sut = User("TEST")
        self.assertIsInstance(sut, User)

    def test_user_get_name(self) -> None:
        """
        Test if the get name getter works properly
        """
        name = "TEST NAME"
        sut = User(name)
        self.assertEqual(sut.get_name(), name)

    def test_user_get_id(self) -> None:
        """
        Test if the get id getter works properly
        """
        curr_id = User.get_static_id()
        User("0")
        User("1")
        self.assertEqual(curr_id + 2, User.get_static_id())


if __name__ == '__main__':
    unittest.main()
