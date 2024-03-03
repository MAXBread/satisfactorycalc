from django.http import HttpRequest
from .session_data import ProductLine


class SandBox:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        if 'product_line' not in request.session:
            self.product_line = self.session['product_line'] = []
        else:
            self.product_line = self.session.get('product_line')

    def __len__(self):
        return len(self.product_line.values())   # test variant

    def add(self):
        max_id = 0
        for n, item in enumerate(self.product_line):
            if item['block_id'] > max_id:
                max_id = item['block_id']
            self.product_line[n]['block_active'] = False
        self.product_line.append(ProductLine(block_id=max_id+1, block_active=True, block_list=[]).product_to_dict())
        self.session.modified = True

    def activate(self, question_id: int) -> None:
        for n, item in enumerate(self.product_line):
            if item['block_id'] == question_id:
                self.product_line[n]['block_active'] = True
            else:
                self.product_line[n]['block_active'] = False
        self.session.modified = True

    def delete(self) -> None:
        for n, item in enumerate(self.product_line):
            if item['block_active']:
                self.product_line.remove(item)
                break
        if len(self.product_line) != 0:
            self.product_line[len(self.product_line) - 1]['block_active'] = True
        self.session.modified = True
