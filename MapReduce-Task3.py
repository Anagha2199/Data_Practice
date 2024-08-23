#3)TransportIssueImpactAnalysis

issue_weights = {}
with open('FMCG_Data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    issue_index = headers.index('transport_issue_l1y')
    product_weight_index = headers.index('product_wg_ton')
    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue
        if issue in issue_weights:
            issue_weights[issue] += product_weight
        else:
            issue_weights[issue] = product_weight
print("Transport Issue : Total Supply Weight")
for issue, total_weight in issue_weights.items():
    print(f'\t\t{issue}\t\t:\t\t{total_weight}')