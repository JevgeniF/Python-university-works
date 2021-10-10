OstaGrabber.

The script grabs listings from categories on Osta.ee web.

You will be notified about the end of parsing and data grabbing by the 
following message in Terminal/Command Line:
"All data saved. No more pages left."

The received data (Titles, Prices and Links to pictures) saved to osta.json 
file in the default script folder after the end of procedure.

The start_url consist of two variables.
This was done to simplify switching between categories, in case of we want to
grab data from other than the default (Arvutid) category.

main = 'https://www.osta.ee/'
category = 'kategooria/arvutid'

This feature is experemental and needs more testing.

Created as Homework 4 for ICS0019 course
by Jevgeni Fenko
jevgeni.fenko@taltech.ee
200810IADB