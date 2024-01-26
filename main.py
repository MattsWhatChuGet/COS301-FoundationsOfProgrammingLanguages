# Title: Homework 01: PMPVI Program
# By: Matthew Patterson

# Variables
literals = ["+", "-", "(", ")", "=", " "]
operators = ["+", "-", "=", "("]
userTokens = []
userVariableTokens = {}

# Functions
def TokenizeInput(input):
    curIndex = 0
    curToken,prevChar = "", ""
    isCurTokenNeg = False

    # Negative Number handling
    # if there is a "-" with a "-" as the prevChar or no Prev char, its a neg.

    # Iterate through input
    for i in input:
        if i != " ":
            if i not in literals:
                # 'i' is not a literal, thus is part of curToken
                curToken += i
                if curIndex == len(input) - 1:
                    # If this is the end of the input, submit the curToken.
                    SubmitCurrentToken(curToken,isCurTokenNeg)
                    curToken = ""
                    isCurTokenNeg = False
            elif (prevChar in operators and i == "-") | (prevChar == "" and i == "-"):
                curToken += i
                isCurTokenNeg = True
            else:
                if curToken != "":
                    SubmitCurrentToken(curToken, isCurTokenNeg)
                curToken = ""
                isCurTokenNeg = False
                SubmitCurrentToken(i, isCurTokenNeg)
            prevChar = i
        curIndex += 1

def SubmitCurrentToken(curToken, isNeg):
    # If token is a number, convert token to int and append to token
    if curToken.isnumeric() | isNeg:
        userTokens.append(int(curToken))
    else:
    # Non-numerical tokens are variables.
        userTokens.append(curToken)

def EvaluateTokens(arrayOfTokens):
    operand = ""
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
                curTotal = EvaluateCurExpression(curTotal, operator, EvaluateTokens(arrayOfTokens))
                isPrevCharAnOp = False
                operand = ""
            elif i == ")":
                if operand != "":
                    curTotal = EvaluateCurExpression(curTotal, operator, operand)
                    isPrevCharAnOp = False
                    operand = ""
                return curTotal
            elif i in literals:
                operator = i
                isPrevCharAnOp = True
            else:
                if i in userVariableTokens.keys():
                    operand = userVariableTokens.get(i)
                else:
                    operand = i
                curTotal = EvaluateCurExpression(curTotal, operator, operand)
                operand = ""
    if operand != "":
        return EvaluateCurExpression(curTotal, operator, operand)
    return curTotal

def EvaluateCurExpression(curTotal, operator, operand):
    match operator:
        case "+" | "":
            return curTotal + operand
        case "-":
            return curTotal - operand

# The Start of the Program
while True:
    TokenizeInput(input())
    if userTokens.count("(") is userTokens.count(")"):
        print(EvaluateTokens(userTokens))
    else:
        print("ERROR: Missing a open/closing parentheses.")

    # Clear Tokens for loop
    userTokens.clear()