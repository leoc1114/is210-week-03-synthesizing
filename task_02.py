#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = inquisition.SPANISH

A = SPANISH.index('Spanish')

B = len(SPANISH)

FLEMISH = SPANISH[0:19] + 'Flemish ' + SPANISH[27:418]
