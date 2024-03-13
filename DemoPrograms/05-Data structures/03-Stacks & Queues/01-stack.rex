/* REXX */

push '1. last'
push '2. in'
push '3. last'
push '4. out'

do queued()
  parse pull item
  say item
end

queue '1. first'
queue '2. in'
queue '3. first'
queue '4. out'

push '0. <== yay ==>'

do queued()
  parse pull item
  say item
end