import os
import json

from .lib.helpers.FilesWalker import FilesWalker
from .lib.helpers.TimeLogger import TimeLogger

JSON_LEFT_ARRAY_BRACKET = '['
JSON_RIGHT_ARRAY_BRACKET = ']'
JSON_COLON = ','


def create_file_if_needed(output_file):
    if not os.path.isfile(output_file):
        open(output_file, 'a').close()
        return True
    return False


def vectors2matrix(input_folder, output_file):
    output_folder = os.path.dirname(output_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    params = {
        'files_map': []
    }

    def vectors_file_process(filename, params):
        tl = TimeLogger()
        with open(filename, 'r') as vector_file_descriptor:
            vector_json = vector_file_descriptor.read()

            is_beginning = create_file_if_needed(output_file)

            with open(output_file, 'a') as output_file_descriptor:
                prefix = JSON_LEFT_ARRAY_BRACKET if is_beginning else JSON_COLON
                output_file_descriptor.write(prefix + vector_json)

        print(filename + ' process completed. Time: ' + str(tl.finish()))

        params['files_map'].append(filename)

    FilesWalker.walk(input_folder, lambda filename: vectors_file_process(filename, params))

    with open(output_file, 'a') as output_file_descriptor:
        output_file_descriptor.write(JSON_RIGHT_ARRAY_BRACKET)

    with open(output_folder + '/files_map.json', 'w') as files_map_file_descriptor:
        files_map_file_descriptor.write(json.dumps(params['files_map']))
