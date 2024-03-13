scale = "Do Re Mi Fa Sol La Ti Do"
 
/* quick and dirty ;-) */
do i = 1 to words(scale)
  say word(scale, i)
end

/* the right way :-) */
line = scale
do while line \= ''
  parse var line w line
  say w
end

/* count words in a string */
say "They're are "words(scale)" notes in the major scale"

/* print the characters in the string */
len = length(scale)
do i = 1 to len
  say substr(scale, i, 1)
end

/* concatenate */
scale = "  "scale"  "
say "'"scale"'"

/* trim */
scale = strip(scale, 'L')
scale = strip(scale, 'T')
scale = strip(scale)  /* strip(scale, 'B') */

/* sub-strings */
s = left(scale, 2)
s = right(scale, 2)
s = substr(scale, 3, 2)

/* with justification */
str = "REXX"
say left(str, length(str), 10) /* 'REXX      ' */