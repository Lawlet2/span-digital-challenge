<p align="center">
  <img src="/docs/images/span-logo.png">
</p>




# CODE CHALLENGE

Span code challenge 
Author: Eduardo A.

## Summary

We want you to create a production ready, maintainable, testable command-line application that will calculate the ranking table for a league.

## Full Problem Statement & Instructions
<p align="center">
  <a src="/docs/challenge/instructions.pdf"
</p>

### [Read more here](/docs/challenge/instructions.pdf) 

## Demo

#### Test the code challenge online here: https://span.eduardo-ac.com

##### If cursor is not showing/blinking, type enter to start 

Run the project with: 

```
python main.py
```
or with:

```
 python main.py --file="games.txt"
```
## Tech Stack

#### Programming language

- Python 3

#### Requirements

- Pyxtermjs 0.5.0.2
- Pytest 7.1.3
- Pytest-mock 3.10.0
- Coverage 6.5.0

## Project File Structure

The project has the following file structure (tree representation)

```
├── README.md                
├── constants.py             
├── docs
│   ├── challenge
│   │   └── instructions.pdf
│   └── images
│       └── span-logo.png
├── games.txt
├── gamesmanager.py
├── main.py
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── test_gamesmanager.py
│   └── test_main.py
```

| File      | Description |
| ----------- | ----------- |
| README.md   | This document     |
| constants.py | Variables for global use|
| docs | Documentation Folder |
| games.txt | Sample input .txt file |
| gamesmanager.py|  Class used to parse the games results, calulate, teams points and return the sorted teams in descending order|
| main.py | Main project file |
| tests | Tests package |


## Installation
TIP: Use virtualenv to run the project

"The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories". Extract from: https://docs.python.org/3.8/library/venv.html

Virtuaelnv installation guide:
https://virtualenv.pypa.io/en/latest/installation.html



#### 1. Install the requirements packages using the pip command

```
pip install -r requirements.txt
```

#### 2. Run the project
There are two ways to run the project, the first one is for standard input from the console (A) and the second way is for pass the .txt file that contains the desired input (B).

- ##### A. Console Input:
    Run the main.py module:

    ```
        python main.py
    ```

    After excute the main file, the console will require the number of games to process:
    ```
     Enter the number of games
     5
    ```
    Then is required to input each game result per new line:
    ```
     Enter the number of games
     5
     Lions 3, Snakes 3
     Tarantulas 1, Tarantulas 0
     Lions 1, FC Awesome 1
     Tarantulas 3, Snakes 1
     Lions 4, Grouches 0
    ```
    And finally the if the program succeed, the console will output
    the following message and the result.txt file has been created:
    ```
    **************************************************
    SPAN CODE CHALLENGE

    Output file: result.txt

    Tip to print the output file: cat result.txt

    **************************************************
    ```
    To print the result, type:
    ```
    cat result.txt
    ```

    :trophy: Congratulations! Your ranking table has been generated

    ```
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
    ```

- ##### B. File Input:
    Run the main.py module with the file argument:

    ```
        python main.py --file="games.txt"
    ```

    If the program succeed, the console will output
    the following message and the result.txt file has been created:
    ```
    **************************************************
    SPAN CODE CHALLENGE

    Output file: result.txt

    Tip to print the output file: cat result.txt

    **************************************************
    ```
    To print the result, type:
    ```
    cat result.txt
    ```

    :trophy: Congratulations! Your ranking table has been generated

    ```
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
    ```

- ##### Error Log

    The program logs an ERROR only the specific input line and the executes the next line till end

    Invalid input sample:

    ```
    SPAN invalid INPUT,,,,,,,,,9999

    DIGITAL invali INPUT,,,,,,,,,9999
    ```

    Logged Error:
    ```
    ERROR:root:Invalid input format, (sample format -> First Team 2, Second Team 5)
    ```

    Then its created and empty input file, but if there's any valid input the result.txt will contain the rankings results of the valid given inputs:
    ```
    **************************************************
    SPAN CODE CHALLENGE

    Output file: result.txt

    Tip to print the output file: cat result.txt

    **************************************************
    ```

## Testing
To run the project's tests follow the next steps:

- If the requirements are not installed, then:

    ```
    pip install -r requirements.txt
    ```
    
- Run pytest:
   ```
    pytest
    ```

- Testing results:
<p align="left">
    <img src="/docs/images/testing-res.png">
</p>

- Also the test coverage package is installed so then to obtain the project's coverage execute:
   ```
    coverage report -m
    ```

- Finally, returns the coverage results:
<p align="left">
    <img src="/docs/images/cov-res.png">
</p>


## Run the console in the browser
Pyxtermjs is a fully functional terminal in your browser. Extract from: https://github.com/cs01/pyxtermjs

This project uses Pyxtermjs to run a console in an AWS EC2 for demo purposes, but also can be executed locally in your machine, to do so just type:

 ```
    pyxtermjs -p 8000
 ```

 After that, a flask server will start to serve the xterm console:

 ```
 pyxtermjs > INFO (main:147) serving on http://127.0.0.1:5000
 * Serving Flask app 'pyxtermjs.app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off

  ```

  NOTE: Remeber to run before:
    ```
    pip install -r requirements.txt
    ```

Then enter to the browser and use the terminal to execute the main.py:
<p align="left">
    <img src="/docs/images/pyxterm.png">
</p>