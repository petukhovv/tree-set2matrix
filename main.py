import os
import argparse
import subprocess

from lib.helpers.FilesWalker import FilesWalker
from lib.helpers.TimeLogger import TimeLogger

parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', '-i', nargs=1, type=str, help='folder with ASTs')
parser.add_argument('--output_folder', '-o', nargs=1, type=str,
                    help='Output folder with files, which will contain ast_features and feature values as JSON')
parser.add_argument('--ast2vec_path', nargs=1, type=str, help='path to ast2vec repo')
args = parser.parse_args()

python_interpreter = 'python3'
input_folder = args.input_folder[0]
output_folder = args.output_folder[0]
ast2vec_path = args.ast2vec_path[0]


def ast_file_process(filename):
    tl = TimeLogger()
    relative_filename = os.path.relpath(filename, input_folder)
    output_file = output_folder + '/' + relative_filename
    output_folders = os.path.dirname(output_file)
    if not os.path.exists(output_folders):
        os.makedirs(output_folders)
    subprocess.call([python_interpreter, ast2vec_path + '/main.py', '-i', filename, '-o', output_file])
    print(output_file + ' feature extraction completed. Time: ' + str(tl.finish()))


FilesWalker.walk(input_folder, ast_file_process)
