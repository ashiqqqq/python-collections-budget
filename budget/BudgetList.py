class BudgetList(object):
    """docstring for ."""

    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if (self.sum_expenses + self.item < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return (self.expenses + self.overages)

    def __main__(myBudgetList):
        BudegtList = 1200
        return BudgetList
        
