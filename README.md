
<p align="center">
  <img src="https://github.com/shammur/PRESUP/blob/main/pretens_logo.png" width="350" title="PRESUP">
<!--   <img src="your_relative_path_here_number_2_large_name" width="350" alt="accessibility text"> -->
</p>

# SemEval 2022 Task 3
# Presupposed Taxonomies: Evaluating Neural Network Semantics (PreTENS) 

<!-- [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) -->

## Tasks

PreTENS includes the two following sub-tasks: 
- a binary classification: Predicting the acceptability of sentences (**A (1)** _vs_ **UA (0)**)
<!-- - , which consists in predicting the acceptability label assigned to each sentence of the test set; -->
- a regression task: Predicting the degree of Acceptance in a five Likert-scale
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

**ID    Sentence    LABEL/SCORE**

where LABEL is for binary classification task and SCORE is for the regression task.
SCORE: represent average of the assigned score (1-7) given by the annotator. Details of scales and agreements will be elaborated/updated later.
The LABEL (1/0) is assigned based on the regression score.

## Evaluation Measures
The official evaluation metrics for the Classification tasks are:
**Precision**, **Recall**, **F1-measure** and **macro F-measure** (See the sub-Task1 starter code for more details)

As for the Regression, we opt for **MSE**, **RMSE** and **Spearman Correlation** (rho) (See the sub-Task2 starter code for more details)

## Formating and Evaluation Scripts

!!! note
> A single baseline evaluation is defined: for both sub-tasks we used a Linear Support Vector classifier that uses n-grams (up to three) as input features. Participants can run the evaluation system and obtain the results by using different cross-validation configurations on the training set. Due to the presence in the official test-set of additional constructions with the same presuppositional constraints, we have found that applying the baseline methods on the official test-set yields results that are from 10% to 20% lower than the training set. This highlights the importance of achieving a great deal of syntactic generality on this task. For this reason we encourage to test different cross-validation configurations on the training set. 

To get our participant started with the Task, we provide baseline scripts showing how the data is processed, splited and in the end -- evaluated for the said task.

Below are the baseline and starter code:

**_Subtask1_**:
https://colab.research.google.com/drive/1wDFQnEfMkoJY99Bmv-CfsTsdwleCDg2f?usp=sharing

**_Subtask2_**: 
https://colab.research.google.com/drive/18KwrdyTsp3wOPcaB7pyFnqOSc3Te7p-X?usp=sharing

You can also find the necessary codes in this git repository

## License

MIT

## Useful links

   [Task Website](<https://sites.google.com/view/semeval2022-pretens>)
      
   [Participants Registration Form](<https://docs.google.com/forms/d/e/1FAIpQLSfS1oIjxCifghMFPpxPOpu-8HC8lJutXa65BXfpXpOmxcJ_Wg/viewform>)
   
   mailinglist: semeval2022-task3@googlegroups.com
   
## Organizers

Shammur Absar Chowdhury - Qatar Computing Research Institute, HBKU, Qatar

Dominique Brunato - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Cristiano Chesi - University School for Advanced Studies (IUSS), Pavia, Italy

Felice Dell'Orletta - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Simonetta Montemagni - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Giulia Venturi -  Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Roberto Zamparelli - Department of Psychology and Cognitive Science - University of Trento, Italy


**Contact**: semeval2022-task3-organizers@googlegroups.com
