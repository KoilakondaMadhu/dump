def splitit(transactions):
    balances = {}

    for transaction in transactions:
        payer, amount, _, recipient = transaction.split('/')
        value = int(amount[1:])
        if payer != recipient:
            balances[payer] = balances.get(payer, 0) - value
            balances[recipient] = balances.get(recipient, 0) + value

    results = []
    for person, amount in balances.items():
        if amount > 0:
            results.append(f"{person}/A/{amount}")
        elif amount < 0:
            results.append(f"A/{person}/{-amount}")

    if not results:
        return ["NO DUES"]
    return results


# Input processing
n = int(input())
transactions = [input() for _ in range(n)]

# Output the result
result = splitit(transactions)
for line in result:
    print(line)
