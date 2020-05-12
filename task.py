class Task:
    def __init__(self, date, name, info, state):  # strings, state in lower case
        self.date = date
        self.name = name
        self.info = info
        self.state = state

    def move_right(self):
        if self.state == "todo":
            self.state = "doing"
        elif self.state == "doing":
            self.state = "done"
        else:
            raise ValueError("unable to move")