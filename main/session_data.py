from dataclasses import dataclass, asdict, field


@dataclass
class Block:
    recipe_id: int
    factory_id: int
    input_dict: dict
    output_dict: dict
    quantity_factory: int
    # TODO: quantity_factory and choose fabric or factory


@dataclass
class ProductLine:
    block_id: int
    block_active: bool
    block_list: list[Block]
    output: dict = field(init=False)
    input: dict = field(init=False)

    def __post_init__(self):
        self.calc_output()
        self.calc_input()

    def calc_input(self) -> None:
        product_dict = {}
        for block in self.block_list:
            for product, quantity in block.input_dict.items():
                if product not in product_dict:
                    product_dict[product] = quantity
                else:
                    product_dict[product] = product_dict[product] + quantity
        self.input = product_dict

    def calc_output(self) -> None:
        product_dict = {}
        for block in self.block_list:
            for product, quantity in block.output_dict.items():
                if product not in product_dict:
                    product_dict[product] = quantity
                else:
                    product_dict[product] = product_dict[product] + quantity
        self.output = product_dict

    def product_to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def dict_to_product(dict_product):
        # TODO: check if dict empty
        product_copy = dict_product.copy()
        product_copy.pop('input')
        product_copy.pop('output')
        block_list = product_copy.pop('block_list')
        blocks = [Block(**block) for block in block_list]
        return ProductLine(block_id=product_copy['block_id'], block_active=product_copy['block_active'], block_list=blocks)

    def add_recipe(self, recipe_id: int, factory_id: int, input_dict: dict, output_dict: dict):
        recipe = Block(recipe_id=recipe_id, factory_id=factory_id, input_dict=input_dict, output_dict=output_dict, quantity_factory=0)
        self.block_list.append(recipe)
        self.calc_output()
        self.calc_input()

    def del_recipe(self, recipe_id: int):
        for block in self.block_list:
            if block.recipe_id == recipe_id:
                self.block_list.remove(block)
                break
        self.calc_output()
        self.calc_input()

    def move_up_recipe(self, recipe_id: int):
        if len(self.block_list) > 1:
            num = 0
            for i, block in enumerate(self.block_list):
                if block.recipe_id == recipe_id:
                    num = i
                    break
            if num != 0:
                prev_element = self.block_list.pop(num - 1)
                self.block_list.insert(num, prev_element)

    def move_down_recipe(self, recipe_id: int):
        if len(self.block_list) > 1:
            num = 0
            for i, block in enumerate(self.block_list):
                if block.recipe_id == recipe_id:
                    num = i
                    break
            if num != len(self.block_list) - 1:
                element = self.block_list.pop(num)
                self.block_list.insert(num + 1, element)
