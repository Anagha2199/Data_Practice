#1)Demand - Supply Mismatch Analysis

zone_regional_zone_weights = {}
with open('FMCG_Data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    zone_index = headers.index('zone')
    regional_zone_index = headers.index('WH_regional_zone')
    product_weight_index = headers.index('product_wg_ton')
    for line in file:
        values = line.strip().split(',')
        zone = values[zone_index]
        regional_zone = values[regional_zone_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue
        key = (zone, regional_zone)
        if key in zone_regional_zone_weights:
            zone_regional_zone_weights[key] += product_weight
        else:
            zone_regional_zone_weights[key] = product_weight
print("\tTotal Supply Weight")
for key, total_weight in zone_regional_zone_weights.items():
    print(f'{key[0]},{key[1]} - {total_weight}')

