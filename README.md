# Technical Competency Test Senior Data Scientist

This repository contains the codebase for exercises from the technical competency test.

This README provides information on how to run the programs and what the logic behind.

The repository contains data samples under the `/data` folder.

## Ex 1: (Golang) Algorithm: Separator Detection in CSV Files

Code location: `sep_detector/detect_sep.go`

**To test the code** do the following steps:
1) make sure you have a Go language installed `export PATH=$PATH:/usr/local/go/bin`
2) clone this repository in the `$GOPATH/src` OR if you cloned it in another 
    directory then move the sep_detector folder in `$GOPATH/src`
3) make sure you have the compiled Go apps in your path: 
`export PATH=$PATH:$GOPATH/bin`
4) `cd sep_detector`
5) build the go application: `go install`
6) to run the program execute the following command in the terminal:
`sep_detector <path_to_csv_file>`
7) you can also run a shell script that tests the `sep_detector` with different 
files from the `/data`:
`sh test.sh`


**How sep_detector works?**

The separator detection of CSV files lies on the following assumptions:
 - each line of the input file contains the same number of fields, thus the same number
  of separator symbols
 - portions of text wrapped in quotation marks and brackets are considered as such
   that do not contain the separator inside
 - only double quote `"` is considered as a valid quotation mark
 - only punctuation symbols and tabs are considered as valid separators,
 	 alphanumerical separators are not
 	 
Thus, to find out which character is a separator the program proceeds as follows:
1) read up to first 20 lines of the input file. This number limits the amount of data
 to work with. In the same it is big enough to make sure that there is only 1 winner
  between different candidates for a "separator" status.
2) count the number of each valid character (punctuation + tab) in each of 20 lines.
3) keep only characters that are present in each line AND have the same occurrence 
across all the lines.
4) if up till now there is more than 1 candidate, select the one with the higher
 frequency in each line.

Shortcomings:
 - files which EOL is not "\n" can still be handled but there are risks of bugs
 - too many assumptions, that make this program potentially poorly perform on 
    non standard CSV files
    
Further development:
 - removing text in quotes and brackets may be done in a more elegant manner. 
    More options may be added.
 - the punctuation from western languages can be completed by punctuation from other
    languages.
 - the separation character may be generalized to any possible character or any 
    combination of characters.
 - the whole approach to tackle the problem may be changed from hard coded rules to
    machine learning problem: given a training set of various CSV files we may create a 
    predictive model that can handle special cases.