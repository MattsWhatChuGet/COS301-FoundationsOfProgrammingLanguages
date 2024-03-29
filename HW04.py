# -----------------------------------------------------------------------------
# Homework 04
# Matthew Patterson
# -----------------------------------------------------------------------------

# imports
import disassembler
import sys

# Compile Assembly Variables
func = "Function: "
conts = []
locals = []
globals = []
body = ["BEGIN"]
indent = "          "

# Tokens
tokens = (
    'NAME', 'NUMBER', 'FLOORDIV', 'FLOAT'
)

### GRAMMAR RULES ###

literals = ['=', '+', '-', '*', '/', '(', ')', '%']

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_FLOORDIV = r'//'

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    conts.append(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    #print(p[1]) - Call print funcs here


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '%' expression
                  | expression FLOORDIV expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '//':
        p[0] = p[1] // p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_float(p):
    "expression : FLOAT"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

### END GRAMMAR RULES ###

### CUSTOM FUNCTIONS ###
def CompileStringList(list):
    newStr = ""
    for i in range(0, len(list)):
        newStr += str(conts[i])
        if(i < len(list) -1):
            newStr += ", "
    return newStr

def PrintAssembly():
    # Prints Assembly Header
    print(func + "main/0")
    print("Constants: " + CompileStringList(conts))
    print("Locals: " + CompileStringList(locals))
    print("Globals: " + CompileStringList(globals))

import ply.yacc as yacc
parser = yacc.yacc()

def main():
    t = ""
    for l in sys.stdin:
        yacc.parse(l)
    PrintAssembly()
main()