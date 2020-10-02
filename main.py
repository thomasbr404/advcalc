import os, sys
import math

import ply.lex as lex
import ply.yacc as yacc

from design.formatting import *

tokens = [	# List of token names
	'INT',
	'FLOAT',
	'NAME',
	'PLUS',
	'MINUS',
	'DIVIDE',
	'MULTIPLY',
	'EQUALS',
	'R_PARENTHESIS',
	'L_PARENTHESIS',
	'DELIMITER'
]

# Token definitions

t_PLUS = r'\+'				# addition token - "+"
t_MINUS = r'\-'				# subtraction token - "-"
t_DIVIDE = r'\/'			# division token - "/"
t_MULTIPLY = r'\*'			# multiplication token - "*"
t_EQUALS = r'\='			# equal to token - "="
t_R_PARENTHESIS = r'\)'		# right parenthesis token - ")"
t_L_PARENTHESIS = r'\('		# left parenthesis token - "("

t_ignore = r' '				# ignore blank characters (spaces)

def t_FLOAT(t):				# float token definition as "number" + "." + "decimals"
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_INT(t):				# integer token definition as any number
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_NAME(t):				# variable token definition as a-z, A-Z, 0-9, _, -
	r'[a-zA-Z_][a-zA-Z_0-9]*'	# must be an alphabetic character first
	t.type = 'NAME'
	return t
	
def t_DELIMITER(t):			# delimiter character set as "#" (not currently functioning.
	r'\#'
	t.type = 'DELIMITER'
	
def t_error(t):				# illegal character as anything outside of already defined tokens
	print("Illegal character input")
	t.lexer.skip(1)
	
lexer = lex.lex()

precedence = (				# must follow order of operations
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE')
)

def p_calc(p):				# carry out equation
	'''
	calc : expression
		 | var_assign
		 | empty
	'''
	print(run(p[1]))
	
def p_var_assign(p):		# assign a float/int to a variable
	'''
	var_assign : NAME EQUALS expression
	'''
	p[0] = ('=', p[1], p[3])

def p_expression(p):		# define what a mathematical expression is
	'''
	expression : expression MULTIPLY expression
			   | expression DIVIDE expression
			   | expression PLUS expression
			   | expression MINUS expression
	'''
	p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
	'''
	expression : INT
			   | FLOAT
	'''
	p[0] = p[1]

def p_expression_var(p):
	'''
	expression : NAME
	'''
	p[0] = ('var', p[1])
	
def p_delimiter(p):
	'''
	delimiter : DELIMITER
	'''
	p[0] = ('#')
	
def p_error(p):				# return an error
	print("Syntax error")

def p_empty(p):
	'''
	empty :
	'''
	p[0] = None


	
parser = yacc.yacc()
env = {}

def run(p):
	global env
	if type(p) == tuple:
		if p[0] == '+':
			return run(p[1]) + run(p[2])
		elif p[0] == '-':
			return run(p[1]) - run(p[2])
		elif p[0] == '*':
			return run(p[1]) * run(p[2])
		elif p[0] == '/':
			return run(p[1]) / run(p[2])
		elif p[0] == '=':
			env[p[1]] = run(p[2])
			#print(env)
		elif p[0] == 'var':
			if p[1] not in env:
				return 'Undeclared variable'
			else:
				return env[p[1]]
		elif p[0] == '#':
			return 'Delimiter detected'	# Not currently functioning, needs to be fixed.
	else:
		return p

while True:
	try:
		s = input(colors.fg.green + "advcalc > " + colors.reset)
	except EOFError:
		break
	parser.parse(s)
