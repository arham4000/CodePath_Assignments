# Problem 1

# def manage_stage_changes(changes):
#     stage = []
#     recently_canceled = ""
#     for change in changes:
#         # Adding to stack
#         if change[0] == 'S':
#             stage.append(change[len(change)-1])

#         # Canceling
#         if change[0] == 'C':
#             recently_canceled = stage.pop()

#         # Reschedule
#         if change[0] == 'R':
#             stage.append(recently_canceled[len(recently_canceled)-1])
#     return stage


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Problem 2

from collections import deque 

def process_performance_requests(requests):
    # Set up queue
    requests = deque()

# # Using list sorting all the inputs at once
#     requests.sort(reverse=True)
#     result = []
#     for request in requests:
#         result.append(request[1])


    # append right

    return result

    






print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
