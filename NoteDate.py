# Project Name: NoteDate
# Author: Patrick J. Connant
# Creation Date: 01/09/2013
# Platform: Sublime Text 2
# Description: My first Sublime Text 2 Plug-in.  Adds a dated dividing line for
#				my personal note system
#
#------------------------------------------------------------------------------
# Modified:
# Modified Date:
# Description:
#------------------------------------------------------------------------------
#

import sublime, sublime_plugin
import datetime

class notedateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		intSpaceNum = 35 #Spaces to Create 80 char line

		# Get Current Line
                line = self.view.line(self.view.sel()[0]) # Get Current line 

                # Spacer 
                self.view.insert(edit, line.begin(), "-" * intSpaceNum)

		# Date formated as mm/dd/yyyy
                today = datetime.date.today()
		self.view.insert(edit,line.begin(), today.strftime("%m/%d/%Y"))

                #Spacer 
                self.view.insert(edit, line.begin(), "-" * intSpaceNum)	