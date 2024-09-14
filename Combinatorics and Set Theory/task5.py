import matplotlib.pyplot as plt
import itertools


# Define the number of votes for A and B
A = 9
B = 2
total = A + B

# Function to generate all paths from (0, 0) to (total_votes, votes_A - votes_B)
def generate_paths(A, B):
    totalVotes = A + B #  sum of A + B = total moves 

    # Create a list of moves with 'U' representing a vote for A and 'L' for B
    moves = ['U'] * A + ['L'] * B
    
    # Generate all unique permutations of the moves
    unique_paths = set(itertools.permutations(moves))
    
    # Return the paths as a list of strings (e.g., 'UULUL')
    return [''.join(path) for path in unique_paths]

# Generate all paths
paths = generate_paths(A, B)

# Plot the paths -
def plot_paths(paths):
    plt.figure()  # Minimal figure without size specification
    for path in paths:
        x, y = [0], [0]  # Start at (0, 0)
        for move in path:
            x.append(x[-1] + 1)  # Increment x by 1 for each step
            y.append(y[-1] + 1 if move == 'U' else y[-1] - 1)  # Increment or decrement y based on move
        plt.plot(x, y, color='blue', alpha=0.3)  # Plot each path with transparency
    
    plt.show()  # Display the plot without extra elements

# Plot all generated paths
plot_paths(paths)
