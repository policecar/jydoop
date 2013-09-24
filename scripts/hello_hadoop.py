"""First test script for MIA's hadoop cluster."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import simplejson as json
except ImportError:
    import json

import jydoop
import jsonfileutils
import re
import os


# specify how data is made available to the 
# job script and process incoming arguments
setupjob = jsonfileutils.setupjob


# called once for each input record
def map( key, value, context ):

    j = json.loads( value )
    sentence  = j['sentence'].encode( 'ascii', 'ignore' )

    # write result of map(...)
    context.write( sentence, 1 )


# utterly optional ^^
combine = jydoop.sumreducer
# def combine( key, values, context ):


# called once for each key
reduce = jydoop.sumreducer
# def reduce( key, values, context ):


# keep the output in HDFS instead of saving locally; will also
# prevent data from being deleted from HDFS after job completion
def skip_local_output():
    return True

# customize this method for local output
# ( make sure skip_local_output returns False )
def output( path, results ):
    path = './local_output/hello.out'
    f = open( path, 'w' )
    for k,v in results:
        f.write( "%s\t%s\n" % ( k, v ))
    f.close()

