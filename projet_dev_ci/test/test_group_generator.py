"""
Module used to test the Group_generator class
"""

import unittest

from projet_dev_ci.model.group import Group
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