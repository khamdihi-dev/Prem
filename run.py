#!/usr/bin/env python
# -*- coding: utf-8

try:
    from asset import run as xyz
except Exception as Error:
    exit('\nErorr Module Or File: {}'.format(Error))

try:
    xyz.AssetAndKey()
except Exception as Error:
    exit('\nErorr Running: {}'.format(Error))
