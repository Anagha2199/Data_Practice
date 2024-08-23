#4)StorageIssueAnalysis

storage_issue_weights = {}
with open('FMCG_Data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    issue_index = headers.index('storage_issue_reported_l3m')
    product_weight_index = headers.index('product_wg_ton')
    for line in file:
        values = line.strip().split(',')
        issue = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue
        if issue in storage_issue_weights:
            storage_issue_weights[issue] += product_weight
        else:
            storage_issue_weights[issue] = product_weight
print(f"Storage Issue : Total Supply Weight")
for issue, total_weight in storage_issue_weights.items():
    print(f'\t{issue}\t\t  :\t\t  {total_weight}')