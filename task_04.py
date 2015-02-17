#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'


FNAME = 'Pat'
NEWS = NEWS.replace('{friend}', 'Pat')

NTYPE = '*amazing*'
NEWS = NEWS.replace('{0}', ' *amazing* ')

RNUM = 42
NEWS = NEWS.replace('{1}', '000042')

EMAIL = NEWS



print EMAIL
