import itertools
import matplotlib.pyplot as plt

# Function to simulate the path based on a sequence of moves
def simulate_path(path):
    """
    Simulates the path based on the sequence of moves ('U' and 'L') 
    and returns the list of coordinates.
    """
    x, y = 0, 3 # Starting at (0, 3)
    coordinates = [(x, y)]  # Storing the start coordinates
    
    # Apply each move in the path
    for move in path:
        if move == 'U':
            x += 1
            y += 1  # Moving up
        elif move == 'L':
            x += 1
            y -= 1  # Moving down
        coordinates.append((x, y))   # Adding the new coordinates to the list
    
    return coordinates

# Function to generate all combinations of 3 U's and 4 L's
def combinations():
    moves = ['U'] * 3 + ['L'] * 4  # 3 U's and 4 L's
    unique_paths = set(itertools.permutations(moves))  # Generate all unique permutations
    return unique_paths

# Function to plot the paths
def plot_paths(paths):
    """
    Plots all valid paths based on their coordinates.
    """
    plt.figure(figsize=(10, 6))  # Set the figure size

    for path in paths:
        coordinates = simulate_path(path)  # Get the coordinates for the path
        x_values, y_values = zip(*coordinates)  # Separate x and y coordinates
        
        plt.plot(x_values, y_values, marker='o')  # Plot the path with markers
    
    # Defining the y - and x - axis 
    plt.title("Total paths between (0,3) and (7,2)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()  # Display the plot

# Example usage
path_combinations = combinations()  # Get all possible combinations
print(f"Total number of combinations: {len(path_combinations)}")

# Plot all the paths
plot_paths(path_combinations)