#to provide the id adress of a code in the system's memory
list_1 = [1, 2, 4, 7, 10]
list_2 = [1, 2, 4, 7, 10]

print(id(list))
print(id(list_1))

# when we run the piece of code we realise that the two lists contain thesame content, they have different adresses because they exist as seperate lists in the system's memory
# the id always changes each time we run out piece of code