/* REXX */

"ALLOC FI(INPUT) DA('SYSTEM.DAILY.SMF') SHR"

 do until eof
    "EXECIO 10000 DISKR INPUT ( STEM rec."
    eof = (rc > 0)
    do i = 1 to rec.0
      iterate 
    end
  end

"EXECIO 0 DISKR INPUT ( FINIS"

"FREE FI(INPUT)"