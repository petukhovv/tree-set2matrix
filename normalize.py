import os
import json

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.TimeLogger import TimeLogger


def normalize(input_folder, output_folder, all_features_file, normalize_type):
    with open(all_features_file, 'r') as all_features_file_descriptor:
        all_features_json = all_features_file_descriptor.read()
        all_features = json.loads(all_features_json)

    def ast_file_process(filename, all_features):
        tl = TimeLogger()
        with open(filename, 'r+') as features_file_descriptor:
            features_json = features_file_descriptor.read()
            features = json.loads(features_json)

            for feature in all_features:
                if feature not in features:
                    features[feature] = 0

            if normalize_type == 'matrix':
                feature_values = [value for (key, value) in sorted(features.items())]
            else:
                feature_values = features

            relative_filename = os.path.relpath(filename, input_folder)
            output_file = output_folder + '/' + relative_filename
            with open(output_file, 'w') as features_normalized_file_descriptor:
                features_normalized_file_descriptor.write(json.dumps(feature_values))

        print(filename + ' normalize completed. Time: ' + str(tl.finish()))

    FilesWalker.walk(input_folder, lambda filename: ast_file_process(filename, all_features))
