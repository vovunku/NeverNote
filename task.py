class Task:
    def __init__(self, date, name, info, complexity, state):  # strings, state in lower case
        self.date = date
        self.name = name
        self.info = info
        self.state = state
        self.complexity = int(complexity)
        f_clr = [50, 205, 50]
        s_clr = [255, 0, 0]
        self.compl_rgb = []  # from lime_green to red
        for f_num, s_num in zip(f_clr, s_clr):
            self.compl_rgb.append(f_num + int(self.complexity * (s_num - f_num) / 10))

    def move_right(self):
        if self.state == "todo":
            self.state = "doing"
        elif self.state == "doing":
            self.state = "done"
        else:
            raise ValueError("unable to move")

    def finish(self):
        self.state = "finished"
