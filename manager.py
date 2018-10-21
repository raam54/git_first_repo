class Manager:
    def __init__(self, cost_hour, increase):
        self.cost_hour = cost_hour
        self.increase = increase * 0.01
        self.hours = 8
        self.tax = 0.13

    def salary(self, days):
        return self.hours * days * (self.increase * self.cost_hour + self.cost_hour)

    def taxes(self, days):
        return self.hours * self.cost_hour * days * self.tax


