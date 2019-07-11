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

  
# Download TAB files
os.system('sudo mkdir /Library/TAB')
# TAB icon
os.system('sudo curl -o /Library/TAB/tab-icon.png https://it-services.s3-eu-west-1.amazonaws.com/TeamCity+Script+Resources/TAB_600x600.png')
os.system('sudo curl -o /Library/TAB/teamcity-icon.png https://it-services.s3-eu-west-1.amazonaws.com/TeamCity+Script+Resources/teamcity-icon-logo-png-transparent.png')
os.system('sudo curl -o /Library/TAB/tab-background.png https://it-services.s3-eu-west-1.amazonaws.com/TeamCity+Script+Resources/tab-background.png')

# Sudo: Spectacle, ZSH, OSX Settings
print "\n\nWelcome to the Mac Setup Script by TAB\n"

os.system('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "/Library/TAB/tab-background.png"\'')

# Basic Info
while name == '':
  name = 'TeamCity'

#while email == '' or '@' not in email:
#  email = raw_input("What's your email?\n").strip()
  
while assettag ==  '' or 'tc-agent' not in assettag:
  assettag = raw_input("Please enter the name of the TeamCity Agent.\n").strip()


def show_notification(text):
  os.system('osascript -e \'display notification "'+ text +'" with title "Mac Setup"\' > /dev/null')
  
#urllib.urlretrieve("https://raw.githubusercontent.com/sampiper/macos-create-user/master/create-user.sh", "create-user.sh")
#os.system('chmod +x create-user.sh')
#subprocess.call(shlex.split('sudo ./create-user.sh "' + name + '" AlwaysTesting! ' + name.replace(' ', '')))



# Create user account
os.system('sysadminctl interactive -addUser ' + name.replace(' ', '').lower() + ' -fullName "' + name + '" -password "AlwaysTesting!" -admin -picture /Library/TAB/tab-icon.png')
# Hide TAB Admin account
os.system('sudo dscl . create /Users/tabadmin IsHidden 1')

print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Set computer name info (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName assettag)
os.system('sudo scutil --set HostName assettag)
os.system('sudo scutil --set LocalHostName assettag) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string assettag)

show_notification("Laptop name: "assettag(' ', ''))

# Change User Icons 

os.system('sudo /usr/bin/dscl . delete /Users/teamcity JPEGPhoto')
os.system('sudo /usr/bin/dscl . create /Users/teamcity Picture "Library/TAB/teamcity-icon.png"')
os.system('sudo /usr/bin/dscl . delete /Users/tabadmin JPEGPhoto')
os.system('sudo /usr/bin/dscl . create /Users/tabadmin Picture "Library/TAB/tab-icon.png"')

# Enabling Remote Login, Remote Management and Remote Apple Events

os.system('sudo systemsetup -setremotelogin on')
os.system('sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -access -on -users admin -privs -all -restart -agent -menu')
os.system('sudo systemsetup -setremoteappleevents on')







