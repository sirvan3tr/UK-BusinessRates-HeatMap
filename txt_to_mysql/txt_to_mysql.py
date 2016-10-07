import csv

smryval10 = 'C:/Users/salmasi/Documents/MATLAB/business_rates/2010-summaryvaluations.csv';
entries10 = 'C:/Users/salmasi/Documents/MATLAB/business_rates/2010-summaryvaluations.csv';
entries10historic = 'C:/Users/salmasi/Documents/MATLAB/business_rates/2010-summaryvaluations.csv';

with open(smryval10, 'r') as f:
    #first_line = f.readline()
    head = [next(f) for x in range(30)]

for i in head:
    print(i)


# https://azure.microsoft.com/en-gb/documentation/articles/sql-database-develop-python-simple/

