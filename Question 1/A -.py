def copy(dict):
    dictionary = {}
    for key in dict:
        dictionary[key] = dict[key]
    return dictionary


def create_dictionary(entire_list, dict):
    skill_list = []
    for i in range(1, 6):
        skill_list.append(entire_list[i])
    dict[entire_list[0]] = skill_list


num_participants = int(input())
dictionary_participants = {}
for i in range(num_participants):
    data = input().split()
    create_dictionary(data, dictionary_participants)

num_projects = int(input())
dictionary_projects = {}
for i in range(num_projects):
    data = input().split()
    create_dictionary(data, dictionary_projects)



# dictionary_projects_iteration = copy(dictionary_projects)
# dictionary_participants_iteration = copy(dictionary_participants)
# dictionary_final = {}
# for project in dictionary_projects_iteration:
#     selected_list = [0, 0, 0, 0, 0]
#     skill = 0
#     # 0 for HTML, 1 for Python, 2 for DSA, 3 for Java, 4 for SQL
#     for participant in dictionary_participants_iteration:
#         if dictionary_projects[project][skill] == 0:
#             skill += 1
#         elif dictionary_projects[project][skill] <= dictionary_participants[participant][skill]:
#             selected_list[skill] = participant
#             del dictionary_participants[participant]
#             skill += 1
#         if skill == 5:
#             break
#     if skill == 5:
#         dictionary_final[project] = selected_list
#         del dictionary_projects[project]
#
# # Now we are left with some participant and some projects in our dictionaries
