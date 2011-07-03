#!/usr/bin/python2.6

'''
 WebMake
	A simple and easy to use static files builder, for web projects
	 Author tom@0x101.com
'''
from webmakelib.input import WebMakeInput
from webmakelib.builder import WebMakeBuilder
import sys, os, datetime, threading

if len(sys.argv) < 2:
	print 'Invalid params provided: webmake.py [path to json config file]'
	exit()

webMakeInput = WebMakeInput(sys.argv[1])
os.chdir(webMakeInput.getPath())

initTime = datetime.datetime.now()

# Process each bundle
for fileBundle in webMakeInput.getFileBundles():
	# Initialize and start the builder as a new thread
	webMakeBuilder = WebMakeBuilder(fileBundle, webMakeInput.getOptimization())
	webMakeBuilder.start()

# Wait until the threads are finished
for thread in threading.enumerate():
	if thread is not threading.currentThread():
		thread.join()

timeDelta = datetime.datetime.now() - initTime
print 'Process complete, it took ' + str(timeDelta.total_seconds()) + ' seconds.'
