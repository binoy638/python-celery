# import our cooking_task from tasks
from main import cooking_task

# Dishes ordered for Table-1
table_1_dishes = ["Chicken Biryani", "Lemon chicken", "Pepper chicken"]

# Call the cooking_task.delay task with input parameters defined for that Task.
result = cooking_task.delay("Table-1", table_1_dishes)

# prints the task id
print(result)
