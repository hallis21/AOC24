#1
print(sum([sum([[(int(n1)*int(n2)) for n1, n2 in [match.replace("mul(", "").replace(")", "").split(",")]][0] for match in matches]) for matches in [__import__("re").compile(r"(mul\(\d{1,3},\d{1,3}\))").findall(line) for line in [x.strip() for x in open("in").readlines()]]]))

# 2
print([sum([sum([(vars.__setitem__("e", True), 0)[1] if match[1] != "" else (vars.__setitem__("e", False), 0)[1] if match[2] != "" else [(int(n1)*int(n2)) for n1, n2 in [match[0].replace("mul(", "").replace(")", "").split(",")]][0] if vars["e"] else 0 for match in matches]) for matches in [__import__("re").compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))").findall(line) for line in [x.strip() for x in open("in").readlines()]]]) for vars in [{"e": True,}]][0])
