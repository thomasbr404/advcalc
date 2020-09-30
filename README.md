# advcalc
Calculator for my hs math classes

I wanted to add a bit of a challenge to them and I felt that this was the way to do it. Each time I move into a new unit, I will attempt to add the needed functionality before the unit is over.

Using PLY, the calculator is basically implementing a very simple language of its own that can store variables and use functions. (That's the plan at least.)

Due to how PLY works (mostly yacc functionality but you know, it's PLY), it generates parsetab.py and parser.out each time main.py is run. Those files look somewhat like: (on the current build)

```
parser.out
Created by PLY version 3.11 (http://www.dabeaz.com/ply)

Unused terminals:

    DIVIDE
    EQUALS
    MINUS
    MULTIPLY
    NAME
    PLUS

Grammar

Rule 0     S' -> calc
Rule 1     calc -> expression
Rule 2     calc -> empty
Rule 3     expression -> INT
Rule 4     expression -> FLOAT
Rule 5     empty -> <empty>

Terminals, with rules where they appear

DIVIDE               : 
EQUALS               : 
FLOAT                : 4
INT                  : 3
MINUS                : 
MULTIPLY             : 
NAME                 : 
PLUS                 : 
error                : 

Nonterminals, with rules where they appear

calc                 : 0
empty                : 2
expression           : 1

Parsing method: LALR

state 0

    (0) S' -> . calc
    (1) calc -> . expression
    (2) calc -> . empty
    (3) expression -> . INT
    (4) expression -> . FLOAT
    (5) empty -> .

    INT             shift and go to state 4
    FLOAT           shift and go to state 5
    $end            reduce using rule 5 (empty -> .)

    calc                           shift and go to state 1
    expression                     shift and go to state 2
    empty                          shift and go to state 3

state 1

    (0) S' -> calc .



state 2

    (1) calc -> expression .

    $end            reduce using rule 1 (calc -> expression .)


state 3

    (2) calc -> empty .

    $end            reduce using rule 2 (calc -> empty .)


state 4

    (3) expression -> INT .

    $end            reduce using rule 3 (expression -> INT .)


state 5

    (4) expression -> FLOAT .

    $end            reduce using rule 4 (expression -> FLOAT .)
```
```
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUALS FLOAT INT MINUS MULTIPLY NAME PLUS\n\tcalc : expression\n\t\t | empty\n\t\n\texpression : INT\n\t\t\t   | FLOAT\n\t\n\tempty :\n\t'
    
_lr_action_items = {'INT':([0,],[4,]),'FLOAT':([0,],[5,]),'$end':([0,1,2,3,4,5,],[-5,0,-1,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,],[2,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','main.py',51),
  ('calc -> empty','calc',1,'p_calc','main.py',52),
  ('expression -> INT','expression',1,'p_expression','main.py',58),
  ('expression -> FLOAT','expression',1,'p_expression','main.py',59),
  ('empty -> <empty>','empty',0,'p_empty','main.py',65),
]
```

DO NOT EDIT EITHER OF THESE FILES PLEASE!
