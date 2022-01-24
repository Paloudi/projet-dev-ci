"""
Module used to test the Group_generator class
"""

import unittest

from projet_dev_ci.model.groupgenerator import GroupGenerator
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

    # region test_groups_generation

    def test_twenty_users_six_groups(self) -> None:
        """
        Test which verify if the group generator class creates 7 groups,
        6 of 3 users and one of 2 users (because of "LAST_MIN" param)
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David")]

        sut = GroupGenerator(user_list_test, 6, "LAST_MIN")
        self.assertEqual(sut.get_number_of_groups(), 7)

    def test_group_generator_odd_number_of_user_and_group_size(self) -> None:
        """
        19 users, 7 groups (in the best case) with last_min
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 7, "LAST_MIN")
        self.assertEqual(sut.get_number_of_groups(), 5)

    def test_group_generator_odd_number_of_user_and_even_group_size(self) -> None:
        """
        19 users, 7 groups (in the best case) with last_min
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MIN")
        self.assertEqual(sut.get_number_of_groups(), 5)

    # endregion
