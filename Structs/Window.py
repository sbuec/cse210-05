class Window:
    '''
    struct
    
    Args:
    - height (int): Program window height
    - width (int): Program window width
    - caption (str): Program window caption
    - fps_cap (int): Program window fps
    '''

    def __init__(self, height: int, width: int, caption: str, fps_cap: int):
        self.height = height
        self.width = width
        self.caption = caption
        self.fps_cap = fps_cap
    
    def __repr__(self) -> str:
        return f'Window("{self.height}", "{self.width}", "{self.caption}", "{self.fps_cap}")'
    
    def __str__(self) -> str:
        return f'({self.height}, {self.width}, {self.caption}, {self.fps_cap})'