#!/usr/bin/python3

class Url:
    def __init__(self, scheme, authority, path, query, fragment):
        self.scheme = ""
        self.authority = ""
        self.path = ""
        self.query = []
        self.fragment = []

    def __eq__(self, other):
        if (self.scheme == other.scheme and
                self.authority == other.authority and
                self.path == other.path and
                self.query == other.query and
                self.fragment == other.fragment):
            return True
        return False

    def __str__(self):
        return f'{self.scheme} ://{self.authority} /{self.path} ?{self.query}{self.fragment}'


class HttpsUrl(Url):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = "https"


class HttpUrl(Url):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = "http"


class GoogleUrl(HttpsUrl):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = "google.com"


class WikiUrl(HttpsUrl):
    def __init__(self, scheme, authority, path, query, fragment):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = "wikipedia.org"
