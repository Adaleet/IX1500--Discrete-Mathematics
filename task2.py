import itertools
import matplotlib.pyplot as plt

# Reuse the factorial and combinations functions from Task 1 if needed for binomial calculations.

# Function to simulate a downward move
def L(m, n):
    return (m+1, n-1)

# Function to simulate an upward move
def U(m, n):
    return (m+1, n+1)

# All the possible combinations of U and L:
def combinations():
    totalMoves = ['U'] * 3 + ['L'] * 4  # 3 U's and 4 L's
    unique_paths = set(itertools.permutations(totalMoves))  # Generate all unique permutations
    return unique_paths

# Reuse the simulate_path function from Task 1
def simulate_path(path):
    """
    Simulates the path based on the sequence of moves ('U' and 'L') 
    and returns the list of coordinates.
    """
    # Start at (0, 3)
    x, y = 0, 3
    coordinates = [(x, y)]  # Start coordinate
    
    # Apply each move in the path
    for move in path:
        if move == 'U':
            x, y = U(x, y)  # Use U function to move up
        elif move == 'L':
            x, y = L(x, y)  # Use L function to move down
        coordinates.append((x, y))  # Add the new coordinates
    
    return coordinates

# Function to filter paths that cross (3,0) or (5,0)
def valid_paths(combinations):
    # Use list comprehension to simulate paths and check if they cross (3,0) or (5,0)
    return [simulate_path(path) for path in combinations if (3, 0) in simulate_path(path) or (5, 0) in simulate_path(path)]

#Plotting all the valid paths for task 2: 
def plot_paths(paths):
    """
    Plots all valid paths based on their coordinates.
    """
    plt.figure(figsize=(10, 6))  # Set the figure size

    for path in paths:
        x_values, y_values = zip(*path)  # Separate x and y coordinates
        plt.plot(x_values, y_values, marker='o')  # Plot the path with markers
    
    # Defining the y - and x - axis 
    plt.title("Paths Crossing the X-axis at (3,0) or (5,0)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()  # Display the plot

# Plotting the valid paths given the constraints
path_combinations = combinations()  # Generate all possible combinations
valid_paths = valid_paths(path_combinations)  # Filter paths that cross (3, 0) or (5, 0)

# Plot the valid paths
plot_paths(valid_paths)

# Print the valid paths
for path in valid_paths:
    print(" -> ".join([f"({x},{y})" for x, y in path]))

# Display the number of valid paths
print(f"Number of valid paths: {len(valid_paths)}")

