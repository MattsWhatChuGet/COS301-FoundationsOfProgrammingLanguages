# Title: Homework 01: PMPVI Program
# By: Matthew Patterson

# Variables
literals = ["+", "-", "(", ")", "=", " "]
userInput = ""
userTokens = []
userVariableTokens = {}

# Functions
def TokenizeInput(input):
    curIndex = 0
    curToken = ""

    # Iterate through input
    for i in input:
        if i not in literals:
            # 'i' is not a literal, thus is part of curToken
            curToken = curToken + i
            if curIndex == len(input) - 1:
                SubmitCurrentToken(curToken)
                curToken = ""
        elif i != " ":
            SubmitCurrentToken(curToken)
            curToken = ""
            userTokens.append(i)
        curIndex = curIndex + 1

def SubmitCurrentToken(curToken):
    if curToken.isnumeric():
        userTokens.append(int(curToken))
    elif curToken.isalpha():
        if curToken in userVariableTokens:
            userTokens.append(userVariableTokens.get(curToken))
        else:
            userVariableTokens[curToken] = 0
    else:
        print("ERROR: Did not submit token")

def EvaluateTokens(arrayOfTokens):
    operand1 = ""
    operator = ""
    operand2 = ""
    curTotal = 0;
    isSettingToVariable = False

    while len(arrayOfTokens) > 0:
        print(str(arrayOfTokens))
        i = arrayOfTokens.pop(0)
        if i == "=":
            isSettingToVariable = True
        elif i == "(":
            if operand1 == "":
                operand1 = EvaluateTokens(arrayOfTokens)
            elif operand2 == "":
                operand2 = EvaluateTokens(arrayOfTokens)
                curTotal = curTotal + EvaluateCurExpression(operand1, operator, operand2)
        elif i == ")":
            return curTotal
        elif i in literals:
            operator = i
            print("curOperator: " + str(operator))
        elif operand1 == "":
            operand1 = i
            print("operand1: " + str(operand1))
        elif operand2 == "":
            operand2 = i
            print("operand2: " + str(operand2))
            curTotal = curTotal + EvaluateCurExpression(operand1, operator, operand2)

        print("curTotal: " + str(curTotal))
    if isSettingToVariable:
        userVariableTokens[len(userVariableTokens) -1 ] = curTotal
        return ""
    else:
        return curTotal

def EvaluateCurExpression(operand1, operator, operand2):
    print("Evaluating: " + str(operand1) + str(operator) + str(operand2))
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2

while userInput != "quit":
    userInput = input()
    TokenizeInput(userInput)
    if userTokens.count("(") is userTokens.count(")"):
        print(EvaluateTokens(userTokens))
    else:
        print("ERROR: Missing a open/closing parentheses.")

    print("User Int Tokens: " + str(userTokens))
    print("User Var Tokens: " + str(userVariableTokens))

    # Clear Tokens for loop
    userTokens.clear()