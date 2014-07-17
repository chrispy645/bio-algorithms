# http://users-cs.au.dk/chili/CSS/Exercises/codontable.jpg

aatable = {
"TTT":"F",
"TTC":"F",
"TTA":"L",
"TTG":"L",
"CTT":"L",
"CTC":"L",
"CTA":"L",
"CTG":"L",
"ATT":"I",
"ATC":"I",
"ATA":"I",
"ATG":"M",
"GTT":"V",
"GTC":"V",
"GTA":"V",
"GTG":"V",
"TCT":"S",
"TCC":"S",
"TCA":"S",
"TCG":"S",
"CCT":"P",
"CCC":"P",
"CCA":"P",
"CCG":"P",
"ACT":"T",
"ACC":"T",
"ACA":"T",
"ACG":"T",
"GCT":"A",
"GCC":"A",
"GCA":"A",
"GCG":"A",
"TAT":"Y",
"TAC":"Y",
"TAA":"*",
"TAG":"*",
"CAT":"H",
"CAC":"H",
"CAA":"Q",
"CAG":"Q",
"AAT":"N",
"AAC":"N",
"AAA":"K",
"AAG":"K",
"GAT":"D",
"GAC":"D",
"GAA":"E",
"GAG":"E",
"TGT":"C",
"TGC":"C",
"TGA":"*",
"TGG":"W",
"CGT":"R",
"CGC":"R",
"CGA":"R",
"CGG":"R",
"AGT":"S",
"AGC":"S",
"AGA":"R",
"AGG":"R",
"GGT":"G",
"GGC":"G",
"GGA":"G",
"GGG":"G"
}

import sys

s = sys.stdin.readline().rstrip().replace('U','T')

t = []

for i in range(0, len(s), 3):
    aa = s[i:i+3]
    if aatable[aa] == '*':
        break
    t.append(aatable[aa])

print "".join(t)

