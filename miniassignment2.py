flag = True


def duplicate_elements():
    array_list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
    for i in array_list:
        ele_count = {}
        for k in i:
            if k in ele_count.keys():
                ele_count[k] += 1
            else:
                ele_count[k] = 1
        for key, value in ele_count.items():
            if value > 1:
                print(key, "->", value, end=",")
        print()


def merge_lists():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    fin_list = []
    for i in list1:
        for j in list2:
            fin_list.append(i+j)
    print(fin_list)


def iterate_nested_list(list1, sub_list):
    global flag
    for item in list1:
        if type(item) is list:
            iterate_nested_list(item, sub_list)
        if flag and type(item) is list:
            item += sub_list
            flag = False


def nested_list_prob(nested_list, sub_list):
    iterate_nested_list(nested_list, sub_list)
    print(nested_list)


def merge_list_to_dict(keys, value):
    res_dict = {}
    for i in range(len(keys)):
        res_dict[keys[i]] = value[i]
    print(res_dict)


def merge_dict(dict1, dict2):
    dict1.update(dict2)
    print(dict1)


def update_key_in_dict(sample_dict, old_key, new_key):
    print("Initial dictionary:", sample_dict)
    sample_dict[new_key] = sample_dict.pop(old_key)
    print("Updated dictionary:", sample_dict)


def convert_dict_to_list(dict_org):
    res_list = []
    for keys, value in dict_org.items():
        keys_list = [keys]
        keys_list += value
        res_list.append(keys_list)
    print(res_list)


duplicate_elements()
merge_lists()
nested_list_prob(["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"], ["h", "i", "j"])
merge_list_to_dict(["Ten", "Twenty", "Thirty"], [10, 20, 30])
merge_dict({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
update_key_in_dict({"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}, "city", "location")
convert_dict_to_list({"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]})