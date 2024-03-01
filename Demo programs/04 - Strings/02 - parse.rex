/* REXX */

dsname = "MY.DATASET.NAME(@README)"

parse var dsname dsn '(' member ')'

say "dsn="dsn" member="member

/* a more vexing parse that doesn't work as expected! */
parm = "DSNAME(MY.DATASET.NAME(@README))"

parse var parm 'DSNAME(' dsn ')'
say dsn  /* MY.DATASET.NAME(@README */

parse var parm 'DSNAME(' dsn '(' mem')' ')'
say dsn mem /* MY.DATASET.NAME @README */

parm = "DSNAME(MY.DATASET.NAME)"
parse var parm 'DSNAME(' dsn '(' mem')' ')'
say dsn mem /* MY.DATASET.NAME)  */
