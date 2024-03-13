/* REXX */

text.1 = "this is a text of record"
text.2 = "to demonstrate how to process"
text.3 = "texts in REXX"
text.0 = 3

n = text.0 + 1
text.0 = n
text.n = "oh yeah!"

do i = 1 to text.0
  say text.i
end