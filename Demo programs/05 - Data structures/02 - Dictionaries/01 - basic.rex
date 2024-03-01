/* REXX */

null = '00'x

dict. = null  

call dict_add "color", "red"
call dict_add "make", "Toyota"

say "color="dict_get("color")
say dict_get("novalue")

call dict_delete "color"

call dict_clear

say "make="dict_get("make")

exit

dict_add: procedure expose dict. 
  parse arg key, value
  dict.key = value
  return 

dict_get: procedure expose dict. 
  parse arg key
  return dict.key

dict_delete: procedure expose dict. 
  parse arg key
  dict.key = null  /* <<< BUG!! */
  return

dict_clear: procedure expose dict. 
  drop dict.
  dict. = '00'x
  return 