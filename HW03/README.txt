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
        [ ] 2.1.5: Single token in list
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

{!}{!} I am so sorry I wasn't able to properly finish this assignment. Life has been hectic.

        Between my 4 kids (My 10 year old daughter and 8 year old son that have both been diagnosed with severe ADHD
        that we are homeschooling, and twins) , taking care of my wife with postpartum depression (so juggling 99% of
        all household things by myself), and with my wife's aunt who is the last of 2 people from her huge family she has
        in her life was in the hospital for surgery. It wasn't looking good for a while, but she was able to recover
        and had her visit this weekend which took alot of time to prep.

        The twins have come down with a stomach bug a few days ago and I have been trying to avoid getting that as I gear up
        to finish the paper work to receive a CUGR grant I was awarded that also has a deadline in a few days.

        I had to take my Van in for inspection early last week - that didn't pass and I have over $1k worth of work I
        need to get done. Been scrambling to try and figure that out.

        Not to mention that the hose to my CPAP machine is leaking because my teething babies bit into it one morning,
        so I have been getting awful sleep and all this insane stress has flared up my psoriasis.

        It is almost 1AM 3/6/24, I have dumped at least 15 hours into this assignment today alone
        and I reluctantly must submit code that doesn't work, and I resent it.

        If I had more time, I could figure it out - but alas that's not an option here.

        Sorry to belly ache, but I legitimately feel like a complete failure when I can't make a deadline for a project.
        I am sorry I wasn't able to juggle all this stuff to show my best work.

        Hopefully I will do better on the next homework.

Me attempting to derive the grammar:

 0  1     2        3               4                            5                   6
_S_ > _E_ > _list_ > (_listitems_) > _listitems_ , [expression] > _listitems_ [E,E] > [E,E,E]

0. Statement                _(1,2,3)_
1. Expression (E)           _(1,2,3)_
2. List                     _(1,2,3)_
3. listitems                _1,2,3_
4. listitems [E]            _1,2_ [3]   _1,2_ , [3]
5. listitems [E, E]         _1_ [2,3]   _1_ , [2,3]
6. [E,E,E]                  [1,2,3]

































