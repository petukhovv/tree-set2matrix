import argparse

from asts2vectors import asts2vectors
from normalize import normalize
from collect_statistic import collect_statistic

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_folder', '-o', nargs=1, type=str,
                    help='Output folder with files, which will contain ast_features and feature values as JSON')
parser.add_argument('--ast2vec_path', nargs=1, type=str, help='path to ast2vec repo')
parser.add_argument('--normalize_type', choices=['matrix', 'map'])
parser.add_argument('-n', nargs='*', default=[1, 2, 3], help='n for collect n-grams statistic')
parser.add_argument('--stage', '-s', choices=['asts2vectors', 'normalize', 'collect_statistic'])
args = parser.parse_args()

input_folder = args.input_folder[0]
output_folder = args.output_folder[0]
stage = args.stage

if stage == 'asts2vectors':
    ast2vec_path = args.ast2vec_path[0]
    all_feature_file = output_folder + '/all_features.json'
    asts2vectors(input_folder, output_folder, ast2vec_path, all_feature_file)
elif stage == 'normalize':
    normalize_type = args.normalize_type[0]
    all_feature_file = input_folder + '/all_features.json'
    normalize(input_folder, output_folder, all_feature_file, normalize_type)
elif stage == 'collect_statistic':
    all_feature_file = input_folder + '/all_features.json'
    n = args.n
    collect_statistic(output_folder, all_feature_file, n)
