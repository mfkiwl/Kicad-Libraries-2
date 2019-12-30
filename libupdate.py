# Add size and type to all parts

import os, glob, datetime

# collect a list of all module names

fplibdir = "/home/wicker/wickerlib/libraries/Wickerlib.pretty/"
modules = glob.glob(fplibdir+'*.kicad_mod')
modules = sorted(modules)

fp_list = []

for m in modules:

  xsize_mils = 0
  ysize_mil = 0
  modtype = ''
  title = ''
  mod_file = []

  title = m.split('/')[6].replace('.kicad_mod','')

  # read in the file
  with open(m, 'r') as f:

    for line in f:
      if 'Fab_XSize' in line:
        x_size_mils = line.split(' ')[2].replace('\n','')
      elif 'Fab_YSize' in line:
        y_size_mils = line.split(' ')[2].replace('\n','')
      elif '(attr' in line:
        modtype = line.split(' ')[3].replace(')\n','')

  print(title, x_size_mils, y_size_mils, modtype)

  fp = {'title':title,
       'xsize':x_size_mils,
       'ysize':y_size_mils,
       'type':modtype
      }

  fp_list.append(fp)

# create footprint list
for fp in fp_list:
  print(fp)

# read in the library file
symlibfilepath = "/home/wicker/wickerlib/libraries/wickerlib.lib2"
symlibfile = []

with open(symlibfilepath, 'r') as f:
  for line in f:
    symlibfile.append(line)

with open(symlibfilepath, 'w') as f:
  for line in symlibfile:

    # For each symbol, get the package from F2
    # F2 "Wickerlib:LED-RGB-5050-SMD" 0 -350 50 H I C CIN
    if 'F2 ' in line:
      package = line.split(' ')[1].replace('"Wickerlib:','').replace('"','')
      f.write(line)

    elif 'F8 ' in line:

      for fp in fp_list:
        if fp['title'] == package:
          curr_fp = fp
          f.write(line)
          f.write('F9 "'+curr_fp['xsize']+'" 0 -350 50 H I C CIN "XSize_mils"\n')
          f.write('F10 "'+curr_fp['ysize']+'" 0 -350 50 H I C CIN "YSize_mils"\n')
          f.write('F11 "'+curr_fp['type']+'" 0 -350 50 H I C CIN "Type"\n')

    else:
      f.write(line)

exit()



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
