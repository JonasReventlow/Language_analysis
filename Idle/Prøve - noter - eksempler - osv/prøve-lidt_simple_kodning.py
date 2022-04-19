>>> 2+3
5
>>> 2 + 3
5
>>> type(2)
<class 'int'>
>>> type(6/2)
<class 'float'>
>>> type('hej med dig')
<class 'str'>
>>> 
>>> husleje = 6.5
>>> el = 0.4
>>> fit = 0.25
>>> mineudgifter = husleje + el + fit
>>> mineudgifter
7.15
>>> print(mineudgifter)
7.15
>>> #man skal skrive print for at få det udskrevet
>>> number = 2
>>> number = number*number
>>> number
4
>>> number*=number
>>> number
16
>>> d* = 6+6
SyntaxError: invalid syntax
>>> d = 6
>>> d* = 6+6
SyntaxError: invalid syntax
 d*=6+6
>>> d
72
>>> #dette sker da python altid regner ud hvad der sker på højre side af = tegnet
>>> 8*2.5
20.0
>>> 9/2
4.5
>>> )9//2
SyntaxError: unmatched ')'
>>> 9//2
4
>>> 9%2
1
>>> 9.0%2
1.0
>>> 4+3*5
19
>>> (4+3)*5
35
>>> 9%2
1
>>> # % viser det overskudende der er i resultater = altså resten af det deviderede
>>> average = 5
>>> average + 3 + 7 + 9
24
>>> 24/4
6.0
>>> average = average + 3 + 7 + 9
>>> average=average/4
>>> average
6.0
>>> average+ = 3 + 7 + 9
SyntaxError: invalid syntax
>>> average+=3+7+9
>>> average=average/4
>>> average
6.25
>>> #Det skulle have været 6, men havde glemt at få average tilbage til 5 igen
