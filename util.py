#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
cnvd_id
release_time
harzard_level
influence_product
description
reference
solution
discoverer
patch
'''

def cnvd_id(td):
    return td.text.strip()

def release_time(td):
    return td.text.strip()

def harzard_level(td):
    return td.text.strip().replace('\t', '').replace('\r\n', '')

def influence_product(td):
    return td.text.strip().replace('\t', '').replace('\r\n\r\n', '\r\n')

def description(td):
    return td.text.strip().replace('\t', '')

def reference(td):
    return td.text.strip()

def solution(td):
    return td.text.strip().replace('\t', '')

def discoverer(td):
    return td.text.strip()

def patch(td):
    return td.text.strip()




