# fakesnake

A Library for generating random data, useful in testing.


## Usage

	>>> from fakesnake import faker
	>>> faker.name()
	'Isaiah Eichmann'
	>>> faker.email()
	'Marilou_Stehr@hotmail.com'
	>>> print faker.address()
	903 Destin Divide
	HighlandsandIslands
	BH5 3JC
	>>> print faker.address['us']
	86455 Cierra Freeway
	Tennessee
	03722
	>>> print faker.address['uk']
	479 Emil Mills
	Derbyshire
	KZ00 4QV
	>>> print faker.url.domainname
	brownandoconnergroup.info


## Modules

* Address
* Company
* Email
* Name
* Phone
* Url
