# Priyanka-piping-map-reduce
# Data details
While searching kaggle i found Health insurance coverage is the best dataset that contains 14 coloumns.
# Content
This dataset provides health insurance coverage data for each state and the nation as a whole, including variables such as the uninsured rates before and after Obamacare, estimates of individuals covered by employer and marketplace healthcare plans, and enrollment in Medicare and Medicaid programs.
# [Raw data links](https://www.kaggle.com/hhs/health-insurance)
# Commands   
``cat states.csv | python 22mapper.py > output2.txt``   
``cat states.csv | python 22mapper.py | sort | python 22reducer.py > output.txt``
# Chart Title
![image](https://user-images.githubusercontent.com/77811257/153538675-30e81ed9-9741-43f8-9668-5ecfba416108.png)

