import math
from google.adk.agents.llm_agent import Agent

def calculate_rectangle_area(width: float, height: float) -> float:
    """Обчислює площу прямокутника."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """Обчислює об'єм куба."""
    return side ** 3

def calculate_cylinder_volume(radius: float, height: float) -> dict:
    """
    Обчислює об'єм циліндра за радіусом основи та висотою.
    
    Args:
        radius: радіус основи циліндра
        height: висота циліндра
    Returns:
        dict: результат обчислення або повідомлення про помилку
    """
    if radius <= 0 or height <= 0:
        return {"error": "Радіус та висота мають бути більшими за нуль", "result": None}
    volume = math.pi * (radius ** 2) * height
    return {"result": round(volume, 2), "error": None}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_agent',
    description="Виконує математичні обчислення геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент який допомагає з обчисленнями.
    У тебе є інструменти для обчислення площі прямокутника, площі кола, об'єму куба та об'єму циліндра.
    Використовуй ці інструменти коли потрібно виконати розрахунки.
    Відповідай українською мовою та детально пояснюй хід обчислень.
    """,
    tools=[calculate_rectangle_area, calculate_circle_area, calculate_cube_volume, calculate_cylinder_volume],
)