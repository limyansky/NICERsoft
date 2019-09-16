nipointing
========

Description
^^^^^^^^^^^

Calculate the optimal (offset) pointing that maximizes the S/N for the target by
minimizing the contamination from nearby targets. Possibility to use SIMBAD 
coordinates for the source (with exact name). Information about nearby sources 
must be provided in a text file with 3 columns (RA, DEC, and estimated NICER 
count-rate).  Sources within 7 or 8 arcmin should be considered. SIMBAD Queries
require package 'astroquery'.
