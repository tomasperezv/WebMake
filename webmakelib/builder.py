import threading
from closure import WebMakeClosure

__metaclass__ = type

class WebMakeBuilder(threading.Thread): 
	""" 
	Class WebMakeBuilder, processing the file bundles as a separated thread, getting a better performance as
	some of the build process requires to make a network request to the Closure compiler API.
	Author tom@0x101.com
	"""
	__fileBundle = None

	__optimization = ''

	def __init__(self, fileBundle, optimization):
		self.__fileBundle = fileBundle
		self.__optimization = optimization
		threading.Thread.__init__(self)

	def run(self):
		print 'building ' + self.__fileBundle.getOutputName()
		for i in range(len(self.__fileBundle.getFiles())):
			closure = WebMakeClosure(self.__optimization)
			content = self.__fileBundle.readContent(i)
			if self.__fileBundle.isJavascript():
				# Apply the closure compiler
				self.__fileBundle.addRawContent(closure.compileString(content))
			else:
				# Just merge the files
				self.__fileBundle.addRawContent(content)
		# Generate the output for the current file bundle
		self.__fileBundle.build()
