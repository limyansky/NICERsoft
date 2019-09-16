merge
========

Description
^^^^^^^^^^^

Merging NICER ObsID or event files.

Output will be written in merged directory. This script assumes that all 
filtering has been done.

Output files include:

* merged event file with it science plot (nicerql.py)

* merged lightcurve produced by extrator

* merged spectrum PHA produced by extrator

The PULSE_PHASE column will be ignored for the nicerql.py plot, since it 
requires a merged orbit file -- not implemented yet.
