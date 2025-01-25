import time

def hello_world(text: str):
    print(text)


def just_sleeping():
    try:
        time.sleep(1)
    except Exception as e:
        print(e)