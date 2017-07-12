from __future__ import print_function, division
import os
import matplotlib.pyplot as plt
import numpy as np
import argparse
from astropy import log
from os import path
from glob import glob
from subprocess import check_call
import shutil
import tempfile
from astropy.table import Table

from nicer.values import *

def runcmd(cmd):
    # CMD should be a list of strings since it is not processed by a shell
    log.info('CMD: '+" ".join(cmd))
    check_call(cmd,env=os.environ)

def filtandmerge(evfiles,workdir=None):
    'Merges and filters a set of event files, returning an etable'

    tmpdir = tempfile.mkdtemp(dir=workdir)

    # Build input file for ftmerge
    evlistname=path.join(tmpdir,'evfiles.txt')
    fout = file(evlistname,'w')
    evfilt_expr = '(PI>30).and.(EVENT_FLAGS==bx1x000)'
    for en in evfiles:
        print('{0}[{1}]'.format(en,evfilt_expr),file=fout)
    fout.close()

    # Run ftmerge
    mergedname = path.join(tmpdir,"merged.evt")
    cmd = ["ftmerge", "@{0}".format(evlistname), "outfile={0}".format(mergedname),
        "clobber=yes"]
    runcmd(cmd)

    # Read merged event FITS file into a Table
    etable = Table.read(mergedname,hdu=1)

    # Clean up
    os.remove(evlistname)
    os.remove(mergedname)
    os.rmdir(tmpdir)

    return etable
