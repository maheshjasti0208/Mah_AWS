# Author: Nirmallya Mukherjee
#
# This program is provided as part of the training and does not carry any warranty
# Using this code in any other context will be at your own risk.
#

import csv

def binary_csv_counting():
    #Reading line a normal file and parsing the content, nothing specific to csv as such
    with open("inpfile1.csv", encoding = 'utf-8') as inpFile:
        for line in inpFile:
            print("Line is", line)
            one = zero = 0
            for i in range(len(line)):
                if(line[i] == '1'):
                    one += 1
                elif(line[i] == '0'):
                    zero += 1
            print("The number of 1 are %s and 0 are %s" %(one, zero))


#This csv file has the following header line
#Year-Month,Agency Number,Agency Name,Cardholder Last Name,Cardholder First Initial,Description,Amount,Vendor,Transaction Date,Posted Date,Merchant Category Code (MCC)
def read_with_header():
    with open('card-spend-fiscalyear-2014.csv', 'r', newline='') as ccspendfile:
        num_lines_to_read = 10
        #Leveraging CSV specific operations, becomes easy to address the columns via header names
        reader = csv.DictReader(ccspendfile)
        for line in reader:
            print(line['Year-Month'], line['Cardholder First Initial'], line['Description'], line['Amount'])
            num_lines_to_read -= 1
            if num_lines_to_read <=0:
                break;


def main():
    binary_csv_counting()
    read_with_header()

if __name__ == "__main__":
    main()
