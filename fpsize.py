# Get size and add to comment header of all parts

import os, glob, datetime

# collect a list of all module names

fplibdir = "/home/wicker/wickerlib/libraries/Wickerlib.pretty/"
modules = glob.glob(fplibdir+'*.kicad_mod')
modules = sorted(modules)

fp_list = []

for m in modules:

  print(m)

  x = []
  y = []
  mod_file = []
  no_calc = False

  # read in the file
  with open(m, 'r') as f:

    for line in f:
      mod_file.append(line)

  # get the values
  for line in mod_file:

    if 'F.Fab' in line:
      if 'end' in line:
        line = line.split(' ')
        x.append(float(line[4]))
        x.append(float(line[7]))
        y.append(float(line[5].replace(')','')))
        y.append(float(line[8].replace(')','')))

    if 'attr virtual' in line:
      no_calc = True

  if no_calc:
    x_size_mils = 0
    y_size_mils = 0
  else:
    # find biggest and smallest x to calculate x_size in mils
    x_min = min(x)
    x_max = max(x)
    x_size_mm = x_max - x_min
    x_size_mils = x_size_mm * 39.3700787401575
    x_size_mils = "{0:.0f}".format(x_size_mils)

    # find biggest and smallest y to calculate y_size in mils
    y_min = min(y)
    y_max = max(y)
    y_size_mm = y_max - y_min
    y_size_mils = y_size_mm * 39.3700787401575
    y_size_mils = "{0:.0f}".format(y_size_mils)

    print(x_size_mils, y_size_mils)

  # write out to the file
  with open(m, 'w') as f:
    for line in mod_file:
      if 'Fab_XSize' in line:
        f.write('# Fab_XSize_mils: '+str(x_size_mils)+'\n')
      elif 'Fab_YSize' in line:
        f.write('# Fab_YSize_mils: '+str(y_size_mils)+'\n')
      else:
        f.write(line)


#for fp in modules:
#  fp = fp.replace("/home/wicker/wickerlib/libraries/Wickerlib.pretty/","")
#  fp = fp.replace(".kicad_mod","")
#  fp_list.append(fp)
#  #print fp
#
## collect a list of all the symbol names
#
#symlibfile = "/home/wicker/wickerlib/libraries/wickerlib.lib"
#symlist = []
#
#with open(symlibfile, 'r') as symfile:
#  for line in  symfile:
#    line = line.split(' ')
#    if 'DEF' == line[0]:
#      m_def = ''
#      m_fp = ''
#      m_def = line[1]
#    if 'F2' in line[0]:
#      m_fp = line[1].replace("\"","")
#      if 'UNDEFINED' in m_fp:
#        print m_def
#
