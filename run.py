#!/usr/bin/env python
# -*- coding: utf-8

try:
    from asset import Prem_enc as Yxz
except Exception as Error:
    exit('\nErorr Module Or File: {}'.format(Error))

try:
    _ = Yxz()
    _.AssetAndKey()
except Exception as Error:
    exit('\nErorr Running: {}'.format(Error))

