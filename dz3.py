#!/usr/bin/python3

class Url:
    def __init__(self, scheme="", authority="", path=[], query={}, fragment=""):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        if str(self) == other:
            return True

    def __str__(self):
        url_string = f'{self.scheme}://{self.authority}'
        if self.path is not None:
            for part in self.path:
                url_string += f'/{part}'
        if self.query != {}:
            query_map = False
            if self.query != {}:
                for path in self.query:
                    if query_map:
                        url_string += f'&{path}={self.query[path]}'
                    else:
                        query_map = True
                        url_string += f'?{path}={self.query[path]}'
        if self.fragment == '':
            pass
        else:
            url_string += f'#{self.fragment}'
        return url_string


class HttpsUrl(Url):
    def __init__(self, scheme='https', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = 'https'


class HttpUrl(Url):
    def __init__(self, scheme='http', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = 'http'


class GoogleUrl(HttpsUrl):
    def __init__(self, scheme='', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = 'google.com'


class WikiUrl(HttpsUrl):
    def __init__(self, scheme='', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = 'wikipedia.org'


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
