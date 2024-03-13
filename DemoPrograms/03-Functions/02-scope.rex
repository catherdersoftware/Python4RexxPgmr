/* REXX */

signal on novalue

x = 50
call first
exit 

first: procedure  
    call second
    return

second: procedure expose x 
    say "X-squared is" x ** x
    return

third:
    side_effects = "yep"
    return

novalue:
  say 'NOVALUE raised at line' sigl
  say 'The referenced variable is' "CONDITION"('D')
  exit 8

glbl._screen_height = 25
glbl._screen_width = 80
glbl._attributes = 31

process_screen: expose glbl.
    say glbl._screen_height
    return

