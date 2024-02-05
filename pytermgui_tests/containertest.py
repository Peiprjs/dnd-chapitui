from pytermgui import Container

container = Container(
    "[bold accent]This is my example",
    "",
    "[surface+1 dim italic]It is very cool, you see",
    "",
    {"My first label": ["Some button"]},
    {"My second label": [False]},
    "",
    ("Left side", "Middle", "Right side"),
    "",
    ["Submit button"]
)
