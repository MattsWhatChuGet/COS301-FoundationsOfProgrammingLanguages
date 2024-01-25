## COS 301 Foundations of Programming Languages
## Homework Assignment 01: PMPV Language
## Author: Matthew Patterson

# Overview
This program itterates through a user's `input()` one char at a time, determining it's tokens and storing them in their respective lists.
- Literals, integers, and called variables are store in a list.
- Expressions that contain exactly one '=" are determined as an assignment expression. It then iterates to determine the "name" and its `value` and is stored in a Dictionary{"name":value}.
It then itterates through the list of tokens and evaluates the expression and returns the total using conditions and recursion.

## Variables
There are 4 variables declared to start:
	- `literals` is a list of charactors that have special usage (i.e. "+" , "-", "(", ")", "=", " ")
		These litterals will be used as conditional checks throughout the logic flow.
	- `userTokens` is a list of tokens that will be populated via the `TokenizeInput(input)` function.
	- `userVariableTokens` is a Dictionary that stores variable names as keys, and their respective value.
	- `isLooping` is a boolian to handle the outtermost "while" loop to keep the program running.


## Functions
### TokenizeInput(input)
The `input` string is converted into a list of "userTokens", where a function itterates through each char and evaluates the token.
	- It starts with tracking the current index (`curIndex`) and the current token (`curToken`).
	- Itterates through the string using `for i in input:`.
		- if `i` isn't a literal, append it to `curToken`.
			- If its the last char in `input` (using `curIndex`) call `SubmitCurrentToken(curToken)` and clear the `curToken` for the next token to be constructed.
		- if `i` isn't a " " (white space is ignored entirly), call `SubmitCurrentToken(curToken)`, clear `curToken, and appends `i` to `userTokens`.
		- Incrament `curIndex`

### SubmitCurrentToken(curToken)
This simply converts the data type of a string token, using `.isnumeric()` to traffic `int(curToken)` to the token list.

### EvaluateTokens(arrayOfTokents)
Treats the `userTokens` list as a stack, popping the first index, and evaluating what to do.
	- i = arrayOfTokens.pop(0)
	- First, it looks for exactly 1 '=' to determin this list as an assignment expression. (more than 1 is ERROR, none is a nor expression)
		- if it is, then the next char will be '=' and it removes it from the list.
		- then it calls to assign the value of the variable by recurssivly calling this function. ( userVariableTokens[i] = EvaluateTokens(arrayOfTokens) )
		- then returns an empty string.
	- Then it checks if `i` is a "(", if it is then it checks if this is the first operand or second, then recurssivly calls this function to evaluate it's value.
	- if `i` is ")" that means the parenthases expression is concluded and then returns the `curTotal` to exit the nested loop.
	- It then checks to see if there is an expression to evaluate, and then calls `EvaluateCurExpression(operand1, operator, operand2)`.
	- if its the last token in the list, it will pass `curTotal` as operand1.
	- Then clears the operand and operator variables.
	- Final, returns the `curTotal`

### EvaluateCurExpression(operand1, operator, operand2)
Simple looks at the operator string, if its "+" or "-" it adds/subtracts operand2 to/from operand 1 and returns the total.