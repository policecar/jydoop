"""Reduce file size by removing dispensable fields."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jydoop
import jsonfileutils
import re
import os

setupjob = jsonfileutils.setupjob

def map( key, value, context ):

    # input ( description, example ): 
    # head_word \t n-gram \t total_count \t year,count tuples
    # foundations     theoretical/JJ/amod/2 foundations/NNS/conj/0 of/IN/prep/2 education/NN/pobj/3   11
    #      1984,2  1990,1  1993,1  1997,1  2001,4  2003,1  2006,1

    # split value by tab delimiter and preserve only the first three items
    j = value.split( '\t' )[:3]

    # output ( description, example ):
    # head_word \t n-gram , count
    # foundations     theoretical/JJ/amod/2 foundations/NNS/conj/0 of/IN/prep/2 education/NN/pobj/3,11
    context.write( '\t'.join( j[:2] ), int( j[2] ))


def skip_local_output():
    return True
