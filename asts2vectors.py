import os
import subprocess
import json
from pprint import pprint
from os import path

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.TimeLogger import TimeLogger

python_interpreter = 'python3'


def collect_features_statistic(features_file, all_features_file):
    with open(features_file, 'r') as features_file_descriptor:
        features_json = features_file_descriptor.read()
        features = json.loads(features_json)

        with open(all_features_file, 'r+') as all_features_file_descriptor:
            all_features_json = all_features_file_descriptor.read()
            all_features = json.loads(all_features_json) if all_features_json else {}
            for feature in features:
                if feature in all_features:
                    all_features[feature] += features[feature]
                else:
                    all_features[feature] = features[feature]

            all_features_file_descriptor.seek(0)
            all_features_file_descriptor.write(json.dumps(all_features))
            all_features_file_descriptor.truncate()


def asts2vectors(input_folder, output_folder, ast2vec_path):
    all_features_file = output_folder + '/all_features.json'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not path.isfile(all_features_file):
        open(all_features_file, 'a').close()

    def ast_file_process(filename):
        tl = TimeLogger()
        relative_filename = os.path.relpath(filename, input_folder)
        output_file = output_folder + '/' + relative_filename
        output_folders = os.path.dirname(output_file)
        if not os.path.exists(output_folders):
            os.makedirs(output_folders)
        subprocess.call([python_interpreter, ast2vec_path + '/main.py',
                         '-i', filename, '-o', output_file, '--no_normalize'])
        collect_features_statistic(output_file, all_features_file)
        print(output_file + ' feature extraction completed. Time: ' + str(tl.finish()))

    FilesWalker.walk(input_folder, ast_file_process)
