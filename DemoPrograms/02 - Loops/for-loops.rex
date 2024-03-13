/* REXX */

say " "
say "-- REXX loops --"

/* controlled repetitive loop */
do i = 1 to 10
  say i
end

do i = 3 to -2 by -1
  say i 
end

/* conditional phases (while and until)*/
do i = 1 to 10 by 2 until i > 6
  say i
end

say ""
do i = 1 to 10 by 2 while i < 6
  say i
end