#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

from model.user import User


class Group:

	def __init__(self, size: int) -> None:
		super().__init__()
		if size and isinstance(size, int) and size > 0:
			self.__size = size
			self.__users: List[User] = []
		else:
			raise ValueError("size parameter is invalid")

	def addUser(self, newUser: User) -> None:
		if newUser and isinstance(newUser, User):
			if self.__size > len(self.__users):
				self.__users.append(newUser)

	# region Getters

	def getUsers(self) -> List[User]:
		return self.__users

	# endregion
