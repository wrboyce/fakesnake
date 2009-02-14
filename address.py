from core import FakeLib
from name import Name

class Address(FakeLib):
	""" Exposes:
			uk and us named formats
			uk_county
			uk_postcode
			us_state
			us_zipcode
	"""
	_formats = {
		'uk': ('###', ' ', 'name', ' ', 'suffix', '\n', 'uk_county', '\n', 'uk_postcode'),
		'us': ('#####', ' ', 'name', ' ', 'suffix', '\n', 'us_state', '\n', 'us_zipcode'),
	}

	_names = Name._first_names + Name._surnames
	_suffixs = ('Alley','Avenue','Branch','Bridge','Brook','Brooks','Burg','Burgs','Bypass','Camp','Canyon','Cape','Causeway','Center','Centers','Circle','Circles','Cliff','Cliffs','Club','Common','Corner','Corners','Course','Court','Courts','Cove','Coves','Creek','Crescent','Crest','Crossing','Crossroad','Curve','Dale','Dam','Divide','Drive','Drive','Drives','Estate','Estates','Expressway','Extension','Extensions','Fall','Falls','Ferry','Field','Fields','Flat','Flats','Ford','Fords','Forest','Forge','Forges','Fork','Forks','Fort','Freeway','Garden','Gardens','Gateway','Glen','Glens','Green','Greens','Grove','Groves','Harbor','Harbors','Haven','Heights','Highway','Hill','Hills','Hollow','Inlet','Inlet','Island','Island','Islands','Islands','Isle','Isle','Junction','Junctions','Key','Keys','Knoll','Knolls','Lake','Lakes','Land','Landing','Lane','Light','Lights','Loaf','Lock','Locks','Locks','Lodge','Lodge','Loop','Mall','Manor','Manors','Meadow','Meadows','Mews','Mill','Mills','Mission','Mission','Motorway','Mount','Mountain','Mountain','Mountains','Mountains','Neck','Orchard','Oval','Overpass','Park','Parks','Parkway','Parkways','Pass','Passage','Path','Pike','Pine','Pines','Place','Plain','Plains','Plains','Plaza','Plaza','Point','Points','Port','Port','Ports','Ports','Prairie','Prairie','Radial','Ramp','Ranch','Rapid','Rapids','Rest','Ridge','Ridges','River','Road','Road','Roads','Roads','Route','Row','Rue','Run','Shoal','Shoals','Shore','Shores','Skyway','Spring','Springs','Springs','Spur','Spurs','Square','Square','Squares','Squares','Station','Station','Stravenue','Stravenue','Stream','Stream','Street','Street','Streets','Summit','Summit','Terrace','Throughway','Trace','Track','Trafficway','Trail','Trail','Tunnel','Tunnel','Turnpike','Turnpike','Underpass','Union','Unions','Valley','Valleys','Via','Viaduct','View','Views','Village','Village','Villages','Ville','Vista','Vista','Walk','Walks','Wall','Way','Ways','Well','Wells')
	_uk_counties = ('Avon','Bedfordshire','Berkshire','Borders','Buckinghamshire','Cambridgeshire','Central','Cheshire','Cleveland','Clwyd','Cornwall','CountyAntrim','CountyArmagh','CountyDown','CountyFermanagh','CountyLondonderry','CountyTyrone','Cumbria','Derbyshire','Devon','Dorset','DumfriesandGalloway','Durham','Dyfed','EastSussex','Essex','Fife','Gloucestershire','Grampian','GreaterManchester','Gwent','GwyneddCounty','Hampshire','Herefordshire','Hertfordshire','HighlandsandIslands','Humberside','IsleofWight','Kent','Lancashire','Leicestershire','Lincolnshire','Lothian','Merseyside','MidGlamorgan','Norfolk','NorthYorkshire','Northamptonshire','Northumberland','Nottinghamshire','Oxfordshire','Powys','Rutland','Shropshire','Somerset','SouthGlamorgan','SouthYorkshire','Staffordshire','Strathclyde','Suffolk','Surrey','Tayside','TyneandWear','Warwickshire','WestGlamorgan','WestMidlands','WestSussex','WestYorkshire','Wiltshire','Worcestershire')
	_uk_countys = _uk_counties
	_us_states = ('Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','NewHampshire','NewJersey','NewMexico','NewYork','NorthCarolina','NorthDakota','Ohio','Oklahoma','Oregon','Pennsylvania','RhodeIsland','SouthCarolina','SouthDakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','WestVirginia','Wisconsin','Wyoming')

	_uk_postcodes = ('??## #??', '??# #??',)
	_us_zipcodes = ( '#####',  '#####-####' )
