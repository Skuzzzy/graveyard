: TIMES ( n1 n2 -- n3)
    * DUP .
;

: MULTIPLY ( n1 n2 -- n3 )
    CR 2DUP SWAP . ." multiplied by " .
    ." equals " TIMES CR ;
