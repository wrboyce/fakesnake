import random

class Faker(object):
	def __getattr__(self, key):
		mod = __import__(key, (), {}, ('fakesnake',), -1)
		return getattr(mod, key.title())()
	
	@staticmethod
	def _parse(s):
		s = ''.join(map(lambda c: c.replace('#', str(random.randint(0,9))), s))
		s = ''.join(map(lambda c: c.replace('?', chr(random.randint(65,90))), s))
		return '\n'.join(l.strip() for l in s.split('\n'))

class FakeLib(object):
	""" WARNING: This code may make your eyes bleed. """
	random = random.choice
	class NoNamedFormats(Exception): pass

	def _get(self, key, default=''):
		""" Shortcut to super(FakeLib, self).__getattribute__(key) """
		try:
			return super(FakeLib, self).__getattribute__(key)
		except AttributeError:
			if default != '':
				return default
			raise

	def _getattr(self, key, default=''):
		""" Shortcut to Fakelib.__getattr__(s,k), with an optional default value. """
		try:
			return getattr(self, key)
		except AttributeError:
			if default != '':
				return default
			raise

	def __getattr__(self, key):
		try:
			# find the private/plural variable (name => _names) and select a random element
			res = self.random(object.__getattribute__(self, '_%ss' % key))
		except AttributeError, e:
			raise AttributeError(str(e).replace('_%ss' % key, key))
		if type(res) == tuple: # if the element is a tuple, it's a list of it's own possible keys or strings
			res = ''.join(self._getattr(k, k) for k in res)
		return Faker._parse(res)

	def __getitem__(self, key):
		""" Allow key access if the module provides named formats. """
		try:
			if self._formats.has_key(key):
				return Faker._parse(''.join(self._getattr(k, k) for k in self._formats[key]))
			else:
				raise IndexError
		except AttributeError:
			raise NoNamedFormats("Library '%s' does not provide named formats" % self.__class__.__name__.lower())
	
	def __call__(self):
			""" When an instance is called, return a random format. """
			formats = self._get('_formats', None)
			if type(formats) == tuple:
				res = ''.join(self._getattr(k, k) for k in self.random(formats))
			elif type(formats) == dict:
				res = ''.join(self._getattr(k, k) for k in self.random(formats.values()))
			return Faker._parse(res)

