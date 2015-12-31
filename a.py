import operator;
print reduce(operator.mul, [rr[0] for rr in [(g,g+1^g-1) for g in [int(a) for a in "".join([str(x) for x in xrange(15)]).join([str(w) for w in map(lambda y : y*y, [q-5 for q in xrange(50) if q % 2 == 0])])]] if rr[0] != 0], 1)
print reduce(operator.mul,\
         [rr[0] for rr in\
            [(g,g+1^g-1) for g in\
                [int(a) for a in\
                    "".join([str(x) for x in xrange(15)])\
                        .join([str(w) for w in map(lambda y : y*y,\
                            [q-5 for q in xrange(50) if q % 2 == 0])])]]\
          if rr[0] != 0],\
        1)

print ", ".join(["(" + str(a[0]) + "F is " + str(a[1]) + "C)" for a in map(lambda x: (x, (x-32)*(5.0/9)), [120, 50])])
