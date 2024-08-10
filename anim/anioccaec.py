import pandas as pd

# Create example DataFrame
data = {
    'own_goal': [0, 1, 0, 1, 1, 0, 0, 1]
}

gs = pd.DataFrame(data)

# Count unique values in 'own_goal' column
own_goal_counts = gs['own_goal'].value_counts()

# Print the result
print(own_goal_counts)
