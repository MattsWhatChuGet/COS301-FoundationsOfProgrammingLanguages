# COS 301 Homework 03
# By Matthew Patterson

# Table of Contents
    1. Overview
    2. Behavior
    3. Development Entries
    4. Input & Output Notes

# 1. Overview
This README has three primary functions:
    1. To articulate the desired behavior for clarity in understanding.
    2. To log entries of my process to track my thinking, attempts, success/failures, etc.
       to keep from running in circles.
    3. Notes on example inputs and outputs.

# 2. Behavior
The purpose of this assignment it to expand upon HW02/calc.py to implement a one-dimensional `List`.

    ## 2.1: Lists
        A grouping of evaluated expressions inside parenthesis, separated by commas,
    with the output having a trailing comma. Each value is to be manipulated as expressions as well.

    ### REQUIRED BEHAVIORS ([*]/[ ] = is/isn't implemented) ###
        [ ] 2.1.0: Always output surrounded with () (not []) and a trailing comma
                (1, 2, 3) -> (1, 2, 3,)
                         !-> [1, 2, 3]
        [*] 2.1.1: Expressions in list with numbers and/or variables are evaluated
               x = 2
               (1, 1+1, x+1) -> (1, 2, 3,)
        [ ] 2.1.2: Distribute Negative
                -(1, 2, 3) -> (-1, -2, -3,)
        [ ] 2.1.3: List to list operators, index to index.
               (1, 2, 3) + (2, 4, 6) -> (3, 6, 9,)
               (1, 2, 3) * (2, 2, 2) -> (2, 4, 6,)
        [*] 2.1.5: Single token in list
            (1,) -> (1,)
        [*] 2.1.6: No comma = not list
            (1) -> 1
        [*] 2.1.7: Nested Parenthesis are just expressions
            (1, (1+1), 3) -> (1, 2, 3,)
        [ ] 2.1.8: Last value of shorter list is applied to remaining indexes
            (3, 4) + (1, 1, 2) -> (4, 5, 6)

# 3. Development
This section is a pseudo-journal entry of my process in figuring out the task.

    ## 3.1 Anticipation of Process
    1. Define the RegEx pattern for a List.
    2. Write rules for the different situations a List will be in to match the expected behavior


    ## 3.2 Defining a List

        1. Created p_list(p) to parent listItems.
            1.1 Defined as: "list : '(' listItems ')'"
        2. Created p_listItems(p) to child a list
            2.1 Defined as: '''listItems : listItems ',' expression | expression ',' '''' with count conditionals.
        3. p_expression_list(p) to allow list to be an expression derivative.
            3.1 "expression : list"

        [SUCCESS] Working behaviors thus far:
            2.1.1
            2.1.6
            2.1.7

        [ERRORS]:
            All other behaviors are not working.

    ## 3.3 List Operator Grammar

        I am prioritizing data manipulation over behavior 2.1.0 for now.

        [Success 2.1.6] Added more conditions in p_listitems and changed some logic to allow for one expression with a comma to be
        defined as a list.

        To get the remaining behaviors, I need to have some list grammar rules defined
        comparable to p_expression_binop(p) function but for lists.

        1. Created p_expression_listOp(p)

        Added a print statement to each expression function for debugging.


