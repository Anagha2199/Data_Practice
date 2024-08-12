my_stocks={}
my_stocks={"TCS":2700,"Infosys":3000,"IDBI":140,"IDFC":100,"NTPC":220}
print(my_stocks)
print(my_stocks.keys())
print(my_stocks.values())
for stock,price in my_stocks.items():
    print(stock,"has the price",price)
my_stocks.pop("Infosys")
print(my_stocks)
my_stocks.popitem()
print(my_stocks)
del my_stocks["TCS"]
print(my_stocks)

swapped={}
for key,value in my_stocks.items():
    swapped[value]=key
print(swapped)