# Scan all parts and build a Markdown table list
# Create a README file in the footprint library directory
# Table looks like this:
# |Footprint|Verified|

import os, glob, datetime

# collect a list of all module names

fplibdir = "/home/wicker/wickerlib/libraries/Wickerlib.pretty/"
modules = glob.glob(fplibdir+'*.kicad_mod')
modules = sorted(modules)

fp_list = []

for fp in modules:
  fp = fp.replace("/home/wicker/wickerlib/libraries/Wickerlib.pretty/","")
  fp = fp.replace(".kicad_mod","")
  fp_list.append(fp)
  #print fp

# collect a list of all the symbol names

symlibfile = "/home/wicker/wickerlib/libraries/wickerlib.lib"
symlist = []

with open(symlibfile, 'r') as symfile:
  for line in  symfile: 
    line = line.split(' ')
    if 'DEF' == line[0]:
      m_def = '' 
      m_fp = ''
      m_def = line[1]
    if 'F2' in line[0]:
      m_fp = line[1].replace("\"","")
      if 'UNDEFINED' in m_fp:
        print m_def
    
