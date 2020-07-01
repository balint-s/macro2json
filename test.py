import json
from macro2json import convert

convert('test_data/input.c', 'out.json');

with open('out.json') as json_file:
    data = json.load(json_file)
    
    assert data.get('SOMETHING') is None
    assert data['HELLO_WORLD'] == '1'
    assert data['SECOND'] == '2'
    assert data['WITH_QUOTES'] == 'hello'
    assert data['FLOAT'] == '3.14'
    assert data['WITH_COMMA'] == 'hello,world'
    assert data['WITH_COMMA2'] == 'hello,world,2'
    assert data['LAST'] == '3'
