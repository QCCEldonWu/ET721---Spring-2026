"""
Eldon Wu
Feb 5, 2026
lab 4, dictionary
"""
print("\n----- Example 1: dictionary -----")
#declare and initialize a dictionary
contacts = {
    'Bill': '718-111-2222',
    'Rick': '917-000-1111',
    'Mary': '800-222-3333'
}
print(f"original dictionary: {contacts}")

#update the value of key Rick
contacts['Rick'] = '347-000-1111'

print(f"updated dictionary: {contacts}")

#add new key-value pair
contacts['Peter'] = '888-000-1111'

print(f"updated dictionary with new pair: {contacts}")

print("\n----- Example 2: loop through dictionary -----")
#for loop to print each key in the dictionary
for v in contacts:
    print(v)

#for loop to print each value in the dictionary
for v in contacts:
    print(contacts[v])

#for loop to print each key-value pair in the dictionary
for v in contacts:
    print(f'{v} phone number is {contacts[v]}')

print("\n----- Example 3: items(), keys(), values() methods in a dictionary -----")
#items method returns the key-value pairs in the dictionary
print(f"items in the dictionary: {contacts.items()}")
# keys method returns all the keys in the dictionary
print(f"all keys in the dictionary: {contacts.keys()}")
# values method returns all the values in the dictionary
print(f"all values in the dictionary: {contacts.values()}")

print("\n----- Example 4: check if a key is 'in' or 'not in' a dictionary -----")
check_name = 'Lucy'
check = check_name in contacts
print(f"is {check_name} in the dictionary? {check}")

print("\n----- Example 5: length of a dictionary -----")
print(f"contacts has {len(contacts)} key-value pairs")

print("\n----- Example 6: remove a pair -----")
print(f"original dictionary: {contacts}")
contacts.pop('Mary')
print(f"updated dictionary: {contacts}")

print("\n----- Example 7: get method -----")
#get method returns the value pair of a key
print(f"key-value pair: {contacts.get('Bill')}")

print("\n----- Example 8: update method -----")
# can be used to update a value of a key or to add a new key-value pair
contacts.update({'Annie': '718-888-9999'})
print(f"{contacts}")

print("\n----- EXERCISE -----")