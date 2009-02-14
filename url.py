import re

from core import FakeLib
from company import Company

class Url(FakeLib):
	""" Exposes:
			domainname
			tld
	"""
	_formats = (
		('http://www.', 'domainname'),
		('http://', 'domainname'),
		('www.', 'domainname'),
		('domainname',)
	)

	_domainnames = (('company', '.', 'tld'), )
	_companys = property(
		lambda s: (re.sub('\W+', '', Company()()).lower(),)
	)
	_tlds = ('co.uk','com','us','org','ca','biz','info','name')
