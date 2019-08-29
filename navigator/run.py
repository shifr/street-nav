import logging
import logging.config

import os

from pathlib import Path

from .models import Robot
from .parsers import CityParser, RoutesParser


logging.basicConfig(level=logging.INFO, format='%(levelname)-5.5s: %(message)s')
log = logging.getLogger(__name__)

DATA_PATH = Path(os.environ.get("DATA_PATH", "/service/data"))


def main():
    log.info("Running process...")

    city_file = DATA_PATH / "city.txt"
    routes_file = DATA_PATH / "routes.txt"
    city = CityParser.from_plain_text(city_file)
    routes = RoutesParser.from_plain_text(city, routes_file)
    robot = Robot()

    log.info("Investigating %s city...", city.name)
    for route in routes:
        print("\nNEW ROUTE\n")
        robot.navigate(route)
    log.info("All routes are finished!")

    log.info("Process finished!")
