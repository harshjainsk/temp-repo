import pandas as pd

loan_amount = 1000000
annual_interest_rate = 10
tenor = 10


interest_rate_per_month = annual_interest_rate / 1200
tenor_in_months = tenor * 12


emi = loan_amount * (interest_rate_per_month * ((interest_rate_per_month + 1) ** tenor_in_months)) / (((1 + interest_rate_per_month) ** tenor_in_months) - 1)


print(emi)


def calculate_amortization_schedule(loan_amount, interest_rate_per_month, tenor_in_months):

    
    payment_number = []
    # payment_date = []
    principal_payment = []
    interest_payment = []
    remaining_balance = []

    # Initialize remaining balance to the loan amount
    remaining = loan_amount


    for period in range(1, tenor_in_months+1):

        interest = remaining * annual_interest_rate / 1200
        print(interest)
        principal = emi - interest
        remaining -= principal


        payment_number.append(period)
        # payment_date.append(pd.to_datetime(f'{period}M'))

        principal_payment.append(principal)

        interest_payment.append(interest)
        remaining_balance.append(remaining)

    # Create a DataFrame from the lists
    amortization_df = pd.DataFrame({
        'Payment Number': payment_number,
        # 'Payment Date': payment_date,
        'EMI': emi,
        'Principal Payment': principal_payment,
        'Interest Payment': interest_payment,
        'Remaining Balance': remaining_balance
    })

    return amortization_df



amortization_schedule = calculate_amortization_schedule(loan_amount, annual_interest_rate, tenor_in_months)
amortization_schedule.to_csv("amortization_schedule.csv", index=False)

# Display the amortization schedule
print(amortization_schedule)
