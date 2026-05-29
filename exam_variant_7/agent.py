import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from google.adk import Agent

# Завантаження екологічних змінних (.env)
load_dotenv()

class Location(ABC):
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    @abstractmethod
    def get_type(self) -> str:
        """Абстрактний метод, який має бути реалізований у дочірніх класах"""
        pass

class City(Location):
    def __init__(self, name: str, country: str = "Україна"):
        super().__init__(name, country)
        # Інкапсуляція: приватний список температур
        self.__temperatures: list[float] = []

    def add_temperature(self, temp: float):
        self.__temperatures.append(temp)

    def average(self) -> float:
        if not self.__temperatures:
            return 0.0
        return sum(self.__temperatures) / len(self.__temperatures)

    def min_temp(self) -> float:
        return min(self.__temperatures) if self.__temperatures else 0.0

    def max_temp(self) -> float:
        return max(self.__temperatures) if self.__temperatures else 0.0

    def get_type(self) -> str:
        return "Місто"

class Meteorologist(Location):
    def __init__(self, name: str, country: str, station: str):
        super().__init__(name, country)
        self.station = station

    def record_weather(self, city: City, temp: float):
        city.add_temperature(temp)

    def get_type(self) -> str:
        return f"Метеоролог на станції {self.station}"

def get_weather(location: str, temperatures: list) -> dict:
    """
    Розраховує статистику погоди для локації за списком зафіксованих температур.
    """
    city = City(location)
    
    for temp in temperatures:
        city.add_temperature(temp)

    avg = city.average()
    
    # Визначення кліматичного стану на основі середньої температури
    if avg >= 25:
        condition = "Спекотно"
    elif avg >= 15:
        condition = "Тепло"
    elif avg >= 5:
        condition = "Прохолодно"
    else:
        condition = "Холодно"

    return {
        "location": city.name,
        "average_temp": round(avg, 2),
        "min_temp": city.min_temp(),
        "max_temp": city.max_temp(),
        "condition": condition
    }

# Ініціалізація Агента згідно з твоїм шаблоном
root_agent = Agent(
    name="WeatherAgent",
    model="gemini-3.1-flash-lite",
    instruction=(
        "Ти — професійний метеорологічний асистент. Твоє завдання: аналізувати погодні дані локацій. "
        "Використовуй інструмент get_weather для розрахунку середньої, мінімальної та максимальної температури. "
        "На основі отриманого стану (condition) давай користувачеві короткі рекомендації щодо одягу чи планів на день. "
        "Відповідай завжди українською мовою."
    ),
    tools=[get_weather]
)


