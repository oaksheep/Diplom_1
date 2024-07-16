from praktikum.bun import Bun

class TestBun:
    bun = Bun('Moon_bun', 1000)

    def test_get_name(self):
        bun_name = self.bun.get_name()
        assert bun_name == 'Moon_bun'

    def test_get_price(self):
        bun_price = self.bun.get_price()
        assert bun_price == 1000
