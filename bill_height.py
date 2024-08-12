bill_height = 0.11
bill_count = 1
days = 1
while (bill_count*bill_height <= 442.0):
    bill_count = bill_count * 2
    days = days + 1
    print("current bill height", bill_height)
    print("current bill count:" ,bill_count)
    print("no of days:" ,days)
print("It took ", days, " days to reach the height of the tower")
