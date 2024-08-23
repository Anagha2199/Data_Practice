#2)Warehouse Refill Frequency Correlation
def convert_capacity_to_numeric(capacity_size):
    size_map = {
        'Small': 1,
        'Mid': 2,
        'Large': 3
    }
    return size_map.get(capacity_size, 0)

capacities = []
refill_requests = []
with open('FMCG_Data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    capacity_index = headers.index('WH_capacity_size')
    refill_index = headers.index('num_refill_req_l3m')
    for line in file:
        values = line.strip().split(',')
        try:
            capacity = convert_capacity_to_numeric(values[capacity_index])
            refill = float(values[refill_index])
            capacities.append(capacity)
            refill_requests.append(refill)
        except ValueError:
            continue
def calculate_correlation(x, y):
    n = len(x)
    if n == 0:
        return None
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    denominator_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5
    if denominator_x == 0 or denominator_y == 0:
        return None
    return numerator / (denominator_x * denominator_y)

correlation = calculate_correlation(capacities, refill_requests)
if correlation is not None:
    print(f"Correlation coefficient: {correlation}")
else:
    print("Insufficient data to compute correlation.")