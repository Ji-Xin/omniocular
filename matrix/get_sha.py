sha = []
labels = []
with open("../../omniocular-data/datasets/vulas_diff_token/test.tsv") as f:
    for line in f:
        a = line.strip().split('\t')
        sha.append(a[1])
        labels.append(a[-1])

with open("truth", 'w') as fout:
    for s, l in zip(sha, labels):
        print("{}\t{}".format(s, l), file=fout)
