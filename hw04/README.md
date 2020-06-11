# COMP 364 - Computer Tools for Life Sciences (Fall 2017)
## Assignment #4 : Machine learning in cheminformatics
### Due: Monday November 27th, 2017 at 11:59:59 pm 

In this COMP 364 assignment you will implement a machine-learned model to predict the median toxic dose (TD<sub>50</sub>) of specific molecules for mice. The TD<sub>50</sub> is the dose of a chemical required to cause an expected toxic effect in 50% of cases. For more information about the TD<sub>50</sub>, please see the following links:

**TD<sub>50</sub> Wikipedia:** https://en.wikipedia.org/wiki/Median_toxic_dose<br/>
**TD<sub>50</sub> Visual representation:** http://www.derangedphysiology.com/main/core-topics-intensive-care/critical-care-pharmacology/Chapter%202.1.7/median-doses-ld50-ed50-and-td50
     
To begin, download the following machine learning toxicology dataset:

**Chemical dataset:** ftp://ftp.ics.uci.edu/pub/baldig/learning/benigni/ISSCAN_v1a_774_10Dec04.sdf
     
You will notice that the dataset is in an unusual file format, called a **'structure-data file' (SDF)**. An SDF file is a chemical table (describes molecules and chemical reactions) in a human-readable format. For more information, see:

**SDF Wikipedia:** https://en.wikipedia.org/wiki/Chemical_table_file#SDF
     
To parse this file format, we will need to update our Python 3 package manager, Anaconda, to include the RDKit module:

 ```
 conda install -c https://conda.anaconda.org/rdkit rdkit
 ```
     
Helpful links/tutorials for the assignment overall:

**NumPy API:** https://docs.scipy.org/doc/numpy-1.13.0/reference/<br/>
**Matplotlib API:** https://matplotlib.org/2.0.2/api/index.html<br/>
**RDKit API:** http://www.rdkit.org/docs/api/index.html<br/>
**RDKit tutoral:** http://www.rdkit.org/docs/GettingStartedInPython.html
