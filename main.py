import time
import pytermgui as ptg

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold
    Window:
        styles:
            border: '60'
            corner: '60'
    Container:
        styles:
            border: '60'
            corner: '60'
"""

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    window = (
        ptg.Window(
            "",
            ptg.InputField("AAAA", prompt="Name: "),
            ptg.InputField("BBBB", prompt="Address: "),
            ptg.InputField("CCCC", prompt="Phone: "),
            "",
            ptg.Container(
                "Additional notes:",
                ptg.InputField(
                    "Meaningful\nNotes"
                ),
                box="EMPTY_VERTICAL"
            ),
            "",
            ["Submit", lambda*_: submit(manager, window)],
            width=60,
            box="DOUBLE",
        )
        .set_title("[210 bold] New contact")
        .center()
        )
manager.add(window)
