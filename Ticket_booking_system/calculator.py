class TicketCalculator:
    def __init__(self, price, seats, age, category):
        self.price = price
        self.seats = seats
        self.age = age
        self.category = category

    def discount_total(self):
        discount_amnt=0
        total_amnt = self.price * self.seats
        if self.category == "student":
            discount=0.15
            discount_amnt=total_amnt *discount
            print(discount_amnt)
            final=total_amnt - discount_amnt
            print(final)
            return discount, total_amnt, discount_amnt,final
        elif self.category == "senior" and self.age>60:
            discount = 0.20
            discount_amnt=total_amnt *discount
            final = total_amnt - discount_amnt
            return discount, total_amnt, discount_amnt,final
        else:
            discount = 0.0
            discount_amnt=total_amnt
            final = total_amnt - discount_amnt
            return discount, total_amnt, discount_amnt,final





