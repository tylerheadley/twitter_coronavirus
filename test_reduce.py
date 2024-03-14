#!/usr/bin/env python3

import argparse
import os
import json
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive mode
import matplotlib.pyplot as plt
from collections import defaultdict

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# Initialize data structure to store tweet counts per hashtag per day
#data = defaultdict(lambda: defaultdict(int))
data = {}

# Load data from input paths
for hashtag in args.hashtags:
    data[hashtag] = []
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            if hashtag in tmp:
                data[hashtag].append(sum(tmp[hashtag].values()))

# Create a line plot for each hashtag
for hashtag in args.hashtags:
    x_values = range(len(data[hashtag]))
    y_values = data[hashtag]

    plt.plot(x_values, y_values, label=f'{hashtag}')

# Add labels and title
plt.xlabel('Day of the Year')
plt.ylabel('Number of Tweets')
plt.title('Tweet Counts by Hashtag Over the Year')

# Add legend
plt.legend()

# Save the line plot to a PNG file
plt.savefig(args.output_path)

# Inform the user about the saved file
print(f'Line plot saved to {args.output_path}')
