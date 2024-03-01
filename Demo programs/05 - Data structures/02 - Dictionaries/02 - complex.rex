/* REXX */

system.server.type = "MVS"
system.server.name = "RSD6"
system.server.plex = "RSPLEXL6"
system.server.jobs.0 = 4
system.server.jobs.1.jobname = "BACKUP"
system.server.jobs.1.jobno = "J00012"
system.server.jobs.2.jobname = "PAYROLL"
system.server.jobs.2.jobno = "J00013"
system.server.jobs.3.jobname = "BILLING"
system.server.jobs.3.jobno = "J00014"
system.server.jobs.4.jobname = "ORDERS"
system.server.jobs.4.jobno = "J00015"

say "System name . . . :" system.server.name
say "System type . . . :" system.server.type
do i = 1 to system.server.jobs.0
  say "jobname="system.server.jobs.i.jobname ||,
      " jobno="system.server.jobs.i.jobno
end