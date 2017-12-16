import os
import json

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.TimeLogger import TimeLogger


def matrix2csv(input_file, output_file):
    with open(input_file, 'r') as matrix_file_descriptor:
        matrix_json = matrix_file_descriptor.read()
        matrix = json.loads(matrix_json)

    vectors = []

    i = 0
    for vector in matrix:
        try:
            print(str(i) + ' appended.')
            vectors.append(','.join(str(x) for x in vector))
        except TypeError:
            with open('exceptions.log', 'a') as ex_file_descriptor:
                ex_file_descriptor.write(json.dumps(vector) + os.linesep + os.linesep)
            print(str(i) + ' TypeError exception.')

        i += 1

    csv = os.linesep.join(vectors)

    with open(output_file, 'w') as csv_file_descriptor:
        csv_file_descriptor.write(csv)
