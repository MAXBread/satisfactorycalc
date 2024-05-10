from django.http import HttpRequest

from .models import Recipe
from .session_data import ProductLine, Block


class SandBox:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        if 'product_line' not in request.session:
            session_data = self.session['product_line'] = []
        else:
            session_data = self.session.get('product_line')
        self.product_line = []
        for block in session_data:
            self.product_line.append(ProductLine.dict_to_product(block))

    def __len__(self):
        return len(self.product_line)

    def get_active_product_line(self) -> ProductLine | None:
        line = None
        for product_line in self.product_line:
            if product_line.block_active:
                line = product_line
                break
        return line

    def session_save(self):
        self.session['product_line'] = [b.product_to_dict() for b in self.product_line]
        self.session.modified = True

    def add(self):
        max_id = 0
        for n, block in enumerate(self.product_line):
            if block.block_id > max_id:
                max_id = block.block_id
            self.product_line[n].block_active = False
        self.product_line.append(ProductLine(block_id=max_id + 1, block_active=True, block_list=[]))
        self.session_save()

    def activate(self, block_id: int) -> None:
        for n, block in enumerate(self.product_line):
            if block.block_id == block_id:
                self.product_line[n].block_active = True
            else:
                self.product_line[n].block_active = False
        self.session_save()

    def delete(self) -> None:
        for n, block in enumerate(self.product_line):
            if block.block_active:
                self.product_line.remove(block)
                break
        if len(self.product_line) != 0:
            self.product_line[len(self.product_line) - 1].block_active = True
        self.session_save()

    def add_recipe(self, recipe: Recipe) -> None:
        for n, block in enumerate(self.product_line):
            if block.block_active:
                input_dict = {r.product_id: float(r.quantity) for r in recipe.input.all()}
                output_dict = {r.product_id: float(r.quantity) for r in recipe.output.all()}
                new_block = Block(recipe_id=recipe.id, factory_id=recipe.fabric.id, input_dict=input_dict,
                                  output_dict=output_dict, quantity_factory=1)
                self.product_line[n].block_list.append(new_block)
                self.product_line[n].calc_input()
                self.product_line[n].calc_output()
                self.session_save()
                break

    def recipe_up(self, block_num):
        if block_num != 0:
            for n, block in enumerate(self.product_line):
                if block.block_active:
                    element_up = self.product_line[n].block_list.pop(block_num)
                    self.product_line[n].block_list.insert(block_num - 1, element_up)
                    self.product_line[n].calc_input()
                    self.product_line[n].calc_output()
                    self.session_save()
                    break

    def recipe_down(self, block_num):
        for n, block in enumerate(self.product_line):
            if block.block_active:
                if block_num == len(self.product_line[n].block_list) - 1:
                    return
                element_down = self.product_line[n].block_list.pop(block_num)
                self.product_line[n].block_list.insert(block_num + 1, element_down)
                self.product_line[n].calc_input()
                self.product_line[n].calc_output()
                self.session_save()
                break

    def recipe_del(self, block_num):
        for n, block in enumerate(self.product_line):
            if block.block_active:
                self.product_line[n].block_list.pop(block_num)
                self.product_line[n].calc_input()
                self.product_line[n].calc_output()
                self.session_save()
                break
