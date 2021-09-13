from ansible_compat.runtime import Runtime


class App():
    def __init__(self) -> None:
        self.runtime = Runtime(isolated=True)

app = App()
