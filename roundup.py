"""
The goal for this exercise is to allow the user to
simulate a roundup savings pot based on user transactions.
 - Given a particular start date, obtain all transactions that have occurred within 30 days of the start date
 - For each transaction, compute the roundup to the nearest pound
    e.g. 3.78 rounds up to 4.00 with a roundup amount of 0.22
         2.19 rounds up to 3.00 with a roundup amount of 0.81
 - Compute the total roundup for each user within those 30 days
 - Return a dictionary with the roundup amount for each user

Stretch goals:
 - Find out how to allow the user to type input into the terminal
    then have them type in their user id, and a start / end date.
    Calculate their round up. Remember to validate their input!

 - Find out how to write to a file. Suppose the user wants to transfer
    their roundups to a charity, can you add this transaction to the
    transactions.csv file?
"""

from datetime import datetime, timedelta

filepath = "data/transactions.csv"
start_day = "02 Feb 2019"

def strip_quotes(s):
    return s.replace('"', '')

def construct_datetime(s):
    clean_dt = strip_quotes(s).replace("IST", "")
    return datetime.strptime(clean_dt,"%a %b %d %H:%M:%S %Y")

if __name__ == "__main__":
    data = []

    with open(filepath) as file:
        for i, line in enumerate(file):
            if i == 0:
                continue

            try:
                (
                    user_id,
                    transaction_id,
                    transaction_time,
                    item_code,
                    description,
                    number_of_items,
                    cost_per_item,
                    country
                ) = line.strip().split(",")
            except ValueError as e:
                print(f"Missing data in line {i}")

            data.append({
                "UserId": int(strip_quotes(user_id)),
                "TransactionId": int(strip_quotes(transaction_id)),
                "TransactionTime": construct_datetime(transaction_time),
                "ItemCode": int(strip_quotes(item_code)),
                "ItemDescription": strip_quotes(description),
                "NumberOfItemsPurchased": int(strip_quotes(number_of_items)),
                "CostPerItem": float(strip_quotes(cost_per_item)),
                "Country": strip_quotes(country)
            })
