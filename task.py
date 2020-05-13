class Task:
    def __init__(self, date, name, info, complexity, state):  # strings, state in lower case
        self.date = date
        self.name = name
        self.info = info
        self.state = state
        self.complexity = int(complexity)
        first_clr = [50, 205, 50]
        second_clr = [255, 0, 0]
        self.compl_rgb = [first_num + int(self.complexity * (second_num - first_num) / 10)
                          for first_num, second_num in zip(first_clr, second_clr)]  # from lime_green to red

    def move_right(self):
        if self.state == "todo":
            self.state = "doing"
        elif self.state == "doing":
            self.state = "done"
        else:
            raise ValueError("unable to move")

    def finish(self):
        self.state = "finished"
