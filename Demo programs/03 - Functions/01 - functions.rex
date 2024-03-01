/* REXX */

call print "hello", "world" /* parenthesis are optional */

say "results of add = " add(1, 2, 3, 4, 5, 6)

exit 0 

echo:
  parse arg first_word, second_word
  say first_word second_word
  return

/* variable number of arguments */
add:
  res = 0 
  do i = 1 to arg()
    res = res + arg(i)
  end
  return res