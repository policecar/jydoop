"""Write text snippets to separate files."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from IPython import embed
except ImportError:
    pass

import jydoop
import re
import os
from config import LOCAL_OUTPUT_PATH

setupjob = jydoop.setupjob
combine  = jydoop.sumreducer
reduce   = jydoop.sumreducer

def map( key, value, context ):

    # input ( description, example ): 
    # head_word \t n-gram , count
    # argument        misplaced/NNP/nn/2 argument/NNP/pobj/0,19

    j      = key.split( '\t' )
    head   = j[0]
    tokens = j[1].split( ' ' )
    text   = ' '.join([ t.split( '/' )[0] for t in tokens ])

    # output: head_word \t text , count
    context.write( '\t'.join([ head, text ]), value )


# if no local output desired, uncomment this method
# def skip_local_output():
#     return True

# else specify how to write output to file
def output( path, results ):
    path = os.path.join( LOCAL_OUTPUT_PATH, 'text_snippets.out' )
    f = open(path, 'w')
    for k,v in results:
        f.write( "%s\t%s\n" % ( k, v ))
    f.close()
