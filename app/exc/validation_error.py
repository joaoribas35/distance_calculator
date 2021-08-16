class ValidationError(Exception):

    def __init__(self, response: dict) -> None:
        self.message = (
            {
                "error":  response["error"],
            }
        )

        super().__init__(self.message)
