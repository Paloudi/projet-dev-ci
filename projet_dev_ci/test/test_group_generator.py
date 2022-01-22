"""
Module used to test the Group_generator class
"""

import unittest

from projet_dev_ci.model.group_generator import Group_generator
from projet_dev_ci.model.group import Group
from typing import List
from projet_dev_ci.model.user import User


class GroupGeneratorTest(unittest.TestCase):
    """
    Class used to test the Group class
    """

    # def test_group_creation(self) -> None:
    #     """
    #     Test if a group can be created
    #     """
    #     sut = Group(10)
    #     self.assertIsInstance(sut, Group)

    def test(self) -> None:
        # user_list_test: List[User] = [User("Frédo"), User("Quentin"), User("David")]

        user_list_test = [User("Frédo"), User("Quentin"), User("David"), User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"), User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"), User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David")]

        sut = Group_generator(user_list_test, 6, "LAST_MIN")
        self.assertEqual(2, 2)
        # sut = Group_generator()