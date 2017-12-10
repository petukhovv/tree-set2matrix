# ast-set2matrix

Program for step-by-step conversion of AST set to the matrix (dataset) using ast2vec

Available steps (stages):
- asts2vectors: ast from specified input folder conversion to vectors in specified output folder (with same path);
- sparse_transformation: convert vectors (but actually is map "feature-value") to sparse representation (two formats: matrix or map);
- normalize: normalization feature values by the number of all features in the current file;
- collect_statistic: collection features statistic (create sorted lists with features and their frequency for specified n).
