"""
Simple utility module to open "explorer" file dialogs.
The name "explorer" comes from the windows file explorer, which is called explorer.
"""
__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import sys
import os
import subprocess

def hasExplorer():
	"""Check if we have support for opening file dialog windows."""
	return True

def openExplorer(filename):
	"""Open an file dialog window in the directory of a file, and select the file."""
	if sys.platform == 'win32' or sys.platform == 'cygwin':
		subprocess.Popen(r'explorer /select,"%s"' % (filename))
	if sys.platform == 'darwin':
		subprocess.Popen(['open', '-R', filename])
	if sys.platform.startswith('linux'):
		subprocess.Popen(['xdg-open', os.path.split(filename)[0]])

def openExplorerPath(filename):
	"""Open a file dialog inside a directory, without selecting any file."""
	if sys.platform == 'win32' or sys.platform == 'cygwin':
		subprocess.Popen(r'explorer "%s"' % (filename))
	if sys.platform == 'darwin':
		subprocess.Popen(['open', filename])
	if sys.platform.startswith('linux'):
		subprocess.Popen(['xdg-open', filename])

