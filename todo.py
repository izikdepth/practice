import argparse

# define command line arguments 
parser = argparse.ArgumentParser()
parser.add_argument('action', choices = ['add', 'view', 'remove'], help = 'action to perform')
parser.add_argument('task', nargs = '?', default='', help='task description')
parser.add_argument('due', nargs = '?', default='', help = 'due date')
args =  parser.parse_args()

# define file name to store inputs
filename = 'tasks.txt'

# Perform action based on command-line arguments
"""
if action is 'add', we create/ open a new file with task description and date provided in the command.

"""
if args.action == 'add':
    with open(filename, 'a') as file:
        file.write(f'{args.task},{args.due}\n')
        print(f'Task "{args.task}" added with due date {args.due}')
elif args.action == 'view':
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                task, due = line.strip().split(',')
                print(f'{i}. {task} - Due date: {due}')
    except FileNotFoundError:
        print('No tasks found')
        
elif args.action == 'remove':
    try:
        task_number = int(args.task)
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            for i, line in enumerate(lines, start=1):
                if i != task_number:
                    file.write(line)
            print(f'Task {task_number} removed')
    except (ValueError, IndexError):
        print('Invalid task number')
        

"""
To run the program, the user can type commands like:
python todo.py add Buy milk 2023-04-15
python todo.py view
python todo.py remove 1


"""