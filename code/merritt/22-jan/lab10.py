with open('demo.csv', 'r') as f:
    data_csv = f.read()
# csv_lines = data_csv.split('\n')
# data_csv = []
# for line in csv_lines:
#     data_csv.append(line.split(','))
data_csv = [line.split(',') for line in data_csv.split('\n')]

keys = data_csv[0]
# data = []
# for row in data_csv[1::]:
#     row_dict = {}
#     # for i in range(len(row)):
#     #     row_dict[keys[i]] = row[i]
#     for i, cell in enumerate(row):
#         row_dict[keys[i]] = cell
#     data.append(row_dict)

# print(list(zip(keys, data_csv[1])))
# print(dict(zip(keys, data_csv[1])))

# for i in range(1, len(data_csv)):
#     data.append(dict(zip(keys, data_csv[i])))

# for values in data_csv[1::]:
#     data.append(dict(zip(keys, values)))

data = [dict(zip(keys, values)) for values in data_csv[1::]]

def create_contact(data, keys):
    # new_contact = {}
    # for key in keys:
    #     new_contact[key] = input(f"What is your new contact's {key}? ")
    # data.append(new_contact)
    data.append({key: input(f"What is your new contact's {key}? ") for key in keys})

data_results = []

def read_contact(data, keys):
    key_string = "\n" + "\n".join(keys) + "\n"
    key_input = input(f"What would you like to search by? Choose from: {key_string} ")
    contact_input = input("What is your search term?")

    # data_results = []
    # for contact in data:
    #     if contact[key_input] == contact_input:
    #         data_results.append(contact)

    # data_results = [contact for contact in data if contact[key_input] == contact_input]
    
    data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))

    print(data_results)

    return data_results

def update_contact(data, keys):
    data_results = read_contact(data, keys)

    index_to_update = int(input(f"Which contact do you want to edit? (1-{len(data_results)}) ")) - 1
    key_to_update = input(f"What key would you like to update? {keys} ")
    value_to_update = input(f"What do you want to change {key_to_update} to? ")

    data_results[index_to_update][key_to_update] = value_to_update

def delete_contact(data, keys):
    data_results = read_contact(data, keys)
    index_to_delete = int(input(f"Which contact do you want to edit? (1-{len(data_results)}) ")) - 1
    data.remove(data_results[index_to_delete])

while True:
    user_input = input("(c)reate, (r)read, (u)pdate, (d)elete, (q)uit?")
    if user_input == 'q':
        break
    elif user_input == 'c':
        create_contact(data, keys)
    elif user_input == 'r':
        read_contact(data, keys)
    elif user_input == 'u':
        update_contact(data, keys)
    elif user_input == 'd':
        delete_contact(data, keys)

data_csv_output = []
data_csv_output.append(keys)
for contact in data:
    data_csv_output.append(list(contact.values()))

# data_csv_output = [list(contact.values()) for contact in data]
# data_csv_output.insert(0, keys)

data_csv_output = [",".join(line) for line in data_csv_output]
data_csv_output = "\n".join(data_csv_output)

with open('demo.csv', 'w') as f:
    f.write(data_csv_output)