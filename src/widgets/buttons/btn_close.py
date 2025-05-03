from flet import IconButton, Icons, Colors, ButtonStyle

def btn_close(size=70, func=None, ttip='', v=True):
    button = IconButton(
        icon=Icons.CLOSE,
        icon_color=Colors.WHITE,
        icon_size=size,
        style=ButtonStyle(bgcolor=Colors.RED),
        tooltip=ttip,
        on_click=func,
        visible=v
    )
    return button
