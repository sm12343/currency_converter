"""
Script for testing a1

Author: Craig Frey
Date:   September 7, 2021
"""
import inspect
import a1

def mystr(x):
    if type(x) == str:
        x = "'" + x + "'"
    return str(x)

def checkDocstring(docstring):
    foundDocstring = False
    foundAuthor = False
    # check module docstring
    docstring = docstring.split('\n')
    for line in docstring:
        if line == 'Module for currency exchange':
            foundDocstring = True
        if line.lower().startswith('author'):
            c = line.find(':')
            if c > 0:
                tail = line[c + 1:].strip()
                if len(tail) > 0 and tail != 'YOUR NAME(S) AND NETID(S) HERE':
                    foundAuthor = True
    if not foundDocstring:
        print('Missing module Docstring -10')
    elif not foundAuthor:
        print('Missing Author -5')

def checkFunc1before_space():
    foundDocstring = False
    # check if func exists and it is a function
    if ('before_space' in dir(a1) and inspect.isfunction(a1.before_space)):
        # check func docstring
        docstring = a1.before_space.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns a copy of s up to, but not including, the first space':
                foundDocstring = True
        if not foundDocstring:
            print('Missing before_space Docstring -4')
        # call func with test cases
        try:
            x = a1.before_space('Hello World')
            if x != 'Hello':
                print("before_space('Hello World'): expected 'Hello' but received " + mystr(x))
            x = a1.before_space('Hello  World')
            if x != 'Hello':
                print("before_space('Hello  World'): expected 'Hello' but received " + mystr(x))
            x = a1.before_space('Scooby doobie doo')
            if x != 'Scooby':
                print("before_space('Scooby doobie doo'): expected 'Scooby' but received " + mystr(x))
            x = a1.before_space(' Scooby')
            if x != '':
                print("before_space(' Scooby'): expected '' but received " + mystr(x))
            x = a1.before_space('Scooby ')
            if x != 'Scooby':
                print("before_space('Scooby '): expected 'Scooby' but received " + mystr(x))
            # test return type
            x = a1.before_space('Hello World')
            if type(x) != str:
                print("before_space('Hello World'): return type expected was <class 'str'> but received " + str(type(x)))
        except:
            print('Error running before_space')
    else:
        print('a1.before_space does NOT exist')

def checkFunc2after_space():
    foundDocstring = False
    # check if func exists and it is a function
    if ('after_space' in dir(a1) and inspect.isfunction(a1.after_space)):
        docstring = a1.after_space.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns a copy of s after the first space':
                foundDocstring = True
        if not foundDocstring:
            print('Missing after_space Docstring -4')
        try:
            x = a1.after_space('Hello World')
            if x != 'World':
                print("after_space('Hello World'): expected 'World' but received " + mystr(x))
            x = a1.after_space('Hello  World')
            if x != ' World':
                print("after_space('Hello  World'): expected ' World' but received " + mystr(x))
            x = a1.after_space('Scooby doobie doo')
            if x != 'doobie doo':
                print("after_space('Scooby doobie doo'): expected 'doobie doo' but received " + mystr(x))
            x = a1.after_space(' Scooby')
            if x != 'Scooby':
                print("after_space(' Scooby'): expected 'Scooby' but received " + mystr(x))
            x = a1.after_space('Scooby ')
            if x != '':
                print("after_space('Scooby '): expected '' but received " + mystr(x))
            # test return type
            x = a1.after_space('Hello World')
            if type(x) != str:
                print("after_space('Hello World'): return type expected was <class 'str'> but received " + str(type(x)))
        except:
            print('Error running after_space')
    else:
        print('a1.after_space does NOT exist')

def checkFunc3first_inside_quotes():
    foundDocstring = False
    # check if func exists and it is a function
    if ('first_inside_quotes' in dir(a1) and inspect.isfunction(a1.first_inside_quotes)):
        docstring = a1.first_inside_quotes.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns the first substring of s between two (double) quotes':
                foundDocstring = True
        if not foundDocstring:
            print('Missing first_inside_quotes Docstring -4')
        try:
            x = a1.first_inside_quotes('Go "big" red')
            if x != 'big':
                print("first_inside_quotes('Go \"big\" red'): expected 'big' but received " + mystr(x))
            x = a1.first_inside_quotes('"Big Red"')
            if x != 'Big Red':
                print("first_inside_quotes('\"Big Red\"'): expected 'Big Red' but received " + mystr(x))
            x = a1.first_inside_quotes('We "all live" on a "yellow" submarine')
            if x != 'all live':
                print("first_inside_quotes('We \"all live\" on a \"yellow\" submarine'): expected 'all live' but received " + mystr(x))
            x = a1.first_inside_quotes('Scooby "" doo')
            if x != '':
                print("first_inside_quotes('Scooby \"\" doo'): expected '' but received " + mystr(x))
            # test return type
            x = a1.first_inside_quotes('go "big" red')
            if type(x) != str:
                print("first_inside_quotes('go \"big\" red'): return type expected was <class 'str'> but received " + str(type(x)))
        except:
            print('Error running first_inside_quotes')
    else:
        print('a1.first_inside_quotes does NOT exist')

def checkFunc4get_lhs():
    foundDocstring = False
    # check if func exists and it is a function
    if ('get_lhs' in dir(a1) and inspect.isfunction(a1.get_lhs)):
        # check func docstring
        docstring = a1.get_lhs.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns the lhs value in the response to a currency query':
                foundDocstring = True
        if not foundDocstring:
            print('Missing get_lhs Docstring -4')
        # call func with test cases
        goodjson = '{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }'
        badjson1 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
        badjson2 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }'
        badjson3 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
        try:
            x = a1.get_lhs(goodjson)
            if x != '1 United States Dollar':
                print('get_lhs(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): expected \'1 United States Dollar\' but received ' + mystr(x))
            x = a1.get_lhs(badjson1)
            if x != '':
                print('get_lhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }\'): expected \'\' but received ' + mystr(x))
            x = a1.get_lhs(badjson2)
            if x != '':
                print('get_lhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }\'): expected \'\' but received ' + mystr(x))
            x = a1.get_lhs(badjson3)
            if x != '':
                print('get_lhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }\'): expected \'\' but received ' + mystr(x))
            # test return type
            x = a1.get_lhs(goodjson)
            if type(x) != str:
                print('get_lhs(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): return type expected was <class \'str\'> but received ' + str(type(x)))
        except:
            print('Error running get_lhs')
    else:
        print('a1.get_lhs does NOT exist')

def checkFunc5get_rhs():
    foundDocstring = False
    # check if func exists and it is a function
    if ('get_rhs' in dir(a1) and inspect.isfunction(a1.get_rhs)):
        # check func docstring
        docstring = a1.get_rhs.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns the rhs value in the response to a currency query':
                foundDocstring = True
        if not foundDocstring:
            print('Missing get_rhs Docstring -4')
        # call func with test cases
        goodjson = '{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }'
        badjson1 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
        badjson2 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }'
        badjson3 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
        try:
            x = a1.get_rhs(goodjson)
            if x != '2.1829264E-5 Bitcoins':
                print('get_rhs(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): expected \'9.1667216E-5 Bitcoins\' but received ' + mystr(x))
            x = a1.get_rhs(badjson1)
            if x != '':
                print('get_rhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }\'): expected \'\' but received ' + mystr(x))
            x = a1.get_rhs(badjson2)
            if x != '':
                print('get_rhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }\'): expected \'\' but received ' + mystr(x))
            x = a1.get_rhs(badjson3)
            if x != '':
                print('get_rhs(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }\'): expected \'\' but received ' + mystr(x))
            # test return type
            x = a1.get_rhs(goodjson)
            if type(x) != str:
                print('get_rhs(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): return type expected was <class \'str\'> but received ' + str(type(x)))
        except:
            print('Error running get_rhs')
    else:
        print('a1.get_rhs does NOT exist')

def checkFunc6has_error():
    foundDocstring = False
    # check if func exists and it is a function
    if ('has_error' in dir(a1) and inspect.isfunction(a1.has_error)):
        # check func docstring
        docstring = a1.has_error.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns True if the query has an error; False otherwise.':
                foundDocstring = True
        if not foundDocstring:
            print('Missing has_error Docstring -4')
        # call func with test cases
        goodjson = '{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }'
        badjson1 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
        badjson2 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }'
        badjson3 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
        try:
            x = a1.has_error(goodjson)
            if x:
                print('has_error(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): expected False but received ' + mystr(x))
            x = a1.has_error(badjson1)
            if not x:
                print('has_error(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }\'): expected True but received ' + mystr(x))
            x = a1.has_error(badjson2)
            if not x:
                print('has_error(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }\'): expected True but received ' + mystr(x))
            x = a1.has_error(badjson3)
            if not x:
                print('has_error(\'{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }\'): expected True but received ' + mystr(x))
            # test return type
            x = a1.has_error(goodjson)
            if type(x) != bool:
                print('has_error(\'{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }\'): return type expected was <class \'bool\'> but received ' + str(type(x)))
        except:
            print('Error running has_error')
    else:
        print('a1.has_error does NOT exist')

def checkFunc7currency_response():
    foundDocstring = False
    # check if func exists and it is a function
    if ('currency_response' in dir(a1) and inspect.isfunction(a1.currency_response)):
        # check func docstring
        docstring = a1.currency_response.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns a JSON string that is a response to a currency query.':
                foundDocstring = True
        if not foundDocstring:
            print('Missing currency_response Docstring -4')
        goodjson = '{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }'
        badjson1 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
        badjson2 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }'
        badjson3 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
        # call func with test cases
        try:
            x = a1.currency_response('USD', 'BTC', 1.0)
            if x != goodjson:
                print("currency_response('USD', 'BTC', 1.0): expected '" + goodjson + "' but received " + mystr(x))
            x = a1.currency_response('XYZ', 'BTC', 1.0)
            if x != badjson1:
                print("currency_response('XYZ', 'BTC', 1.0): expected '" + badjson1 + "' but received " + mystr(x))
            x = a1.currency_response('USD', 'XYZ', 1.0)
            if x != badjson2:
                print("currency_response('USD', 'XYZ', 1.0): expected '" + badjson2 + "' but received " + mystr(x))
            x = a1.currency_response('USD', 'BTC', 'x')
            if x != badjson3:
                print("currency_response('USD', 'BTC', 'x'): expected '" + badjson3 + "' but received " + mystr(x))
            # test return type
            x = a1.currency_response('USD', 'BTC', 1.0)
            if type(x) != str:
                print("currency_response('USD', 'BTC', 1.0): return type expected was <class 'str'> but received " + str(type(x)))
        except:
            print('Error running currency_response')
    else:
        print('a1.currency_response does NOT exist')

def checkFunc8is_currency():
    foundDocstring = False
    # check if func exists and it is a function
    if ('is_currency' in dir(a1) and inspect.isfunction(a1.is_currency)):
        # check func docstring
        docstring = a1.is_currency.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns: True if code is a valid (3 letter code for a) currency':
                foundDocstring = True
        if not foundDocstring:
            print('Missing is_currency Docstring -4')
        # call func with test cases
        goodjson = '{ "ok":true, "lhs":"1 United States Dollar", "rhs":"2.1829264E-5 Bitcoins", "err":"" }'
        badjson1 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
        badjson2 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Exchange currency code is invalid." }'
        badjson3 = '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
        try:
            x = a1.is_currency('USD')
            if not x:
                print('is_currency(\'USD\'): expected True but received ' + mystr(x))
            x = a1.is_currency('XYZ')
            if x:
                print('is_currency(\'XYZ\'): expected False but received ' + mystr(x))
            # test return type
            x = a1.is_currency('XYZ')
            if type(x) != bool:
                print('is_currency(\'XYZ\'): return type expected was <class \'bool\'> but received ' + str(type(x)))
        except:
            print('Error running is_currency')
    else:
        print('a1.is_currency does NOT exist')

def checkFunc9exchange():
    foundDocstring = False
    # check if func exists and it is a function
    if ('exchange' in dir(a1) and inspect.isfunction(a1.exchange)):
        # check func docstring
        docstring = a1.exchange.__doc__.strip()
        docstring = docstring.split('\n')
        for line in docstring:
            if line == 'Returns the amount of currency received in the given exchange.':
                foundDocstring = True
        if not foundDocstring:
            print('Missing exchange Docstring -4')
        # call func with test cases
        try:
            x = a1.exchange('USD', 'BTC', 1.0)
            if x != 2.1829264E-5:
                print("exchange('USD', 'BTC', 1.0): expected 2.1829264E-5 but received " + mystr(x))
            x = a1.exchange('USD', 'EUR', 1.0)
            if x != 0.846572:
                print("exchange('USD', 'EUR', 1.0): expected 0.846572 but received " + mystr(x))
            # test return type
            x = a1.exchange('USD', 'BTC', 1.0)
            if type(x) != float:
                print("exchange('USD', 'BTC', 1.0): return type expected was <class 'float'> but received " + str(type(x)))
        except:
            print('Error running exchange')
    else:
        print('a1.exchange does NOT exist')


docstring = a1.__doc__.strip()
checkDocstring(docstring)
checkFunc1before_space()
checkFunc2after_space()
checkFunc3first_inside_quotes()
checkFunc4get_lhs()
checkFunc5get_rhs()
checkFunc6has_error()
checkFunc7currency_response()
checkFunc8is_currency()
checkFunc9exchange()
print('Complete.')