from flet import IconButton, Icons, Colors

def btn_delete(btn_w = 40, btn_size = 30, on_click_func=None):
    button = IconButton(
        Icons.DELETE, 
        icon_size=btn_size, 
        icon_color=Colors.RED, 
        width=btn_w,
        on_click=on_click_func
        )
    return button