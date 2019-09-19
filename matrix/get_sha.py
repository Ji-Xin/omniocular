split = "train"
sha = []
labels = []
with open("../../omniocular-data/datasets/vulas_diff_token/{}.tsv".format(split)) as f:
    for line in f:
        a = line.strip().split('\t')
        sha.append(a[1])
        labels.append(a[-1])

with open("{}_truth".format(split), 'w') as fout:
    for s, l in zip(sha, labels):
        print("{}\t{}".format(s, l), file=fout)
