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
```python3 src/main.py```
### use python environment
```python3 -m venv venv```

```source venv/bin/activate```

```pip install -r requirements.txt```

```python src/main.py```
### use docker
Because why not make it more complicated and bonus points right?

Build current code into image: 

```docker build -t mypyreader .```

Check image was created: 

```docker images```

Run current code: 

```docker run --rm -v $(pwd)/:/code mypyreader```

Shell to run the code in docker container? 

```docker run -i -t mypyreader /bin/bash```



# Limitations
- program is to be run from root directory
- file line endings are *nix
- file names are constants
- code is only for use based on supplied specification
- no qualifying questions were enabled to elicit full requirements


## References
https://forge.medium.com/how-to-identify-a-smart-person-in-3-minutes-57f058cd5561

https://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/


https://seeknuance.com/2008/02/15/interview-whiteboard-coding-tests-are-usually-worthless/

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

