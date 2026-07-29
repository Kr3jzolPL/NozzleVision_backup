def detect_blob(measurements):

    area = measurements["area"]
    height = measurements["height"]
    count = measurements["count"]

    if area > 25:
        return True

    if height > 35:
        return True

    if count > 25:
        return True

    return False