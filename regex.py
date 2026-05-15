import re 
sequence = "TATAAATAGGCTATAATGTAT"
pattern = r"TATA[AT]A[AT]"
matches = re.findall(pattern, sequence)
print(matches)

if re.fullmatch(r"[ATGC]+", sequence):
    print("valid DNA sequence")
else:
    print("Invalid characters found")

#dedent these lines outside the if/else block
codon = re.findall(r'.{3}', sequence)
print(codon)