def detect_blob(measurements):

    area = measurements["area"]
    height = measurements["height"]
    count = measurements["count"]

    if area > 20:
        return True

    if height > 30:
        return True

    if count > 20:
        return True

    return False