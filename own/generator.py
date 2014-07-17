import random

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

num_entries = random.randint(10,100)
print num_entries
for i in range(0, num_entries):
    a = random.randint(0, len(aatable.keys())-1)    
    b = random.randint(0, len(aatable.keys())-1)
    aa = aatable.keys()[a]
    bb = aatable.keys()[b]
    while bb == aa:
        b = random.randint(0, len(aatable.keys())-1)
        bb = aatable.keys()[b]
    print aa,
    print bb,
    print aatable[aa] == aatable[bb]
