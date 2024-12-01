
print(sum([abs([x[1] for x in [[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()]][i] - sorted([x[0] for x in [[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()]])[i]) for i in range(len([[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()]))]))

print()

print(sum([[[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()][n][0] * [x[1] for x in [[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()]].count([[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()][n][0]) for n in range(len([[int(y) for y in x.strip().split("  ")] for x in open("in").readlines()]))]))
