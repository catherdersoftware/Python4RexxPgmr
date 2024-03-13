/* REXX */

mood = "happy"

if mood = "happy" then do
  say "I'm very pleased your're in good mood"
end  
else if mood = "sad" then do
  say "Cheer up!"
end
else if mood = "anxious" | mood = "worried" then do
    say "Take a chill pill bro!"
end  
else do
  say "I'll put the kettle on!"
end

select
  when mood = "happy" then do
    say "I'm very pleased your're in good mood"
  end  
  when mood = "sad" then do
    say "Cheer up"
  end  
  when mood = "anxious" | mood = "worried" then do
    say "Take a chill pill bro!"
  end  
  otherwise do
    say "I'll put the kettle on!"
  end
 end 