
: make-array ( n -- ) cells allot ;

: zero-init ( n -- ) dup here swap make-array 0 fill ;

: print-all ( array num -- )
    dup 0<> if
	over ?
	-1 recurse
    then
	2drop
;
