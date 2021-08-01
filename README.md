
<p align="center">
  <img src="https://github.com/shammur/PRESUP/blob/main/pretens_logo.png" width="350" title="PRESUP">
<!--   <img src="your_relative_path_here_number_2_large_name" width="350" alt="accessibility text"> -->
</p>

# SemEval 2022 Task 3
# Presupposed Taxonomies: Evaluating Neural Network Semantics (PreTENS) 

<!-- [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) -->

## Tasks

PreTENS includes the two following sub-tasks: 
- a binary classification: Predicting the acceptability of sentences (**A** _vs_ **UA**)
<!-- - , which consists in predicting the acceptability label assigned to each sentence of the test set; -->
- a regression task: Predicting the degree of Acceptance in a five Likert-scale
<!-- - , which consists in predicting the average score assigned by human annotators on a five Likert-scale with respect to the subset of data evaluated via crowdsourcing. -->


## Data
The data comprise of sentences in 3 languages:  **English**, **Italian**, and **French**. 

For each sub-task and each language: 
- The dataset will be split into training and test set
- Additionally, a trail data (a small subset of training set) is released to give participants a proper idea of the data and expected formats.


For the **binary-classification** sub-task, the training and test set will be composed by 10,000  and 23,000 samples, respectively;
For the **regression** sub-task, 1,000 sentences will be provided for the training set and 600 for the test set.

Sample/Trail data for Evaluation Campaign: data/trail

Data Format:

**ID    SENT    LABEL/AVG_SCORE**

where LABEL is for binary classification task and AVG_SCORE is for the regression task.
AVG_SCORE: represent average of the assigned score (1-7) given by the annotator. Details of scales and agreements will be elaborated/updated later.
The LABEL (1/0) is assigned based on the regression score.

## Evaluation Measures
**Coming Soon**

## Formating and Evaluation Scripts

**Coming Soon**

## License

MIT

## Useful links

   [Task Website] (<https://sites.google.com/view/semeval2022-pretens>)
   
   Competition Link: Coming Soon
   
   [Participants Registration Form](<https://docs.google.com/forms/d/e/1FAIpQLSfS1oIjxCifghMFPpxPOpu-8HC8lJutXa65BXfpXpOmxcJ_Wg/viewform>)
   
   mailinglist: semeval2022-task3@googlegroups.com
   
## Organizers

Dominique Brunato - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Cristiano Chesi - University School for Advanced Studies (IUSS), Pavia, Italy

Shammur Absar Chowdhury - Qatar Computing Research Institute, HBKU, Qatar

Felice Dell'Orletta - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Simonetta Montemagni - Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Giulia Venturi -  Institute for Computational Linguistics "A. Zampolli" (CNR), Pisa, Italy

Roberto Zamparelli - Department of Psychology and Cognitive Science - University of Trento, Italy


**Contact**: semeval2022-task3-organizers@googlegroups.com
