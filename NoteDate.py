# Project Name: NoteDate
# Author: Patrick J. Connant
# Creation Date: 01/09/2013
# Platform: Sublime Text 3
# Description: My first Sublime Text 2 Plug-in.  Adds a dated dividing line for
#                               my personal note system
#
#------------------------------------------------------------------------------
# Modified: Patrick J. Conant
# Modified Date: 02/13/2013
# Description: Made Python 3 updates for new code base
#------------------------------------------------------------------------------
#

import sublime, sublime_plugin
import datetime

#Spaces to Create 80 char line with 10 char date
SPACE_NUMBER = 35

class notedateCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                # Loop over all selections
                for line in self.view.sel():
                        self.InsertLine(edit, line)

        # InsertLine - ARGS: Edit and Cursor Location
        def InsertLine(self,edit,cursorloc):
                # Get Current Line
                line = self.view.line(cursorloc) # Get Current line

                # Spacer
                self.view.insert(edit, line.begin(), "-" * SPACE_NUMBER)

                # Date formated as mm/dd/yyyy
                today = datetime.date.today()
                self.view.insert(edit,line.begin(), today.strftime("%m/%d/%Y"))
                

                #Spacer
                self.view.insert(edit, line.begin(), "-" * SPACE_NUMBER)
