"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: 2/17/2022
"""

def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Example: if s is '30 USD', this function returns '30'
    Example: if s is '30 USD and 40 EUR', this function returns '30'


    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    lst = s.split(" ")
    return lst[0]

def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice Precondition: s is a string with at least one space
    Precondition: s is a string with at least one space
    """
    lst = s.split(" ")
    rest = lst[1:]
    return " ".join(rest)

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a double
    quote character (") inside of it.

    Example:  If s is 'A "B C" D', this function returns 'B C'
    Example:  If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.

    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters.
    """
    pos_a = s.find('\"')
    y = s[(pos_a+1):]
    z = y.find('\"')
    pos_b = int(pos_a + z)
    return s[(pos_a+1):(pos_b+1)]

def get_lhs(json):
    """Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    keyword = json.find("lhs")
    new_string = json[keyword+4:]
    return first_inside_quotes(new_string)

def get_rhs(json):
    """Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    keyword = json.find("rhs")
    new_string = json[keyword + 4:]
    return first_inside_quotes(new_string)

def has_error(json):
    """ Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    return 'false' in json

def urlread(url):
    """
    Opens the web page at ``url`` and returns its contents.

    If there is no web page at url a ``URLError``. If the url is malformed, it raises a
    ``ValueError`` instead.

    :param url: The web page url
    :type url:  ``str``

    :return: The contents of the web page at ``url`` if it exists.
    :rtype:  ``str``
    """
    import urllib.request
    connect = urllib.request.urlopen(url)
    header  = connect.info()
    payload = connect.read()
    try:
        return payload.decode('utf-8') # Yeah, no way that was going in A1
    except:
        # We need to find out what the encoding is
        encoding = ''
        for item in header.raw_items():
            if item[0] == 'Content-Type':
                encoding = item[1]
                position = encoding.find('charset=')
                encoding = encoding[position+8:]
    if encoding in ['ISO-8859-1','ansi']:
        return payload.decode('latin1')
    elif encoding == 'ascii':
        return payload.decode('ascii')
    else:
        return payload.decode('unicode_escape')

def currency_response(src, dst, amt):
    """ Returns a JSON string that is a response to a currency query.
    A currency query converts amt money in currency src to the 
    currency dst. The response should be a string of the form
    
    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    entire_url=urlread('http://cs1110.cs.cornell.edu/2019fa/a1?'+'src='+src+
                       '&dst='+dst+'&amt='+str(amt))
    return entire_url

def is_currency(code):
    """ 
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """
    error = has_error(currency_response(code, 'PKR' ,'25'))
    not_error = not error
    return not_error

def exchange(src, dst, amt):
    """ Returns the amount of currency received in the given exchange.
    
    In this exchange, the user is changing amt money in currency 
    src to the currency dst. The value returned represents the 
    amount in currency dst.
    
    The value returned has type float.
    
    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code
        
    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    new_currency_amt = float(before_space(get_rhs(currency_response(src, dst, amt))))
    return new_currency_amt

