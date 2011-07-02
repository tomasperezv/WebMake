#!/usr/bin/python2.6

'''
 WebMake
	A simple and easy to use static files builder, for web projects
	 Author tom@0x101.com
'''

from webmakelib.input import WebMakeInput
from webmakelib.closure import WebMakeClosure
import sys, os, datetime

if len(sys.argv) < 2:
	print 'Invalid params provided: webmake.py [path to json config file]'
	exit()

webMakeInput = WebMakeInput(sys.argv[1])
os.chdir(webMakeInput.getPath())

initTime = datetime.datetime.now()

# Process each bundle
for fileBundle in webMakeInput.getFileBundles():
	# Initialize the raw content
	merge = ''
	for i in range(len(fileBundle.getFiles())):
		closure = WebMakeClosure(webMakeInput.getOptimization())
		if fileBundle.isJavascript():
			# Apply the closure compiler
			fileBundle.addRawContent(closure.compileString(fileBundle.readContent(i)))
		else:
			# Just merge the files
			fileBundle.addRawContent(fileBundle.readContent(i))
	# Generate the output for the current file bundle
	print 'building ' + fileBundle.getOutputName()
	fileBundle.build()

timeDelta = datetime.datetime.now() - initTime
print 'Process complete, it took ' + str(timeDelta.total_seconds()) + ' seconds.'
