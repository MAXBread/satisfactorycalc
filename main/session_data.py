from dataclasses import dataclass, asdict, field
from .models import Recipe


@dataclass
class Block:
    recipe_id: int
    factory_id: int
    input_dict: dict
    output_dict: dict
    quantity_factory: int
    # TODO: fabric incorrect

    def __post_init__(self):
        self.calc_output()

    def calc_output(self):
        output_dict = {}
        for key, value in self.output_dict.items():
            output_dict[key] = value * self.quantity_factory
        self.output_dict = output_dict


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
                    product_dict[product] = quantity * block.quantity_factory
                else:
                    product_dict[product] = product_dict[product] + quantity * block.quantity_factory
        self.input = product_dict

    def calc_output(self) -> None:
        product_dict = {}
        for block in self.block_list:
            for product, quantity in block.output_dict.items():
                if product not in product_dict:
                    product_dict[product] = quantity * block.quantity_factory
                else:
                    product_dict[product] = product_dict[product] + quantity * block.quantity_factory
        self.output = product_dict

    def calc_total(self) -> None:
        product_dict_output = {}
        product_dict_input = {}
        for block in self.block_list.reverse():
            for product, quantity in block.input_dict.items():
                if product not in product_dict_input:
                    product_dict_input[product] = quantity * block.quantity_factory
                else:
                    product_dict_input[product] = product_dict_input[product] + quantity * block.quantity_factory

            for product, quantity in block.output_dict.items():
                if product not in product_dict_output:
                    product_dict_output[product] = quantity * block.quantity_factory
                else:
                    product_dict_output[product] = product_dict_output[product] + quantity * block.quantity_factory


    def product_to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def dict_to_product(dict_product):
        # TODO: check if dict empty
        product_copy = dict_product.copy()
        product_copy.pop('input')
        product_copy.pop('output')
        block_list = product_copy.pop('block_list')
        new_block_list = []
        for block in block_list:
            recipe = Recipe.objects.filter(pk=block['recipe_id']).first()
            input_dict = {r.product_id: float(r.quantity) for r in recipe.input.all()}
            output_dict = {r.product_id: float(r.quantity) for r in recipe.output.all()}
            new_block_list.append(Block(recipe_id=block['recipe_id'], factory_id=block['factory_id'],
                                        input_dict=input_dict, output_dict=output_dict,
                                        quantity_factory=block['quantity_factory']))
        return ProductLine(block_id=product_copy['block_id'], block_active=product_copy['block_active'],
                           block_list=new_block_list)
