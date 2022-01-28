"""
Module used to test the Group_generator class
Module used to test the Group_generator class
"""

import unittest
from projet_dev_ci.models.groupgenerator import GroupGenerator
from projet_dev_ci.models.user import User
from projet_dev_ci.models.group import Group


class GroupGeneratorTest(unittest.TestCase):
    """
    Class used to test the Group class
    -> We do not test getters and setters because we decided that it is not relevant
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

    def test_group_generator_odd_number_of_user_and_group_size_with_last_min(self) -> None:
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

    def test_group_generator_odd_number_of_user_and_group_size_with_last_max(self) -> None:
        """
        19 users, 7 groups (in the best case) with last_max
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 7, "LAST_MAX")
        self.assertEqual(sut.get_number_of_groups(), 6)

    def test_group_generator_odd_number_of_user_and_even_group_size_with_last_min(self) -> None:
        """
        19 users, 8 groups (in the best case) with last_min
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

    def test_group_generator_odd_number_of_user_and_even_group_size_with_last_max(self) -> None:
        """
        19 users, 8 groups (in the best case) with last_max
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")
        self.assertEqual(sut.get_number_of_groups(), 9)

    def test_get_last_param(self) -> None:
        """
        Test method to test the getter
        """
        last_param_expected = "LAST_MAX"
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, last_param_expected)

        self.assertEqual(sut.get_last_param(), last_param_expected)
        self.assertIsInstance(sut.get_last_param(), str)

    def test_get_users_list(self) -> None:
        """
        Test method to test the getter
        """
        user_list_test_expected = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test_expected, 8, "LAST_MAX")

        self.assertEqual(sut.get_users_list(), user_list_test_expected)
        self.assertIsInstance(sut.get_users_list(), list)

    def test_get_users_number(self) -> None:
        """
        Test method to test the getter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        self.assertEqual(len(sut.get_users_list()), len(user_list_test))
        self.assertIsInstance(sut.get_users_number(), int)

    def test_get_group_list(self) -> None:
        """
        Test method to test the getter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        self.assertEqual(len(sut.get_groups_list()), 9)
        self.assertIsInstance(sut.get_groups_list(), list)

    def test_get_number_of_groups(self) -> None:
        """
        Test method to test the getter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        self.assertEqual(sut.get_number_of_groups(), 9)
        self.assertIsInstance(sut.get_number_of_groups(), int)

    def test_get_last_group(self) -> None:
        """
        Test method to test the getter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        last_group_expected = sut.get_groups_list()[-1]

        self.assertEqual(last_group_expected, sut.get_last_group())
        self.assertIsInstance(sut.get_last_group(), Group)

    def test_set_last_param(self) -> None:
        """
        Test method to test the setter
        """
        last_param_before = "LAST_MAX"
        last_param_expected = "LAST_MIN"
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, last_param_before)

        sut.set_last_param(last_param_expected)

        self.assertNotEqual(last_param_before, last_param_expected)
        self.assertEqual(sut.get_last_param(), last_param_expected)

    def test_set_users_list(self) -> None:
        """
        Test method to test the setter
        """
        user_list_expected = [User("Frédo"), User("Quentin"), User("David")]
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        sut.set_users_list(user_list_expected)

        self.assertNotEqual(user_list_expected, user_list_test)
        self.assertEqual(sut.get_users_list(), user_list_expected)

    def test_set_users_number(self) -> None:
        """
        Test method to test the setter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        user_number_before = len(user_list_test)
        user_number_after = 42
        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        sut.set_users_number(42)

        self.assertNotEqual(user_number_before, user_number_after)
        self.assertEqual(sut.get_users_number(), user_number_after)

    def test_set_groups_list(self) -> None:
        """
        Test method to test the setter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]
        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        group_list_before = sut.get_groups_list()
        group_list_after = []
        for group in group_list_before:
            group_list_after.append(group)

        group_list_after.append(Group(42))
        sut.set_groups_list(group_list_after)

        print(len(group_list_before), len(group_list_after))
        self.assertNotEqual(group_list_before, group_list_after)
        self.assertEqual(len(group_list_before) + 1, len(group_list_after))

    def test_set_number_of_groups(self) -> None:
        """
        Test method to test the setter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")
        number_of_groups_before = sut.get_number_of_groups()
        sut.set_number_of_groups(42)
        number_of_groups_after = sut.get_number_of_groups()

        sut.set_users_number(42)

        self.assertNotEqual(number_of_groups_before, number_of_groups_after)
        self.assertEqual(number_of_groups_after, 42)

    def test_display_group_info(self) -> None:
        """
        Test method to test the setter
        """
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")

        with self.assertLogs(level='INFO') as log:
            sut.display_group_info()
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn("Groups size", log.output[0])

    def test_add_to_group(self) -> None:
        """
        Test method to test the setter
        """
        user_to_add = User("Quentin")
        group_to_be_added_to = Group(2)
        user_list_test = [User("Frédo"), User("Quentin"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin"), User("David"), User("David"),
                          User("Marion"), User("Isshia"), User("Damien"),
                          User("Quentin")]

        sut = GroupGenerator(user_list_test, 8, "LAST_MAX")
        number_of_groups_before = sut.get_number_of_groups()
        sut.set_number_of_groups(42)
        number_of_groups_after = sut.get_number_of_groups()

        sut.set_users_number(42)

        self.assertNotEqual(number_of_groups_before, number_of_groups_after)
        self.assertEqual(number_of_groups_after, 42)

    # endregion
