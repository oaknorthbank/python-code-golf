# Python-Code-Golf
Tax calculator task for python code golf

Refactoring Golf is a game designed to stretch your refactoring muscles and to get you to explore your IDE to see what's really possible using shortcuts and automation. The idea is to focus on one aspect of coding and see how far it can be pushed.

This repository contains multiple versions of a simple class to calculate tax on a payslip.

- The first 5,000 is tax free
- Up to 20,000 is taxed at 10%
- Up to 40,000 is taxed at 20%
- Above 40,000 is taxed at 40%

Each version is a refactoring of the previous version. Sticking with the golf metaphor, each version is called a "hole".

Your goal is to refactor from each hole to the next safely and efficiently, using the features of the IDE with as few "strokes" as possible, where a stroke is an action that changes the code. Every stroke costs you points.

## Scoring

- 0 points for formatting and selection
- 1 point for every change made to the code using a shortcut or automated IDE feature (e.g., an automated refactoring, code template, rename, or Find/Replace)
- 2 points for every manual edit. Note that a single "edit" could cover multiple lines of code.
- There is a double points penalty for changes that leave the code failing the tests or not compiling.
- Allow yourselves a maximum of 2 attempts at each round to determine your best score.
- Tests must be run after each "stroke"

## Hints

If you can't remember the shortcut for something, right clicking and pressing "Show Context Items" can be useful
Local history can be very useful in intellij IDEs
Commit code to your branch frequently to make rolling back changes easier

## Running

1. pipenv install
2. pipenv run pytest
3. create a new branch to commit code to

inspired by  https://github.com/sf105/refactoring-golf/tree/trunk
