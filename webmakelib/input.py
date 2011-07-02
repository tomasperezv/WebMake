import sys, os, json
from filebundle import WebMakeFileBundle

__metaclass__ = type

class WebMakeInput: 
	""" 
	Class WebMakeInput, parses the JSON config of the project.
	Author tom@0x101.com
	"""
	__bundles = []

	__optimization = ''

	__jsonConfig = ''

	__path = ''

	__jsonInput = None

	def __init__(self, filename):
		self.__jsonConfig = self.__readJSONConfig(filename)
		self.__initializeJson()

	def __readJSONConfig(self, filename):
		self.__path = os.path.dirname(filename)

		# Read the JSON Config file and instantiate an input manager
		inputFile = open(filename, 'r')
		jsonConfig = inputFile.read()
		inputFile.close()

		return jsonConfig

	def __initializeJson(self):
		# Parse the json, generate the bundles information and optimization
		# TODO: Implement error handling
		self.__jsonInput = json.loads(self.__jsonConfig)
		self.__optimization = self.__jsonInput['optimization']
		for fileBundle in self.__jsonInput['bundles']:
			self.__bundles.append(WebMakeFileBundle(fileBundle['files'], fileBundle['output']))

	def getPath(self): 
		return self.__path

	def getFileBundles(self): 
		return self.__bundles

	def getOptimization(self): 
		return self.__optimization

	def getJsonInput(self): 
		return self.__jsonInput

	def getInputString(self):
		return self.__inputString

