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
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -1 * amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum([element["amount"] for element in self.ledger])

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def __repr__(self):
        title_length = 30
        # set length of item description part
        item_desc_length = 23
        # set length of the spending amount part
        amount_length = 7
        star_length = (title_length - len(self.name)) // 2
        # make stars string
        stars = "".join(["*" for i in range(star_length)])
        title = f"{stars}{self.name}{stars}"
        body = ""
        for element in self.ledger:
            padding_length = item_desc_length - len(element["description"])
            padding = "".join([" " for i in range(padding_length)])
            amount = "{:.2f}".format(element['amount'])
            amount_padding_length = amount_length - len(amount)
            amount_padding = "".join([" " for i in range(amount_padding_length)])
            amount = f"{amount_padding}{amount[:amount_length]}"
            body += f"{element['description'][:item_desc_length]}{padding}{amount}\n"
        body += f"Total: {self.get_balance()}"

        return f"{title}\n{body}"


def count_spending(category):
    total = 0
    for element in category.ledger:
        if element['amount'] < 0:
            total += -1 * element['amount']
    return total


def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    spendings = [ count_spending(c) for c in categories ]
    percentages = [ int((s / sum(spendings) * 100)) for s in spendings ]
    # build the graph
    for i in range(100, -10, -10):
        if i < 100 and i > 0:
            output += " "
        if i == 0:
            output += "  "
        output += f"{i}| "
        for j in range(len(categories)):
            if i <= percentages[j]:
                output += "o  "
            else:
                # 3 spaces
                output += "   "
        output += "\n"
    # build the separation line
    # concatenate 4 spaces (on the left side)
    output += "".join([" " for i in range(4)])
    # approximately 3 dashes (-) per each letter underneath the separation line plus one
    output += "".join(["-" for i in range(len(categories) * 3 + 1)])
    output += "\n"
    # work with category names separately
    category_names = [ c.name for c in categories ]
    max_length = max([len(name) for name in category_names])
    # find the longest category name and make other category names as long by adding spaces
    for i in range(len(category_names)):
        category_names[i] += "".join([" " for _ in range(max_length - len(category_names[i]))])
    # build the part with category names underneath the separation line
    for i in range(max_length):
        # start with 4 spaces on the left side on each line
        output += "".join([" " for i in range(4)])
        for name in category_names:
            output += f" {name[i]} "
        if i < max_length - 1:
            output += " \n"
        # last line should not contain a newline character
        else:
          output += " "
    return output
