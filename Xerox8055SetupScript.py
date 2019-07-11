#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib
import urllib2
import subprocess
import shlex

name = ''
email = ''
assettag = ''


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "**************************************************************"
  print "Install the XCode Command Line Tools and run this script again"
  print "**************************************************************"
  exit()

# Installing Printer and driver

print "Installing INKBOT Printer"
os.system('sudo curl -o /Library/Printers/PPDs.zip https://s3-eu-west-1.amazonaws.com/it-services/XeroxC8055Script/PPDs.zip')
os.system('sudo curl -o /Library/Printers/Xerox.zip https://s3-eu-west-1.amazonaws.com/it-services/XeroxC8055Script/Xerox.zip')
os.system('sudo unzip /Library/Printers/PPDs.zip')
os.system('sudo unzip /Library/Printers/Xerox.zip -d /Library/Printers/')
os.system('sudo curl -o /Library/Printers/PPDs/Contents/Resources/Xerox\ AltaLink\ C8055.gz https://s3-eu-west-1.amazonaws.com/it-services/Backgrounds/Xerox+AltaLink+C8055.gz')
os.system('lpadmin -p OfficePrinter -L "2nd Floor, The Spitfire Building" -E -v ipp://10.5.0.10 -o printer-is-shared=“False”  -P /Library/Printers/PPDs/Contents/Resources/Xerox\ AltaLink\ C8055.gz')
