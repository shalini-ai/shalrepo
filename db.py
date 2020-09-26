# example = {
#     1: {
#         "header": "H1",
#         "body": "B1",
#         "footer": "f1"
#     },
#     2: {
#         "header": "H2",
#         "body": "B2",
#         "table":{"r1":"v1","r2":"v2","r3":{"g1":"gv"}},
#         "footer": "f2"
#     }
# }


# def flattening(dictionary):
#     list1 = []
#     for key, value in dictionary.items():
#         list1.append(key)
#         # print(value)
#         helper(value,list1)
#     return list1
# def helper(dict1,list1):
#     for key,value in dict1.items():
#         list1.append(key)
#         if isinstance(key,dict):
#             helper(value,list1)
#         list1.append(value)
#         # print(list2)
#     return list1


# print(flattening(example))
print("hello")
