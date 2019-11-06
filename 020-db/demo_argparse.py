import argparse

## komplexere Parameteruebergabe zB mit
## https://pypi.python.org/pypi/ConfigArgParse
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--inputfile',
  action="store", dest="inputfile",
  help="inputfile to be parsed")

parser.add_argument('-d', '--debug',
  help="debug")

options = parser.parse_args()
print ('Input File', options.inputfile)
