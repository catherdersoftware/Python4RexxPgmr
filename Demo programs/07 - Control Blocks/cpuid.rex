/* REXX - CPU ids */                                                        
                                                                            
cvt      = storage(10,4)                                                    
cvtsname = storage(d2x(x2d(c2x(cvt))+x2d(154)),8)                           
ecvt     = storage(d2x(c2d(cvt)+x2d(8c)),4)                                 
ipa      = storage(d2x(c2d(ecvt)+x2d(188)),4)                               
ipasxnam = storage(d2x(x2d(c2x(ipa))+x2d(160)),8)                           
say "SYSNAME="||strip(cvtsname) "SYSPLEX="||strip(ipasxnam)  "Date="||date()
                                                                            
iosdshid = storage(d2x(x2d(c2x(cvt))+x2d(42c)),4)                           
type     = storage(d2x(x2d(c2x(iosdshid))+x2d(1a)),6)                       
model    = storage(d2x(x2d(c2x(iosdshid))+x2d(20)),3)                       
man      = storage(d2x(x2d(c2x(iosdshid))+x2d(23)),3)                       
plant    = storage(d2x(x2d(c2x(iosdshid))+x2d(26)),2)                       
seqno    = storage(d2x(x2d(c2x(iosdshid))+x2d(28)),12)                      
say "CPC="||type||"."||model||"."||man||"."||plant||"."||seqno              
                                                                            
say " "                                                                     
cvtmaxmp = c2d(storage(d2x(x2d(c2x(cvt))+x2d(1dc)),2))                      
cvtpccat =     storage(d2x(c2d(cvt)+x2d(2fc)),4)                            
say "-----------------------"                                               
say " ID  VER  CPUID   MODEL"                                               
say "-----------------------"                                               
do p = 0 to cvtmaxmp                                                        
   pcca   = storage(d2x(c2d(cvtpccat)+p*4),4)                               
   if pcca  <> "00000000"x then do                                          
      pccapcca = storage(d2x(c2d(pcca)),4)                                  
      if pccapcca = "PCCA" then do                                          
         pccavc   = storage(d2x(c2d(pcca)+4),2)                             
         pccacpid = storage(d2x(c2d(pcca)+6),6)                             
         pccamdl  = storage(d2x(c2d(pcca)+12),4)                            
         pccaattr = storage(d2x(c2d(pcca)+x2d(178)),1)                      
        sp=""                                                               
        pccaziip = bitand(pccaattr,x2c("04"))                               
        if pccaziip = "04"x then sp=sp"zIIP"                                
        pccazaap = bitand(pccaattr,x2c("01"))                               
        if pccazaap = "01"x then sp=sp"zAAP"                                
        say right(p,3," ")||"  "||pccavc " " pccacpid||,                    
            "  "|| pccamdl sp                                               
      end                                                                   
   end                                                                      
end                                                                         