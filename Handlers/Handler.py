class Handler:
    '''Base Handler Class'''

    def __init__(self) -> None:
        self._input = {}

    def add(self, name, setup_info: list) -> object:
        '''Adds set_up_info to hold and manage'''

        if name not in self._input:
            self._input[name] = []
            self._input[name] = setup_info
            self.load(name, setup_info)
        return self._input[name][0]
    
    def remove(self, name, setup_info) -> None:
        '''Removed set_up_info from holder and manager'''

        if name in self._input:
            if setup_info in self._input[name]:
                self._input[name].remove(setup_info)
    
    def load(self, name: str, setup_info: list):
        '''Default load function to place the object into Handler lists'''
        pass
    
    def draw(self):
        '''Default draw function that draws on screen'''
        pass

    def update(self):
        '''Default update function that updates the objects on screen'''