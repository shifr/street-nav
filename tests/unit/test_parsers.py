from navigator.parsers import CityParser, RoutesParser


class TestCityParser:
    def test_from_plain_text(self, city, data_path):
        new_city = CityParser.from_plain_text(data_path / "city.txt")

        assert new_city == city


class TestRoutesParser:
    def test_from_plain_text(self, routes, city, data_path):
        new_routes = RoutesParser.from_plain_text(city, data_path / "routes.txt")

        assert new_routes == routes
