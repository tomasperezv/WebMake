import httplib, urllib, sys, os

__metaclass__ = type

class WebMakeClosure: 
	""" 
	Class WebMakeClosure, a wrapper for the Google's Closure Compile API. Which applies minimization and structure improvements to Javascript files.
	Author tom@0x101.com
	"""
	__optimization = 'WHITESPACE_ONLY'

	__headers = { "Content-type": "application/x-www-form-urlencoded" }

	def __init__(self, optimization = 'WHITESPACE_ONLY'):
		self.__optimization = optimization

	def compileString(self, codeString):
		params = self.__getParams(codeString)
		conn = self.__getConnection(params)
		response = conn.getresponse()
		data = response.read()
		conn.close
		return data

	def __getParams(self, codeString):
		''' 
		@see http://code.google.com/closure/compiler/docs/api-ref.html

		Example of values:

		compilation level: WHITESPACE_ONLY | SIMPLE_OPTIMIZATIONS | ADVANCED_OPTIMIZATIONS
		output format: test, json, xml
		output info: compiled_code | warnings | errors | statistics
		'''
		return urllib.urlencode([
			('js_code', codeString),
			('compilation_level', 'WHITESPACE_ONLY'),
			('output_format', 'text'),
			#('output_info', 'statistics'),
			('output_info', 'compiled_code'),
		])

	def __getConnection(self, params):
		conn = httplib.HTTPConnection('closure-compiler.appspot.com')
		conn.request('POST', '/compile', params, self.__headers)
		return conn
