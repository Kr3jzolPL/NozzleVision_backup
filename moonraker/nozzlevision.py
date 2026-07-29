from nozzlevision.engine import inspect

def check():

    result = inspect()

    return {
        "blob": result["blob"]
    }