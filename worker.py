class Worker:
    def __init__(self, cost_hour):
        self.cost_hour = cost_hour
        self.hours = 8
        self.tax = 0.13

    def salary(self, days):
        return self.hours * self.cost_hour * days

    def taxes(self, days):
        return self.hours * self.cost_hour * days * self.tax

