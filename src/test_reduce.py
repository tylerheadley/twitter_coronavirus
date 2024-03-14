#!/usr/bin/env python3

import argparse
import os
import json
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive mode
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# Initialize data structure to store tweet counts per hashtag per day
data = defaultdict(list)

# Load data from input paths
for hashtag in args.hashtags:
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            if hashtag in tmp:
                data[hashtag].append(sum(tmp[hashtag].values()))

# Convert x-axis values from days of the year to dates in MM/DD or MM-DD format
dates = [datetime.strptime(f'2024-01-01', '%Y-%m-%d').strftime('%m/%d') for _ in range(365)]

# Create a line plot for each hashtag
for hashtag in args.hashtags:
    x_values = dates[:len(data[hashtag])]
    y_values = data[hashtag]

    plt.plot(x_values, y_values, label=f'{hashtag}')

# Add labels and title
plt.xlabel('Date (MM/DD)')
plt.ylabel('Number of Tweets')
plt.title('Tweet Counts by Hashtag Over the Year')

# Add legend
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Save the line plot to a PNG file
plt.savefig(args.output_path)

# Inform the user about the saved file
print(f'Line plot saved to {args.output_path}')
