def get_creators(record:dict) -> list:
    match record:
        case {'type':'book','api':2,'authors':[*names]}:
            return names
        case {'type':'book','api':1,'author':name}:
            return [name]
        case {'type':'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r} ")
        case {'type':'movie','director':name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record : {record!r}")
        

d1=dict(api=1, author='Douglas Hofstadter',type='book', title='Gödel, Escher, Bach')
print(get_creators(d1)) #unlike sequence patterns, mapping patterns succeed at partial mapping i.e presence of an extra field along 
                        # specified fields in pattern will work fine

from collections import OrderedDict

d2 = OrderedDict(api=2, type='book',title='Python in a Nutshell',authors='Martelli Ravenscroft Holden'.split())
print(get_creators(d2))
