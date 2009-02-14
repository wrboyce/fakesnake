from core import FakeLib
from name import Name
from url import Url

class Email(FakeLib):
	""" Exposes:
			domainname
			domain
			name
	"""
	_formats = ( ('name', '@', 'domainname'), )
	_domainnames = (
		('gmail.com', 'googlemail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk',) * 20 +
		( ('domain',), )
	)
	_names = (
		('first_name',),
		('first_name', '.', 'surname'),
		('first_name', '_', 'surname'),
		('first_name', '####'),
		('first_name', 'surname'),
	)

	# names
	_first_names = Name._first_names
	_surnames = Name._surnames
	
	# domains
	_domains = property(
		lambda s: (Url().domainname.strip('www.'), )
	)
