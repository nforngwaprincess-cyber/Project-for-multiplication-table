print("Welcome to CATUC POS")
sum_items = int(input("\nPlease enter the number of items bought:"))
items_SN =[]
items_name =[]
items_quantity = []
items_cost = []

for item in range(1,sum_items+1):
    SN = int(input(f"\nPlease enter the serial number of item {item}:"))
    items_SN.append(SN)
    name = input(f"\nPlease enter the item name of item {item}:")
    items_name.append(name)
    quantity = int(input(f"\nPlease enter the item quantity of item {item}:"))
    items_quantity.append(quantity)
    cost = float(input(f"\nPlease input the cost of item {item}:"))
    items-cost.append(cost)

#individual item cost total
items_cost_total = []
for i in range (sum_items):
    item_total = items_quantity[i] * items_cost[i]
    items_cost_total.append(item_total)

#total items cost
final_total = sum(items_cost_total)

if final_total >10000:
    discount = 0.30 * final_total
    total_cost = final_total - discount
    print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
elif(len((items_cost)) > 5) and (final_total > 4000):
    discount = 0.15 * final_total
    total_cost = items_cost - discount
    print(f"\nTotal purchase ={total_cost}frs\n Thanks for your patronage")
elif items_cost > 5000:
    discount = 0.10 * final_total
    total_cost = items-cost - discount
    print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
else:
    total_cost = final_total
    print(f"\nTotal purchase = {total_cost}frs\n Thanks for your patronage")
        
        
          

          




    











    
    

    
                  











