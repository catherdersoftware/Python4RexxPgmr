from pyzfile import *

# read a binary file using QSAM
try:
    with ZFile("//'SYSTEM.DAILY.SMF'", "rb,type=record,noseek") as file:
        for rec in file:
            pass
except ZFileError as e:
    print(e)

# read a text file using BSAM
try:
    with ZFile("//'USERID.CNTL(JCL)'", "rb,type=record",encoding='cp1047') as file:
        for rec in file:
            print(rec)
except ZFileError as e:
    print(e)

# Note: pyzfile can handle all types of data set: BSAM, QSAM, VSAM (ESDS, KSDS, RRDS), Unix