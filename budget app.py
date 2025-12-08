class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            body += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + body + total


def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = sum(
            -item["amount"]
            for item in cat.ledger
            if item["amount"] < 0
        )
        spent.append(total)

    overall = sum(spent)
    percentages = [(s / overall) * 100 for s in spent]
    percentages = [int(p // 10) * 10 for p in percentages]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "    "
        for cat in categories:
            if i < len(cat.name):
                chart += " " + cat.name[i] + " "
            else:
                chart += "   "
        chart += " \n"

    return chart.rstrip("\n")
