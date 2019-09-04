#!/usr/bin/env python3
import argparse
import json
import re

"""
Count all the possible outcomes (traces) starting from a user-defined origin.
@author Ruud de Jong
@license MIT
"""

data = {}
all_counts = {}


def count(key):
    global data
    global all_counts

    if key not in data:
        raise KeyError("Key '{}' was not found in the grammar. Misspelled or not in top level of JSON.".format(key))

    # We've already counted this key. Just return that.
    if key in all_counts:
        return all_counts[key]

    all_counts[key] = 0
    count_for_key = 0

    children = data[key]
    for val in children:

        new_starts = re.findall("#([^#]+)#", val)

        if len(new_starts) == 0:
            # Nothing to expand in this child. Just add one.
            count_for_key += 1
        else:
            # Expand a #variable#.
            # Multiply if we have multiple #variables# in #one# #sentence#.
            multiplied_count = 1
            for s in new_starts:
                s = s.split(".")[0]
                multiplied_count *= count(s)  # Recursive

            count_for_key += multiplied_count

    all_counts[key] = count_for_key
    return count_for_key


def main():
    global data

    parser = argparse.ArgumentParser(description="Count the number of possible traces of a Tracery grammar.")
    parser.add_argument("file", help="the JSON file containing your grammar")
    parser.add_argument("-o", "--origin", help="name of the node from which to start counting", default="origin")
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        data = json.load(file)

        origin = args.origin
        print("Starting point '{}' has {} possible traces.".format(origin, count(origin)))


if __name__ == "__main__":
    main()
