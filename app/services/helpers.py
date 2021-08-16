def verify_input_keys(data: dict):
    """ Will return a list with strings if the required_keys does not contain a key named address"""

    required_keys = ["address"]
    keys = data.keys()

    return [key for key in required_keys if key not in keys]


def verify_error(data: dict):
    """ Will return a list with strings if the verifying_keys contains a key named error"""

    verifying_keys = ["error"]
    keys = data.keys()

    return [key for key in verifying_keys if key in keys]
