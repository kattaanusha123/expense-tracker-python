class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def to_file_string(self):
        # Format used to store data in file
        return f"{self.amount},{self.category},{self.date}\n"

    @staticmethod
    def from_file_string(line):
        amount, category, date = line.strip().split(",")
        return Expense(float(amount), category, date)
