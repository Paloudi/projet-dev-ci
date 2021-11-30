#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class User:

	def __init__(self, name) -> None:
		super().__init__()
		if name and isinstance(name, str):
			self.__name = name

