# fixedwidthgenerators

# Python "Challenge" code

_Sep 2020_
## Assumptions
- needs to be quick to read
- demonstrate understanding of iteration, conditionals, file handles and string manipulation
- demonstrate Python Syntax comprehension, basic programming norms - naming conventions 
- use base python
- Parser has access to 'spec.json' to anticipate fixed document structure, rather than interpreting from file

## Approach
- Simple python3 with expected libraries
- Quick refactoring without over complication (Don't boil the ocean)
- Pytest to validate expected functionality of data generation during refactoring
- Functional approach where possible - avoid side effects, obviously file writing is a mutation
- Work steps in main() function

## Build/Run
### use python
- Download the code
- From the command prompt navigate to the folder \fixedwidthgenerators-master\fixedwidthgenerators-master>
- python src/fixedfilegenerator.py
```python src/fixedfilegenerator.py```
- Output files will be genrated in the following location as per the sample output \fixedwidthgenerators-master\fixedwidthgenerators-master\





###
Sample output: 


- D:\Vikram\Projects\Test\fixedwidthgenerators-master\fixedwidthgenerators-master>python src/fixedfilegenerator.py
- Enter the number of lines to generate a fixed length file:13
- Enter the delimiter whcih you want to use generate the file,
- columnheadings: ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
- columnwidths: ['5', '12', '3', '2', '13', '7', '10', '13', '20', '13']
- Please refer fixed file :: D:\Vikram\Projects\Test\fixedwidthgenerators-master\fixedwidthgenerators-master\fixed.txt and csv file :: -D:\Vikram\Projects\Test\fixedwidthgenerators-master\fixedwidthgenerators-master\snake.csv



# Limitations
- file names are constants
- code is only for use based on supplied specification
- no qualifying questions were enabled to elicit full requirements



# Data Engineering Coding Challenges


## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

