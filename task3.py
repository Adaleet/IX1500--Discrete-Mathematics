import itertools
import matplotlib.pyplot as plt

def L(m, n):
    return (m+1, n-1)

# Function to simulate an upward move
def U(m, n):
    return (m+1, n+1)

# Function to simulate the path, check if it's valid, and return the coordinates
def validated_path(path):
    x, y = 0, 3   # Start at (7, 6)
    coordinates = [(x, y)]  # Start with the initial coordinates

    # Simulate the path and check for validity
    for move in path:
        if move == 'U':
            x, y = U(x, y)  # Move up
        elif move == 'L':
            x, y = L(x, y)  # Move down

        # If the path crosses or touches the x-axis, mark it as invalid
        if y <= 0:
            return False, []  # Invalid path

        coordinates.append((x, y))  # Store the new coordinates

    # Check if the path ends at (20, 5)
    return (x, y) == (7, 2), coordinates  # Return whether it's valid and the path

# Function to generate all valid paths and their coordinates
def combinations():
    totalMoves = ['U'] * 3 + ['L'] * 4  # 3 U's and 4 L's
    all_paths = set(itertools.permutations(totalMoves))  # Generate unique permutations
    valid_paths = []

    # Validate and store only valid paths
    for path in all_paths:
        is_valid, coordinates = validated_path(path)
        if is_valid:
            valid_paths.append(coordinates)

    return valid_paths

# Function to plot the valid paths
def plot_paths(paths):
    plt.figure(figsize=(10, 6))  # Set the figure size

    # Plot each path
    for path in paths:
        x_values, y_values = zip(*path)  # Separate x and y coordinates
        plt.plot(x_values, y_values, marker='o')

    # Configure the plot's appearance
    plt.title("Valid paths not crossing the x-axis")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()  # Display the plot

# Main code to generate, print, and plot paths
valid_paths = combinations()
print(f"Total number of valid paths: {len(valid_paths)}")

# Plot the valid paths
plot_paths(valid_paths)
