# -*- coding: utf-8 -*- #
# Copyright 2021
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility script for SemEval Tasks"""
"""*********************************************************************************************"""
#   Synopsis     [ Scripts for    ]
#   Author       [ Shammur A Chowdhury ]

"""*********************************************************************************************"""

import pandas as pd
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


## Function to create train test from the folds given
## in the task data
def get_train_dev(test_fold_id, table):
    test = table[test_fold_id]
    tables = []
    index = 0
    while index < len(table):

        if index != test_fold_id:
            tables.append(table[index])
        index += 1
    train = pd.concat(tables, ignore_index=True)
    return train, test




## Evaluation function for both the task
def evaluation_meaure(preds, labels):
  # calculate accuracy using sklearn's function
  acc = accuracy_score(labels, preds)
  pre = precision_score(labels, preds)
  recall = recall_score(labels, preds)
  f1 = f1_score(labels, preds,average='binary')
  f1M = f1_score(labels, preds, average='macro')

  return {
      'accuracy': acc,
      'Precision': pre,
      'Recall': recall,
      'F1': f1,
      'F1macro':f1M
  }
