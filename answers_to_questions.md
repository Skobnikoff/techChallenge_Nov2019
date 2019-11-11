### Explain in your own words, what is the Hypothesis Testing Methodology?

As it is often done in statistics, the conclusions about the whole population of the data
are based on one or multiple samples. Not only because the data is scarce but also because
statistical science assume that hidden processes generating the data of a population are
the same as one generating samples of that population.

Hypothesis Testing is a classical approach in statistics used to infer the true nature
of the analyzed data: its distribution and underlying parameters 
(mean, variance, skewness and so on).

It is done by comparing 2 or more hypothesis (hence the name of the method).
One hypothesis is considered as default one (Null hypothesis) and all the others are
alternatives. If some of alternative hypothesis manages to be accepted it becomes a new
Null hypothesis. If none of alternative hypothesis is accepted, then the Null hypothesis
is considered as the true one (with a certain level of confidence, typically 95%, or 
5% error).

Knowing the nature of the data is useful in many ways: predictions, anomaly detection,
data simulation and so on.


### When building models, explain the process, how you would go about measuring the accuracy and performance of your model?

When I build models, the process looks as following:
1) understand the problem and underlying ML solution: classification, regression, 
    time series prediction, anomaly detection or clustering.
2) explore the data: is it balanced? highly variable? Dense? etc
3) define the limitations (depends on the step 1 et 2): interoperability of the model,
    prediction speed, training speed, memory consumption, aversion of false positives, 
    number of clusters or something else.
4) define a measure of the model performance in accordance to its limitations 
    and overall goal: 
    - interoperability of the model (highly subjective and works only for basic models): 
        number of trees, of tree leaves, of rules.
    - prediction speed, training speed: time in seconds
    - memory consumption: percentage of CPU/GPU or RAM consumed during the model execution,
        disk space occupied
    - the overall prediction accuracy: maximizing F1-score when the data is unbalanced, rarely basic accuracy (needs balanced dataset)
    - aversion of false positives: maximizing recall
    - aversion of false negatives: maximizing precision
    - clustering: cluster purity or F-measure, many others can be used as well
5) label the data (if supervised learning) 
6) split the data on a train and test sets
7) train the model on a train set, use the cross-validation
8) validate the model with the validation set. If not satisfactory, try to understand why, go back to the previous steps
9) delivery


### What is the difference between Machine Learning and Artificial Intelligence?

Artificial intelligence does not have a single definition. It is a broad field of a scientific research aiming to 
increasingly improve the overall intelligence of computers and machines. The intelligence manifests in autonomy of 
taking decisions, high adaptability to the new environment, ability to learn, reason and create.

Artificial intelligence relies on a mix of other sciences: neuroscience, cognitive science, psychology, statistics, 
math, computer science, optics, mechanics, biology, linguistics and others.

Machine learning is an important part of artificial intelligence which deals with learning from experience.
Experience means data. ML has an algorithmic toolset, it leverages methods from statistics, calculus, graph theory,
computer science. 

Machine learning in contrast to artificial intelligence does not aim to make a machine generally intelligent but
specifically good at such narrow tasks like price prediction, image classification, anomaly detection, clustering
clients, converting speech to text and vice versa, and thousand of other use cases.




