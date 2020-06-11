class Task:
    def __init__(self, date, name, info, complexity, state):  # strings, state in lower case
        self.date = date
        self.name = name
        self.info = info
        self.state = state
        self.complexity = int(complexity)
        easy_color = [50, 205, 50]
        hard_color = [255, 0, 0]
        self.complexity_rgb = [easy_num + int(self.complexity * (hard_num - easy_num) / 10)
                               for easy_num, hard_num in zip(easy_color, hard_color)]  # from lime_green to red

    def move_right(self):
        if self.state == "todo":
            self.state = "doing"
        elif self.state == "doing":
            self.state = "done"
        else:
            raise ValueError("unable to move")

    def finish(self):
        self.state = "finished"
