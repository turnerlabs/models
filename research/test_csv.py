import os
import sys
import glob
import pandas as pd

import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('csv', False, 'Path to the CSV input')
FLAGS = flags.FLAGS

def test_csv(csv_file):
    csv = pd.read_csv(csv_file)
    for index, row in csv.iterrows():
        if row['xmin'] >= row['xmax'] or row['ymin'] >= row['ymax']:
            print row['filename']

    return True


def main():
    csv_path = FLAGS.csv
    if csv_path == False:
        print("must pass in csv flag")
        sys.exit(1)

    test_csv(csv_path)

main()