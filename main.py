import os, sys
import math

import ply.lex as lex
import ply.yacc as yacc

tokens = [	# List of token names
	'INT',
	'FLOAT',
	'NAME',
	'PLUS',
	'MINUS',
	'DIVIDE',
	'MULTIPLY',
	'EQUALS'
]

# Token definitions

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='

t_ignore = r' '

def t_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'NAME'
	return t
	
def t_error(t):
	print("Illegal character input!")
	t.lexer.skip(1)
	
lexer = lex.lex()

def p_calc(p):
	'''
	calc : expression
		 | empty
	'''
	print(p[1])
	
def p_expression(p):
	'''
	expression : INT
			   | FLOAT
	'''
	p[0] = p[1]
	
def p_empty(p):
	'''
	empty :
	'''
	p[0] = None
	
parser = yacc.yacc()

while True:
	try:
		s = input('')
	except EOFError:
		break
	parser.parse(s)



