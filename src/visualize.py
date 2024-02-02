#!/usr/bin/env python3

import argparse
import os
import json
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-interactive mode
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

# Open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# Normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# Get the top 10 items
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]

# Extract labels and values for the bar chart
labels, values = zip(*items)

# Create a bar chart using matplotlib
# plt.bar(labels, values)
plt.bar(range(len(labels)), values)
plt.xlabel(args.input_path.split(".")[1])
plt.ylabel('Number of Tweets')
plt.title(f'Top 10 {args.key} Twitter Usage By {args.input_path.split(".")[1]}') # (Percentage)' if args.percent else f'Top 10 {args.key}')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.xticks(range(len(labels)), labels, rotation=45, ha='right') 

plt.tight_layout()

# Save the bar chart to a PNG file in the current directory
output_file = f'top_10_{args.key}_by_{args.input_path.split(".")[1]}_chart.png'
plt.savefig(output_file)

# Inform the user about the saved file
print(f'Bar chart saved to {output_file}')

