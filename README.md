# ast-set2matrix

Program for step-by-step conversion of AST set to the matrix (dataset) using [**ast2vec**](https://github.com/PetukhovVictor/ast2vec)

Available steps (stages):
- **asts2vectors**: ast from specified input folder conversion to vectors in specified output folder (with same path);
- **sparse_transformation**: convert "vectors" (but actually is map "feature-value") to sparse representation (two formats: matrix or map);
- **normalize**: normalization feature values by the number of all features in the current file;
- **collect_statistic**: collection features statistic (create sorted lists with features and their frequency for specified n).

## Input
### asts2vectors

* **-s, --stage** -> asts2vectors;
* **-i, --input_folder**: input folder with ASTs (in JSON format);
* **-o, --output_folder**: output folder with "vectors" (but actually is map "feature-value");
* **--ast2vec_path**: path to [ast2vec](https://github.com/PetukhovVictor/ast2vec)

Also see ast2vec README: https://github.com/PetukhovVictor/ast2vec (ASTs format, output format, etc)

#### Example of use
```
python3 main.py -i ./ast -o ./test -s asts2vectors --ast2vec_path ../ast2vec/
```
