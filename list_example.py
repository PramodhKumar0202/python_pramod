# example 1
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
    print(f"{task}")

# example 2
grades = [85,92,78,90,88]

grades.append(100)

avg_grade =sum(grades)/len(grades)
print(f"average grade: {avg_grade:.2f}")

highest_grade =max(grades)
lowest_grade =min(grades)

print(f"highest grade: {highest_grade}")
print(f"lowest grade: {lowest_grade}")

#example 3
inventory =["apples","bananas","oranges","grapes"]

inventory.append("strawberries")

inventory.remove("bananas")
# checking 

item="oranges"
if item in inventory:
    print(f"{item} are in stock")
else:
    print(f"{item} are out of stock")


#printing the inventory
print("inventory list")

for item1 in inventory:
    print(f"{item1}")

#example 4

# Collecting user feedback
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")