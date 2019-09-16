psrpipe
=======

Description
^^^^^^^^^^^

Pipeline process NICER data.

Output will be written in current working directory in directories that end in '_pipe'.

Several diagnostic plots are produced, and the following data processing steps are run:

* Select good times according to the following:

  * (ANG_DIST.lt.0.015).and.(ELV>30.0)

  * (MODE.eq.1).and.(SUBMODE_AZ.eq.2).and.(SUBMODE_EL.eq.2)

  * SAT_LAT, SAT_LONG not in SAA or polar horn regions specified by region files

  * If --dark is specified then also filter on SUNSHINE.eq.0

Optionally, you can filter on overshoot rate or rate of bad ratio events

* Select events according to:

  * EVENT_FLAGS=bx1x000 (SLOW-only or SLOW+FAST events)

  * PI in the specified range (default is 0.25-12.0 keV)

  * Remove events from any DET_ID specified by the --mask parameter

 The final output is 'cleanfilt.evt' and extracted PHA and lightcurve FITS

 files produced by extrator. The event file will have a PULSE_PHASE column

 computed using PINT if the --par file is specified on the command line.
