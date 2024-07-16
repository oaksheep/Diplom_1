import pytest
from unittest import mock
from praktikum.database import Database
from praktikum.ingredient import Ingredient


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

    @pytest.mark.parametrize("i, bun_name, bun_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_parameterization(self, i, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert buns[i].get_name() == bun_name
        assert buns[i].get_price() == bun_price


    @pytest.mark.parametrize("i, sous, ingredient_name, ingredient_price", [
        (0, "SAUCE", "hot sauce", 100),
        (1, "SAUCE", "sour cream", 200),
        (2, "SAUCE", "chili sauce", 300),
        (3, "FILLING", "cutlet", 100),
        (4, "FILLING", "dinosaur", 200),
        (5, "FILLING", "sausage", 300)
    ])
    def test_available_ingredients_parameterization(self, i, sous, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[i].get_name() == ingredient_name
        assert ingredients[i].get_type() == sous
        assert ingredients[i].get_price() == ingredient_price

