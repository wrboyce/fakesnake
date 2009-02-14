from core import FakeLib
from name import Name

class Company(FakeLib):
	_formats =  (
		('surname', ' ', 'suffix'),
		('surname', ' ', 'and', ' ', 'surname', ' ', 'suffix'),
		('surname', ', ', 'surname', ' ', 'and', ' ', 'surname'),
	)

	_surnames = Name._surnames
	_suffixs = ('Inc','and Sons','LLC','Group','PLC','Ltd')
