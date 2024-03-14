#!/usr/bin/env python3

import argparse
import os
import json
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive mode
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime, timedelta

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# Initialize data structure to store tweet counts per hashtag per day
data = defaultdict(lambda: defaultdict(int))

# Load data from input paths
for hashtag in args.hashtags:
    for path in args.input_paths:
        with open(path) as f:
            tmp = json.load(f)
            if hashtag in tmp:
                for date_str, count in tmp[hashtag].items():
                    date = datetime.strptime(date_str, "%Y-%m-%d")  # Assuming dates are in ISO format
                    day_of_year = date.timetuple().tm_yday
                    data[hashtag][day_of_year] += count

# Create a line plot for each hashtag
for hashtag in args.hashtags:
    x_values = list(data[hashtag].keys())
    y_values = list(data[hashtag].values())

    plt.plot(x_values, y_values, label=f'{hashtag}')

# Add labels and title
plt.xlabel('Date (MM-DD)')
plt.ylabel('Number of Tweets')
plt.title('Tweet Counts by Hashtag Over the Year')

# Add legend
plt.legend()

# Save the line plot to a PNG file
plt.savefig(args.output_path)

# Inform the user about the saved file
print(f'Line plot saved to {args.output_path}')
