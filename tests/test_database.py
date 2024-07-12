import pytest
from unittest import mock
from praktikum.database import Database


class TestDatabase:
    def test_available_buns_with_mocks(self):
        database = Database()
        mock_buns = [mock.Mock(name="Moon_bun"), mock.Mock(name="Sun_bun"), mock.Mock(name="Mars_bun")]
        database.available_buns = mock.Mock(return_value=mock_buns)

        assert database.available_buns() == mock_buns

    def test_available_ingredients_with_mocks(self):
        database = Database()
        mock_ingredients = [mock.Mock(name="Sweet_sauce"), mock.Mock(name="Bitter_sauce"), mock.Mock(name="Sour_sauce"),
                            mock.Mock(name="Meatball"), mock.Mock(name="Prosciutto"), mock.Mock(name="Sausage")]
        database.available_ingredients = mock.Mock(return_value=mock_ingredients)

        assert database.available_ingredients() == mock_ingredients

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("Moon_bun", 1000),
        ("Sun_bun", 1200),
        ("Mars_bun", 1300)
    ])
    def test_available_buns_parameterization(self, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()

        for bun in buns:
            if bun.name == bun_name:
                assert bun.price == bun_price

    @pytest.mark.parametrize("sous, ingredient_name, ingredient_price", [
        ("sauce", "Sweet_sauce", 1010),
        ("sauce", "Bitter_sauce", 1020),
        ("sauce", "Sour_sauce", 1030),
        ("filling", "Meatball", 1110),
        ("filling", "Prosciutto", 1120),
        ("filling", "Sausage", 1130)
    ])
    def test_available_ingredients_parameterization(self, sous, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()

        for ingredient in ingredients:
            if ingredient.type == sous and ingredient.name == ingredient_name:
                assert ingredient.price == ingredient_price