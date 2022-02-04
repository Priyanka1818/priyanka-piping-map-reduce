# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 14) : 
    State,Uninsured_Rate,Uninsured_Rate2,Uninsured_Rate_Change,Health_Insurance_Coverage_Change,Employer_Health_Insurance_Coverage,Marketplace_Health_Insurance_Coverage,Marketplace_Tax_Credits,Average_Monthly_Tax_Credit,State_Medicaid_Expansion,Medicaid_Enrollment,Medicaid_Enrollment,Medicaid_Enrollment_Change,Medicare_Enrollment = datalist

    # print intermediate key-value pairs to standard output
    print(Uninsured_Rate_Change,"\t",1)
