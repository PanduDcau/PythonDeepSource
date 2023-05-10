# Breast-Cancer-Prediction

# Introduction


Breast cancer is the most common malignancy among women, accounting for nearly 1 in 3 cancers diagnosed among women in the United States, and it is the second leading cause of cancer death among women. Breast Cancer occurs as a results of abnormal growth of cells in the breast tissue, commonly referred to as a Tumour. A tumour does not mean cancer - tumours can be benign (not cancerous), pre-malignant (pre-cancerous), or malignant (cancerous). Tests such as MRI, mammogram, ultrasound and biopsy are commonly used to diagnose breast cancer performed. Since the labels in the data are discrete, the predication falls into two categories, (i.e. Malignant or benign). In machine learning this is a classification problem.

Other Issues in the Domain (along with the chosen issue) – 
=============================================================
	i. Breast Cancer Prediction
	ii. Twitter Sentiment Analysis
	iii. Heart Attack Detection

Breast Cancer is often neglected or hard to diagnose, this is the very reason that compelled us to choose this issue.


1.1.	Problem Definition
===========================

The goal is to classify whether the breast cancer is benign or malignant and predict the recurrence and non-recurrence of malignant cases after a certain period. To achieve this, we have used machine learning classification methods to fit a function that can predict the discrete class of new input.

1.2.	Objectives
===================
•	The goal is to classify whether the breast cancer is benign or malignant and predict the recurrence and non-recurrence of malignant cases after a certain period.  
•	Using  machine learning classification methods to fit a function that can predict the discrete class of new input.
•	Compare the accuracies of different ML algorithm prediction on the given dataset.

1.3.	Methodology
===================
The dataset is checked for any null values and cleaned. If the class are in string type then change them into integers. After the dataset is cleaned then explore the data for feature extraction. Now split the clean data into train and test dataset. Run the classifier model and predict the accuracy for test dataset.

Logistic Regression:
====================
The logistic model is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick. This can be extended to model several classes of events such as determining whether an image contains a cat, dog, lion, etc.
We can understand the working of Logistic Regression algorithm with the help of the following steps −

	Step 1: Load the data
	Step 2:Logistic Regression measures the relationship between the dependent variable and the independent variables, by estimating probabilities using its underlying logistic function.
	Step 3: These probabilities must then be transformed into binary values in order to actually make a prediction using the sigmoid function. 
	Step 4: The Sigmoid-Function takes any real-valued number and map it into a value between the range of 0 and 1.
	Step 5: This values between 0 and 1 will then be transformed into either 0 or 1 using a threshold classifier.

Random Forest:
==============
Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes or mean prediction of the individual trees.
We can understand the working of Random Forest algorithm with the help of the following steps −

	Step 1 − First, start with the selection of random samples from a given dataset.
	Step 2 − Next, this algorithm will construct a decision tree for every sample. Then it will get the prediction result from every decision tree.
	Step 3 − In this step, voting will be performed for every predicted result.
	Step 4 − At last, select the most voted prediction result as the final prediction result.

Steps for K-Nearest Neighbor:
=============================
It is one of the most basic yet essential classification algorithms in Machine Learning. It belongs to the supervised learning domain and finds intense application in pattern recognition, data mining and intrusion detection. It is widely disposable in real-life scenarios since it is non-parametric, meaning, it does not make any underlying assumptions about the distribution of data 

We can implement a KNN model by following the below steps:
	
	Step 1 − Load the data
	Step 2 − Initialise the value of k
	Step 3 − For getting the predicted class, iterate from 1 to total number of training data points
	Step 4 − Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
	Step 5 − Sort the calculated distances in ascending order based on distance values
	Step 6 − Get top k rows from the sorted array
	Step 7 − Get the most frequent class of these rows
	Step 8 − Return the predicted class

Steps for Support Vector Machine:
=================================
Support vector classifier is a classifier model for the support vector machine. Support Vector Machine (SVM) is a supervised machine learning algorithm which can be used for both classification or regression challenges. A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labelled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples. In two-dimensional space this hyperplane is a line dividing a plane in two parts where in each class lay in either side.


We can implement a SVM model by following the below steps:

	Step 1: Load the data
	Step 2: Split data into train and test
	Step 3: First, it finds decision boundaries that correctly classify the training dataset.
	Step 4: Pick the decision boundary which has maximum distance from the nearest points (supported vectors) of these two classes as the best one.
	Step 5:  Predict values using the SVM algorithm model
	Step 6:Calculate the accuracy and precision.

                  
1.4.	Software Requirements
==============================
Google Colab: It is a free cloud service, based on Jupyter Notebooks for machine-learning education and research. It provides a runtime fully configured for deep learning and free-of-charge access to a robust GPU. Colaboratory allows you to use and share Jupyter notebooks with others without having to download, install, or run anything on your own computer other than a browser. Colab allow user to run bash commands. It provides free GPU and TPU access to the user to run machine learning and deep learning problem.

1.5.	Tool Description
===========================
**Numpy** - NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

**pandas** - pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

**Matplotlib** - Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.

**RandomForestClassifier** - Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes or mean prediction of the individual trees.


**LogisticRegression** - The logistic model is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick. This can be extended to model several classes of events such as determining whether an image contains a cat, dog, lion, etc.

**SVC** - Support vector classifier is a classifier model for the support vector machine. Support Vector Machine (SVM) is a supervised machine learning algorithm which can be used for both classification or regression challenges.


# Implementation


2.1.	Design & Implementation
================================
Breast Cancer Wisconsin Dataset is provided by UCI Machine Learning. Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. There are two attribute Information provided, ID number and Diagnosis (M = malignant, B = benign). And ten real-valued features are computed for each cell nucleus:  a) radius (mean of distances from center to points on the perimeter) b) texture (standard deviation of gray-scale values) c) perimeter d) area e) smoothness (local variation in radius lengths) f) compactness (perimeter^2 / area - 1.0) g) concavity (severity of concave portions of the contour) h) concave points (number of concave portions of the contour) i) symmetry j) fractal dimension ("coastline approximation"). The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. 


2.1.1. Implementation Mechanism
================================
Data preprocessing is a crucial step for any data analysis problem. It is often a very good idea to prepare your data in such way to best expose the structure of the problem to the machine learning algorithms that you intend to use. First, the data should be loaded using pandas. Drop the unnecessary column like ID, which is irrelevant to our model. Next check for null values in the dataset if any, clean the rows.


2.1.2.	Major Considerations for Implementation 
================================
One of the issues that we faced was the value for attribute “class” were in string type, we had to change it to integer type, so that it can be our target class. We accomplish this task by using LabelEncoder provided in sklearn library.


# Results and Discussion

To improve SVM model prediction, we standardized out data. On running the algorithms on standardised data, it was found that SVM should significant improvement from merely 62.8% before to 97.2% now. Based on new accuracy results, Logistic Regression, Random Forest and Support Vector Machine show promising results.

# Conclusion
	1. The Objective of the project was to predict whether the tumour is malignant or benign.
	2. Different Algorithms were used to make prediction using the feature dataset.
	3. Logistic Regression provided highest accuracy of 95%, which is slightly higher than K-Nearest Neighbour.
	4. While Support Vector Machine gave the worst accuracy for prediction.
	5. Upon standardizing data, we get good accuracy results using logistic regression, Random Forest and Support Vector Machine, correctly classifying tumour into malignant or benign almost 95-97% of times.
