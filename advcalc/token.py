import os, sys, math

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
	'EQUALS',
	'R_PARENTHESIS',
	'L_PARENTHESIS',
	'DELIMITER'
]

literals = [ '{', '}' ]
