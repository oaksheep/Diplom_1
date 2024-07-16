import pytest

from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Moon_bun", 1000)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize(
        'ingredient, expected_result', [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, ['SAUCE']),
            (ingredient_types.INGREDIENT_TYPE_FILLING, ['FILLING'])
        ]
    )
    def test_add_ingredient(self, ingredient, expected_result):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == expected_result

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Salad", "Cheese", 1100)
        ingredient2 = Ingredient("Tomato", "Fillet", 1200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Salad", "Cheese", 1100)
        ingredient2 = Ingredient("Tomato", "Fillet", 1200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Sun_bun", 1300)
        ingredient1 = Ingredient("Salad", "Cheese", 1000)
        ingredient2 = Ingredient("Tomato", "Fillet", 1200)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 4800

    def test_get_receipt(self):
        bun = Bun("Sun_bun", 1300)
        ingredient1 = Ingredient("Salad", "Cheese", 1000)
        ingredient2 = Ingredient("Tomato", "Fillet", 1200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {ingredient1.get_type().lower()} {ingredient1.get_name()} =' in receipt
        assert f'= {ingredient2.get_type().lower()} {ingredient2.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt