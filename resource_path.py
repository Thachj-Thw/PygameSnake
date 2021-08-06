def path():
    import sys, os
    try:
        return sys._MEIPASS
    except AttributeError:
        return os.path.abspath(".")
