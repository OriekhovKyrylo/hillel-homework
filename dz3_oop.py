#!/usr/bin/python3

class Url:
    def __init__(self, input_scheme="", input_authority="", path="", query={}, fragment=[]):
        self.scheme = input_scheme
        self.authority = input_authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        if (self.scheme == other.scheme and
                self.authority == other.authority and
                self.path == other.path and
                self.query == other.query and
                self.fragment == other.fragment):
            return True
        return False

    def __str__(self):
        return f'{self.scheme} {self.authority} {self.path} {self.query}{self.fragment}'


class HttpsUrl(Url):
    def __init__(self, input_scheme="https://"):
        super().__init__(input_scheme)


class HttpUrl(Url):
    def __init__(self, input_scheme="https://"):
        super().__init__(input_scheme)


class GoogleUrl(HttpsUrl):
    def __init__(self, input_authority="google.com/"):
        super().__init__(input_authority)


class WikiUrl(HttpsUrl):
    def __init__(self, input_authority="wikipedia.org"):
        super().__init__(input_authority)
