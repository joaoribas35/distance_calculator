def verify_input_keys(data: dict):
    required_keys = ["address"]
    keys = data.keys()

    return [key for key in required_keys if key not in keys]


def verify_error(data: dict):
    verifying_keys = ["error"]
    keys = data.keys()

    return [key for key in verifying_keys if key in keys]
