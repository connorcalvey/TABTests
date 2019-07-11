# Installing Printer and driver

print "Installing INKBOT Printer"
os.system('sudo curl -o /Library/Printers/PPDs.zip https://s3-eu-west-1.amazonaws.com/it-services/XeroxC8055Script/PPDs.zip')
os.system('sudo curl -o /Library/Printers/Xerox.zip https://s3-eu-west-1.amazonaws.com/it-services/XeroxC8055Script/Xerox.zip')
os.system('sudo unzip /Library/Printers/PPDs.zip')
os.system('sudo unzip /Library/Printers/Xerox.zip -d /Library/Printers/')
os.system('sudo curl -o /Library/Printers/PPDs/Contents/Resources/Xerox\ AltaLink\ C8055.gz https://s3-eu-west-1.amazonaws.com/it-services/Backgrounds/Xerox+AltaLink+C8055.gz')
os.system('lpadmin -p INKBOT -L "2nd Floor, The Spitfire Building" -E -v ipp://10.2.0.24 -o printer-is-shared=“False”  -P /Library/Printers/PPDs/Contents/Resources/Xerox\ AltaLink\ C8055.gz')
