from datetime import datetime, timezone

# logging decorator
def logger(fn):
    def inner(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        to_execute = fn(*args, **kwargs)
        print(f'{fn.__name__} executed. Logged at {called_at}')
        return to_execute
    return inner

@logger
def fee():
    pass

@logger
def fo():
    pass

@logger
def fum():
    pass

fee()
fo()
fum()