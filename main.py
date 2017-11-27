import os
import json
import argparse
import subprocess
from pprint import pprint

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.TimeLogger import TimeLogger

from asts2vectors import asts2vectors
from normalize import normalize

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_folder', '-o', nargs=1, type=str,
                    help='Output folder with files, which will contain ast_features and feature values as JSON')
parser.add_argument('--ast2vec_path', nargs='?', type=str, help='path to ast2vec repo')
parser.add_argument('--stage', '-s', choices=['asts2vectors', 'normalize', 'vectors2matrix'])
args = parser.parse_args()

input_folder = args.input_folder[0]
output_folder = args.output_folder[0]
stage = args.stage
all_feature_file = output_folder + '/all_features.json'

if stage == 'asts2vectors':
    ast2vec_path = args.ast2vec_path[0]
    asts2vectors(input_folder, output_folder, ast2vec_path, all_feature_file)
elif stage == 'normalize':
    normalize(input_folder, all_feature_file)
