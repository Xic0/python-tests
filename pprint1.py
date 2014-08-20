#!/usr/bin/python --

def TopOrBottom(chr, width):
    return "%s%s%s" % ("+", (chr * (width - 2)), "+")

def Fmt(val1, leftbit, val2, rightbit):
    part2 = '%.2f' % val2
    return "%s%s%s%s" % ("| ", val1.ljust(leftbit-2, " "), part2.rjust(rightbit-2, " "), " |")


items = [['Soda', 1.45], ['Candy', .75], ['Bread', 1.95], ['Milk', 2.59]]

print TopOrBottom("=", 40)
total = 0
for c in range(0, len(items)):
    print Fmt(items[c][0], 30, items[c][1], 10)
    total += items[c][1]
print TopOrBottom("-", 40)
print Fmt('Total', 30, total, 10)
print TopOrBottom("=", 40)
