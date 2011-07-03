import re, sys, os

__metaclass__ = type

class WebMakeFileBundle:
	""" 
	Class WebMakeFileBundle, just a container for info about a set of files that we want to build together.
	Author tom@0x101.com
	"""

	__files = []

	__outputName = ''

	__rawContent = ''

	def __init__(self, files = [], outputName = ''):
		self.__files = files
		self.__outputName = outputName

	def getFiles(self):
		return self.__files

	def getOutputName(self):
		return self.__outputName

	def isJavascript(self):
		isJs = False
		# TODO: Improve the regular expression
		if re.search('.js$', self.__outputName):
			isJs = True
		return isJs	
	
	def readContent(self, fileIndex = 0):
		fileName = self.__files[fileIndex]
		inputFile = open(fileName, 'r')
		content = inputFile.read()
		inputFile.close()
		return content
	
	def addRawContent(self, rawContent):
		self.__rawContent = self.__rawContent + rawContent

	def build(self):
		outputFile = open(self.__outputName, 'w')
		outputFile.write(self.__rawContent)
		outputFile.close()
	
	def setRawContent(self, content):
		self.__rawContent = content

	def getRawContent(self):
		return self.__rawContent
