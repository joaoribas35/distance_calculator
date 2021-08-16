class AddressError(Exception):

    def __init__(self) -> None:
        self.message = {"error": 'invalid or inexistent address'}

        super().__init__(self.message)
