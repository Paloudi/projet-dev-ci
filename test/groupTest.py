import unittest

from model.group import Group
from model.user import User


class MyTestCase(unittest.TestCase):

	def testGroupCreation(self):
		sut = Group(10)
		self.assertIsInstance(sut, Group)

	def testGroupAddUser(self):
		user = User("test")
		sut = Group(1)
		sut.addUser(user)
		self.assertEqual(user, sut.getUsers()[0])

	def testGroupAddTooManyUsers(self):
		groupSize = 5
		sut = Group(groupSize)
		for i in range(0, 10):
			sut.addUser(User("test"+str(i)))
		self.assertEqual(groupSize, len(sut.getUsers()))

	def testGroupAddNullUser(self):
		user = None
		sut = Group(1)
		sut.addUser(user)
		self.assertEqual(0, len(sut.getUsers()))

	def testGroupNegativeSize(self):
		with self.assertRaises(ValueError):
			sut = Group(-10)


if __name__ == '__main__':
	unittest.main()
