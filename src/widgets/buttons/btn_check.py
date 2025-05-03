from flet import IconButton, Icons, Colors, ButtonStyle

def btn_check(size=70, func=None, ttip='', is_visible=True, is_disabled=False):
    button = IconButton(
        icon=Icons.CHECK,
        icon_color=Colors.WHITE,
        icon_size=size,
        style=ButtonStyle(bgcolor=Colors.GREEN),
        tooltip=ttip,
        on_click=func,
        visible=is_visible,
        disabled=is_disabled
    )
    return button
