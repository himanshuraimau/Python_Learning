chai_type = "Masala"
quantity = 2
order = 'I orderd {} cups of {} chai'.format(quantity, chai_type)
print(order)

# String to List
order = 'I orderd 2 cups of Masala chai'
print(order.split())

# List to string
chai_varieties = ['Masala', 'Ginger', 'Cardamom']
print(" ".join(chai_varieties))
print(", ".join(chai_varieties))

chai  = "He loves \"Masala\" chai"
print(chai)

chai = r'He loves \"Masala"\ chai'  
print(chai)