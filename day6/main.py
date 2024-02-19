with open("6.in") as file:
    data = [line.strip() for line in file]

data.append("")

# Parse the data into list of groups
groups, group = [], []

for line in data:
    if line == "":
        groups.append(group)
        group = []

    else:
        group.append(line)


part1 = sum(len(set.union(*map(set, group))) for group in groups)
part2 = sum(len(set.intersection(*map(set, group))) for group in groups)

print(part1)
print(part2)
