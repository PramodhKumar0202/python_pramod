to_do_list=["Buy Groceries","Clean the house","Pay bills"]

## Adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go For a Run")

## Removing a completed task
to_do_list.remove("Clean the house")

## checking if a task is in the list
if "Pay bills" in to_do_list:
    print("Don't forgrt to pay the utility bills")

print("To Do List remaining")
for task in to_do_list:
    print(f"-{task}")