from translator.src.modules.module import Module

class Project (Module):

    def __init__ (self, budget: int, duration: int, strict: bool):
        self.budget = budget
        self.duration = duration
        self.strict = strict

    # Futureu functions go below