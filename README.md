
<p align="center">
  <img src="https://github.com/shammur/PRESUP/blob/main/pretens_logo.png" width="350" title="PRESUP">
<!--   <img src="your_relative_path_here_number_2_large_name" width="350" alt="accessibility text"> -->
</p>

# SemEval 2022 Task 3
# Presupposed Taxonomies: Evaluating Neural Network Semantics (PreTENS) 

<!-- [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) -->

> **⚠ New Notice:**
> Evaluation Phase has started, please check the data folder for test data and sample_data for correct submission format. Updated rules are vailable in the task website. CodaLab links are given below.

## FAQ and Submission Rules

- **Maximum Submission**: 3 result submissions per subtask
- **Ranking**: Two ranking per subtask - Per Language Ranking and Global Ranking
- **What results will be displayed/used in the LeaderBoard**: All the measures given in baseline script (Precision, Recall, F1 and F1-macro for subtask1 and Rho for subtask2) will be shown, but the final ranking will be based on macro F1 and Rho.
- **The naming convention for submission file**: The result/submission file will be tab separated (with headers: ID \t Labels/Score), named as answer.tsv and then compressed to a zip file with naming convention: <teamName_subtaskX_submissionNo.zip>, X={1,2} and No={1,2,3}
- **Results selected to display in Leaderboard**: Each team will have 3 chances (per task) and from there they can choose which results to submit in the leaderboard. However, each team must submit at least one result in the board (they can change the selected entry to show anytime during competition). This is mainly given so participants attempting just selected language are not penalized by the global-ranking score mechanism.

## Tasks

PreTENS includes the two following sub-tasks: 
- a binary classification: Predicting the acceptability of sentences (**A (1)** _vs_ **UA (0)**)
<!-- - , which consists in predicting the acceptability label assigned to each sentence of the test set; -->
- a regression task: Predicting the degree of Acceptance in a seven Likert-scale
<!-- - , which consists in predicting the average score assigned by human annotators on a five Likert-scale with respect to the subset of data evaluated via crowdsourcing. -->


## Data
The data comprise of sentences in 3 languages:  **English**, **Italian**, and **French**. 

For each sub-task and each language: 
- The dataset will be split into training and test set
- Additionally, a trail data (a small subset of training set) is released to give participants a proper idea of the data and expected formats.


For the **binary-classification** sub-task, the training and test set will be composed by ~5,000  and 23,000 samples, respectively;
For the **regression** sub-task, ~500 sentences will be provided for the training set and a bigger for the test set.

Sample/Trail data for Evaluation Campaign: data/trail

Data Format:

**ID    Sentence    LABELS/SCORE**

where LABEL is for binary classification task and SCORE is for the regression task.
SCORE: represent average of the assigned score (1-7) given by the annotator. Details of scales and agreements will be elaborated/updated later.
The LABEL (1/0) is assigned based on the regression score.

## Evaluation Measures
The official evaluation metrics for the Classification tasks are:
**Precision**, **Recall**, **F1-measure** and **macro F-measure** (See the sub-Task1 starter code for more details)

As for the Regression, we opt for **MSE**, **RMSE** and **Spearman Correlation** (rho) (See the sub-Task2 starter code for more details)

<!-- ## Formating and Evaluation Scripts -->

> **⚠ NOTICE:**
>For each sub-task a separate baseline is defined: i) for the binary classification sub-task baseline, a Linear Support Vector classifier using n-grams (up to three) as input features is used, and ii) as for the regression sub-task, a baseline using a Linear Support Vector regressor with the same n-grams features is provided. Participants can run the evaluation system and obtain the results by using different cross-validation configurations on the training set. Due to the presence in the official test-set of additional constructions with the same presuppositional constraints, we have found that applying the baseline methods on the official test-set yields results that are from 10% to 20% lower than the training set. This highlights the importance of achieving a great deal of syntactic generality on this task. For this reason we encourage to test different cross-validation configurations on the training set.


To get our participant started with the Task, we provide baseline scripts showing how the data is processed, splited and in the end -- evaluated for the said task.

Below are the baseline and starter code:

**_Subtask1_**:
https://colab.research.google.com/drive/1wDFQnEfMkoJY99Bmv-CfsTsdwleCDg2f?usp=sharing

**_Subtask2_**: 
https://colab.research.google.com/drive/18KwrdyTsp3wOPcaB7pyFnqOSc3Te7p-X?usp=sharing

You can also find the necessary codes in this git repository (SemEval_Task3_Baseline_subtask1.ipynb and SemEval_Task3_Baseline_subtask2.ipynb)

## License

MIT

## Useful links

   [Task Website](<https://sites.google.com/view/semeval2022-pretens>)
      
   [Participants Registration Form](<https://docs.google.com/forms/d/e/1FAIpQLSfS1oIjxCifghMFPpxPOpu-8HC8lJutXa65BXfpXpOmxcJ_Wg/viewform>)
   
   Evaluation Platforms:
   [Subtask1] (https://codalab.lisn.upsaclay.fr/competitions/1292)
   [Subtask2] (https://codalab.lisn.upsaclay.fr/competitions/1290)


   mailinglist: semeval2022-task3@googlegroups.com
   
## Organizers

Shammur Absar Chowdhury - Qatar Computing Research Institute, HBKU, Qatar

Dominique Brunato - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Cristiano Chesi - University School for Advanced Studies (IUSS), Pavia, Italy

Felice Dell'Orletta - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Simonetta Montemagni - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Giulia Venturi -  Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Roberto Zamparelli - Department of Psychology and Cognitive Science - University of Trento, Italy

For any queries:
**Contact**: semeval2022-task3-organizers@googlegroups.com
