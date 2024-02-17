import copy

from django.http import HttpRequest


class SandBox:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        if 'session_key' not in request.session:
            self.sandbox = self.session['session_key'] = []
        else:
            self.sandbox = self.session.get('session_key')

    def __len__(self):
        return len(self.sandbox.values())   # test variant

    def add(self):
        self.sandbox.append({'craft': None})
        self.session.modified = True
