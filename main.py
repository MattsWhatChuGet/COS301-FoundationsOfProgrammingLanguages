# Title: Homework 01: PMPVI Program
# By: Matthew Patterson

# Variables
literals = ["+", "-", "(", ")", "=", " "]
userTokens = []
userVariableTokens = {}
isLooping = True

# Functions
def TokenizeInput(input):
    curIndex = 0
    curToken = ""

    # Iterate through input
    for i in input:
        if i not in literals:
            # 'i' is not a literal, thus is part of curToken
            curToken += i
            if curIndex == len(input) - 1:
                # If this is the end of the input, submit the curToken.
                SubmitCurrentToken(curToken)
                curToken = ""
        elif i != " ":
            # i is literal, and not white space. This means we submit the curToken to the list.
            SubmitCurrentToken(curToken)
            curToken = ""
            userTokens.append(i)
        curIndex += 1

def SubmitCurrentToken(curToken):
    # If token is a number, convert token to int and append to token
    if curToken.isnumeric():
        userTokens.append(int(curToken))
    # Non-numerical tokens are variables.
    elif curToken.isalpha():
        userTokens.append(curToken)

def EvaluateTokens(arrayOfTokens):
    operand1, operand2 = "", ""
    operator = "+"
    curTotal = 0

    while len(arrayOfTokens) > 0:
        i = arrayOfTokens.pop(0)

        if userTokens.count("=") == 1:
            # If this is an assignment expression store evaluated value into variable.
            arrayOfTokens.pop(0)
            userVariableTokens[i] = EvaluateTokens(arrayOfTokens)
            return ""
        elif userTokens.count("=") > 1:
            print("ERROR: Too many '='")
            break
        else:
            if i == "(":
                # Start recursive call to evaluate parenthesis before parental loop to maintain proper priority.
                if operand1 == "":
                    operand1 = EvaluateTokens(arrayOfTokens)
                elif operand2 == "":
                    operand2 = EvaluateTokens(arrayOfTokens)
                    curTotal += EvaluateCurExpression(operand1, operator, operand2)
            elif i == ")":
                return curTotal
            elif i in literals:
                operator = i
            # This is the logic state where only non-literal tokens exist.
            elif operand1 == "":
                if i in userVariableTokens.keys():
                    operand1 = userVariableTokens.get(i)
                else:
                    operand1 = i
                if len(userTokens) == 0:
                    curTotal = EvaluateCurExpression(curTotal, operator, operand1)
                    operand1 = ""
                    operand2 = ""
            elif operand2 == "":
                if i in userVariableTokens.keys():
                    operand2 = userVariableTokens.get(i)
                else:
                    operand2 = i
                curTotal += EvaluateCurExpression(operand1, operator, operand2)
                operand1 = ""
                operand2 = ""
    return curTotal

def EvaluateCurExpression(operand1, operator, operand2):
    match operator:
        case "+" | "":
            return operand1 + operand2
        case "-":
            return operand1 - operand2

# The Start of the Program
while isLooping:
    TokenizeInput(input())
    if userTokens.count("(") is userTokens.count(")"):
        print(EvaluateTokens(userTokens))
    else:
        print("ERROR: Missing a open/closing parentheses.")

    # Clear Tokens for loop
    userTokens.clear()