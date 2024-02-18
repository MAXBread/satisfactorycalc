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
        max_id = 0
        for item in self.sandbox:
            if item['id'] > max_id:
                max_id = item['id']

        for item in self.sandbox:
            self.sandbox[item['id'] - 1]['active'] = False
        self.sandbox.append({'craft': None, 'id': max_id+1, 'active': True})
        self.session.modified = True

    def activate(self, question_id: int) -> None:
        for i, item in enumerate(self.sandbox):
            if item['id'] == question_id:
                self.sandbox[i]['active'] = True
            else:
                self.sandbox[i]['active'] = False
        self.session.modified = True

    def delete(self) -> None:
        print(self.sandbox)
        for i, item in enumerate(self.sandbox):
            if item['active']:
                print(item)
                print(i)
                self.sandbox.remove(item)
                break
        if len(self.sandbox) != 0:
            self.sandbox[len(self.sandbox) - 1]['active'] = True
        self.session.modified = True

