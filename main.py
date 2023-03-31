#Anna Kūliņa 14.grupa 221RDB057

def main():

  n = int(input())
  numuri = {}

  while(n):
    komanda = input().split()
    if komanda[0] == "add":
        if len(komanda) == 3:
          numuri[komanda[1]] = komanda[2]
        else:
          print("wrong input")
    elif komanda[0] == "del":
        if komanda[1] in numuri:
            del numuri[komanda[1]]
    elif komanda[0] == "find":
        if komanda[1] in numuri:
            print(numuri[komanda[1]])
        else:
            print("not found")
    


if __name__ == "__main__":
    main()

# # python3

# class Query:
#     def __init__(self, query):
#         self.type = query[0]
#         self.number = int(query[1])
#         if self.type == 'add':
#             self.name = query[2]

# def read_queries():
#     n = int(input())
#     return [Query(input().split()) for i in range(n)]

# def write_responses(result):
#     print('\n'.join(result))

# def process_queries(queries):
#     result = []
#     # Keep list of all existing (i.e. not deleted yet) contacts.
#     contacts = []
#     for cur_query in queries:
#         if cur_query.type == 'add':
#             # if we already have contact with such number,
#             # we should rewrite contact's name
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     contact.name = cur_query.name
#                     break
#             else: # otherwise, just add it
#                 contacts.append(cur_query)
#         elif cur_query.type == 'del':
#             for j in range(len(contacts)):
#                 if contacts[j].number == cur_query.number:
#                     contacts.pop(j)
#                     break
#         else:
#             response = 'not found'
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     response = contact.name
#                     break
#             result.append(response)
#     return result

# if __name__ == '__main__':
#     write_responses(process_queries(read_queries()))