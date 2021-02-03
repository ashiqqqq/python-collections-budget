class BudgetList(object):
    """docstring for ."""

    def __init__(self, budegt):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if self.sum_expenses + self.item < self.budget:
            self.expenses.append(self.item)
            self.sum_expenses =+ item
            
