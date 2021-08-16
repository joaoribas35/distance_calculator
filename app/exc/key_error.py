class KeyError(Exception):
    feild_options = ['address']

    def __init__(self) -> None:
        self.message = {"error": 'invalid key'}

        super().__init__(self.message)
