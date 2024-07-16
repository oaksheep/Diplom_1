from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient("FILLING", "Meatball", 1000)
        assert ingredient.get_price() == 1000

    def test_get_name(self):
        ingredient = Ingredient("FILLING", "Meatball", 1000)
        assert ingredient.get_name() == "Meatball"

    def test_get_type(self):
        ingredient = Ingredient("FILLING", "Meatball", 1000)
        assert ingredient.get_type() == "FILLING"
