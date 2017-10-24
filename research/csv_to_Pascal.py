import os
import sys
import glob
import pandas as pd

import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('csvs', False, 'Path to the CSV inputs')
FLAGS = flags.FLAGS

def create_xml_item(images, row):
    xml = ['<annotation verified="yes">']
    xml.append('  <folder>' + images + '</folder>')
    xml.append('  <filename>' + row['filename'].split('/')[-1] + '</filename>')
    xml.append('  <path>' + row['filename'] + '</path>')
    xml.append('  <source><database>Unknown</database></source>')
    xml.append('  <size><width>' + str(row['width']) + '</width><height>' + str(row['height']) + '</height><depth>3</depth></size>')
    xml.append('  <segmented>0</segmented>')
    xml.append('  <object>')
    xml.append('    <name>' + row['class'] + '</name>')
    xml.append('    <pose>Unspecified</pose>')
    xml.append('    <truncated>0</truncated>')
    xml.append('    <difficult>0</difficult>')
    xml.append('      <bndbox>')
    xml.append('        <xmin>' + str(row['xmin']) + '</xmin>')
    xml.append('        <ymin>' + str(row['ymin']) + '</ymin>')
    xml.append('        <xmax>' + str(row['xmax']) + '</xmax>')
    xml.append('        <ymax>' + str(row['ymax']) + '</ymax>')
    xml.append('      </bndbox>')
    xml.append('  </object>')
    xml.append('</annotation>')
    return '\n'.join(xml)

def csv_to_pascal(path):
    for csv_file in glob.glob(path + '/*.csv'):
        csv = pd.read_csv(csv_file)
        for index, row in csv.iterrows():
            xml = create_xml_item(path, row)
            # If not exists, create the file
            new_file = path + os.path.splitext(row['filename'].split('/')[-1])[0] + '.xml'
            fp = open(new_file, 'w+')
            print(new_file)
            fp.write(xml)
    return True


def main():
    csv_path = FLAGS.csvs
    if csv_path == False:
        print("must pass in csvs flag")
        sys.exit(1)

    csv_to_pascal(csv_path)
    print('Successfully converted csv to Pascal.')


main()