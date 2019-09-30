nicer package
=============

Submodules
----------

nicer.NicerFileSet module
-------------------------

.. automodule:: nicer.NicerFileSet
   :members:
   :undoc-members:
   :show-inheritance:

nicer.bkg\_plots module
-----------------------
Contains a single function that uses the plotutils.py module to produce various
background plots.

First Plot: Multiplies the 'NUM_FPM_ON' and 'FPM_RATIO_REJ_COUNT' columns of
the provided .mkf file, producing the total number of counts rejected by 
PI_RATIO, then plots this during good time intervals.

PI_RATIO is a cut to reduce the number of particle events, and can be read
about in more detail on NASA's NICER mission guide page.

'NUM_FPM_ON' - Number of FPMs enabled for science
'FPM_RATIO_REJ_COUNT' - the rate of events that would be selected by the simple
cut (PI > 300 && PI_RATIO > 1.53). These are nominally background which would
be rejected by the so-called trumpet cut by nicerclean. This is the average 
count rate of ratio-rejected events per enabled FPM.

Thus, multiplying these two values gives the total number of events rejected
by NICER.

Second Plot: Plots the total count rate of over counts via multiplying the
'NUM_FPM_ON' and 'FPM_OVERONLY_COUNT' columns of the provided .mkf file.

'FPM_OVERONLY_COUNT' - the average count rate of over counts per enabled FPM.

Third Plot: Shows when NICER was in the SAA. The magnitude of this plot is set
to be the maximum value of the total count rate of over counts, during the time
in which NICER was in the SAA.

Fourth Plot: Plots the total count rate of over counts via multiplying the
'NUM_FPM_ON' and 'FPM_UNDERONLY_COUNT' columns of the provided .mkf file.

Fifth Plot: Plots the 'SUN_ANGLE', 'BR_EARTH', 'MOON_ANGLE', and 'ELV' columns
of the provided .mkf file over time, during good time intervals.

'SUN_ANGLE' - angle between pointing and sun vector
'BR_EARTH' - angle between pointing and bright earth
'MOON_ANGLE' - angle between pointing and moon vector
'ELV' - angle between pointing and earth limb

Sixth Plot: Plots the 'ANG_DIST' column of the provided .mkf file over time,
during good time intervals. 

'ANG_DIST' - angular distance of pointing from nominal

Seventh Plot: Plots the 'COR_SAX' column of the provided .mkf file over time,
during good time intervals. 

'COR_SAX' - magnetic cut off rigidity (IGRF map)

Eighth Plot: Plots a light curve (c/s) for each GTI.

.. automodule:: nicer.bkg_plots
   :members:
   :undoc-members:
   :show-inheritance:

nicer.cartographer module
-------------------------

.. automodule:: nicer.cartographer
   :members:
   :undoc-members:
   :show-inheritance:

nicer.eng\_plots module
-----------------------

.. automodule:: nicer.eng_plots
   :members:
   :undoc-members:
   :show-inheritance:

nicer.fitsutils module
----------------------

.. automodule:: nicer.fitsutils
   :members:
   :undoc-members:
   :show-inheritance:

nicer.latloninterp module
-------------------------

.. automodule:: nicer.latloninterp
   :members:
   :undoc-members:
   :show-inheritance:

nicer.mcc module
----------------

.. automodule:: nicer.mcc
   :members:
   :undoc-members:
   :show-inheritance:

nicer.plotutils module
----------------------

.. automodule:: nicer.plotutils
   :members:
   :undoc-members:
   :show-inheritance:

nicer.sci\_plots module
-----------------------

.. automodule:: nicer.sci_plots
   :members:
   :undoc-members:
   :show-inheritance:

nicer.sps module
----------------

.. automodule:: nicer.sps
   :members:
   :undoc-members:
   :show-inheritance:

nicer.values module
-------------------

.. automodule:: nicer.values
   :members:
   :undoc-members:
   :show-inheritance:

nicer.yday\_custom module
-------------------------

.. automodule:: nicer.yday_custom
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: nicer
   :members:
   :undoc-members:
   :show-inheritance:
