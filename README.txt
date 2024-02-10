# COS 301 Homework 02
# By Matthew Patterson

# Table of Contents
    0. Overview
    1. Behaviors
        1.0 Two New Operators
            1.0.0 The Modulos Behavior
            1.0.1 The Floor Division Behavior
        1.1. Float or Integer Return Behavior
            1.1.0 Explicitly a Float
            1.1.1 Floats as Necessary
    2. Documentation
        2.0 Implementing Operators


# 0. Overview
    This document serves two primary purposes.
        0. To explain the behavior this program is intended to have.
        1. To serve as a documentation of my process for note-taking and context.

    The behavior of this program is an edited version of `ply.calc.py` that implements two additional behaviors:
        0. Two new operators: the modulos ('%') and floor division ('//').
        1. Returns floats only when decimals are explicitly invoked or necessary.

    The documentation section will be quasi-journal entries of my reason, attempts, and results of working through
the implementation process. This is for both my own utility of tracking what I have tried and also as context
for the end state of this assignment.

    I also am using a numerical system to organize and also make certain points referable.

# 1. Behaviors
    For the sake of exercising my own clarity as well as confirmation for you that I understand the desired behavior,
this section describes the various behavior elements that is to be implemented in this assignment.

## 1.0 Two New Operators
    This section describes the expected return value of each new operator.

### 1.0.0 The Modulos Behavior ('%')
    It returns the remainder of a division expression.
Examples:
    - 4%2 returns 0 because 2 goes into 4 evenly, therefore there is no remainder (4%2 = 2R0).
    - 19%4 returns 1 because 4 goes into 19 four times evenly (4*4=18) with a remainder of 1 (19%4 = 4R1).

### 1.0.1 The Floor Division Behavior ('//')
    Returns the lowest integer of a division expression.
In other words, it removes values past a decimal, resulting in an integer.
Examples:
    - 5/2 returns 2.5
    - 5//2 returns 2, because the floor is the lowest whole number.


## 1.1 Float or Integer Return Behavior
The return value of an expression should always be an integer,
Unless:
    Rule 0: A float is explicitly invoked. Examples:
        - 1 + 1 returns 2.
        - 1 + 1.0 returns 2.0.
    Rule 1: An expression's return value can only be answered accurately with a float. Examples:
        - 10//2 returns 5 (NOT 5.0), as a decimal is unnecessary for a correct answer.
        - 5/2 returns 2.5, a float is necessary for accuracy.


# 3. Documentation
    In this section I will note my reasoning, pseudocode, and attempts with their results with each issue.

## 3.0 Implementing Operators
    To start, I observed existing code to approximate needed changes.

Here are a list of my starting observations:
    3.0.0. Adding the new chars to the `literals` array.
    3.0.1. Appending new operators to `precedence`
    3.0.2. Appending new expressions in `p_expression_binop(p)`. Both in the comment string, and the `if` statements.

That was the only observations I had on my first read through. I made these observations to day HW02 was assigned.
This leads me to my first, and biggest mistake, I assumed the HW as fairly simple and prioritized other assignments
and obligations that had more impending deadlines/family things. Before I knew it, it's now the weekend prior to
this due date.

Now, here's where I start to actually implement my assumptions:
    3.0.0. Appending Literals[]:
        0a Added "%" to array, no problem.
        0b [ERROR] '//' was not added. The lexer only allows single chars literals.
            - Instantly, to me this insinuates that there might be a need to edit more than just `calc.py`,
                however nothing has been mentioned yet in class about editing `lexer`,
                so I will ignore this for now.
            - Perhaps there's a way to use the existing '/' char.
            - I continued to the next observation for now.
    3.0.1. Appending Precedence
        1a. Wasn't sure how too, start with adding it to the '('left', '*', '/')` section.
            - [ERROR] yacc was unable to build the parser adding anything to that section.
            - This is where the fear really started to sink in.
            - I removed my additions, and continued to the next one.
    3.0.2 Appending '...binop(p)' string & if
        2a [SUCCESS] Added ''| expression '%' expression' to string and the appropriate elif condition.
            - Ran the program, and the % returned expected results.
        2b [ERROR] Tried doing the same with '//', as expected, yacc couldn't parse it.
            - Removed changes and then wondered what to do next.