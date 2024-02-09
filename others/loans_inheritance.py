class Loan:

    def __init__(self, amount, interest_rate, duration):

        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration

    
    def apply_for_loan(self):

        self.is_approved = True
        print("Loan is approved")
    

    def calculate_total_payment(self):

        if self.is_approved:
            interest_amount = self.amount * self.interest_rate * self.duration

            return interest_amount + self.amount

        else:

            print("Your loan is not approved. HEnce, cannot calculate total payment")



class CarLoan(Loan):

    def __init__(self, amount, interest_rate, duration, car_model):

        super().__init__(amount, interest_rate, duration)
        self.car_model = car_model


    def display_car_model(self):

        print(f"Car Model is: {self.car_model}")




# Create a general loan
personal_loan = Loan(amount=5000, interest_rate=0.08, duration=12)
personal_loan.apply_for_loan()

# Create a car loan (inherits from Loan)
car_loan = CarLoan(amount=20000, interest_rate=0.1, duration=24, car_model="Sedan")
car_loan.apply_for_loan()
car_loan.display_car_model()

# Calculate total payment for both loans
print(f"Total Payment for Personal Loan: {personal_loan.calculate_total_payment()}")
print(f"Total Payment for Car Loan: {car_loan.calculate_total_payment()}")
