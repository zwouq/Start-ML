answer = []
substring_to_find = 'кот'

for priority in tasks:
    if priority < 2:
        task_list = tasks[priority]  # Get the list of tasks for this priority
        for task in task_list:
            if substring_to_find.lower() in task.lower():
                answer.append(task)  # Add only the task that contains the substring
                if len(answer) >= 2:
                    break  # Stop adding tasks if the limit is reached
    if len(answer) >= 2:
        break  # Stop iterating through priorities if the task limit is reached
