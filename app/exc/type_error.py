class TypeError(Exception):

    def __init__(self) -> None:
        self.message = {"error": 'address must be a string'}

        super().__init__(self.message)
