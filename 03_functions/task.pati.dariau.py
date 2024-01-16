def print_task(task_list: list, hide_done=False) -> None:
    for index, task in enumerate(task_list):
        if task['done']:
            is_done = "x"
        else:
            is_done = "-"
        print(f"{index:4}[{is_done}] {task['name']}")

def add_task(task_list: list, task_name: str, done=False) ->list:
    task = {'name' : task_name, 'done': done}
    task_list.append(task)
    return task_list

def mark_done(task_list: list, task_index: int) -> list:
    task_status = task_list[task_index]['done']
    task_status = not task_status
    task_list[task_index]['done'] = task_status
    print(f"Task{task_list[task_index]['name']} is now {task_status}")
    return task_list

def remove_task(task_list: list, task_index: int) -> list:
    removed_task = task_list.pop(task_index)
    print (f"Remove task: {removed_task['name']}")
    return task_list

def input_task_index(task_list: list) -> int:
    print_task(task_list)  
    task_index = input('Choose Task ID: ')
    if task_index.isnumeric():
        task_index = int(task_index)
    else:
        print('Error: Wrong Task ID, it must be a number')
        return None
    if task_index > len(task_list) or task_index <0:
        print('Error: Task ID is too high or negative')
        return None
    return task_index
    
def main(task_list):
    while True:
        print("---[Task ]---")
        print("9: Exit")
        print("1: Print all task")
        print("11: Print only undonne task")
        print("2: Add a task")
        print("3: Mark task done/undone")
        print("4: Remoce a task")
        choice = input("Choice:")
        if choice.startswith("0"):
             break
        elif choice.startswith("1"):
            if choice.startswith("11"):
              print_task(task_list, True)
            else:  
                print_task(task_list)
        elif choice.startswith("2"):
            task_list = add_task(task_list, input("Task name:"))
        elif choice.startswith("3"):
            task_list = mark_done(task_list, input_task_index(task_list))
        elif choice.startswith("4"): 
            task_list = remove_task(task_list, input_task_index(task_list))  
        else:
            print("Error: Bad choice! Try Again.")

main([])