from ..models import City, Landmark
from .helpers import get_position


class CityParser:
    @classmethod
    def from_plain_text(cls, file_path: str) -> City:
        """
        Parse a city and landmarks from the plaintext file
        """
        with open(file_path, "r") as f:
            name_line = f.readline()
            city = City(name_line.strip())

            line = f.readline()
            while line:
                *name_parts, pos = line.split()
                position = get_position(pos)
                name = " ".join(name_parts)

                city.landmarks[name] = Landmark(name, position)

                line = f.readline()

            return city
