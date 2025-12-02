ranges = [
	"67562556-67743658",
	"62064792-62301480",
	"4394592-4512674",
	"3308-4582",
	"69552998-69828126",
	"9123-12332",
	"1095-1358",
	"23-48",
	"294-400",
	"3511416-3689352",
	"1007333-1150296",
	"2929221721-2929361280",
	"309711-443410",
	"2131524-2335082",
	"81867-97148",
	"9574291560-9574498524",
	"648635477-648670391",
	"1-18",
	"5735-8423",
	"58-72",
	"538-812",
	"698652479-698760276",
	"727833-843820",
	"15609927-15646018",
	"1491-1766",
	"53435-76187",
	"196475-300384",
	"852101-903928",
	"73-97",
	"1894-2622",
	"58406664-58466933",
	"6767640219-6767697605",
	"523453-569572",
	"7979723815-7979848548",
	"149-216"
]
# ranges = [
#     "11-22",
#     "95-115",
#     "998-1012"
# ]


def parse_range(r: str) -> tuple[int, int]:
	left, right = r.split("-")
	start = int(left)
	end = int(right)
	if start > end:
		raise ValueError(f"Invalid range '{r}': start > end")
	return start, end


all_numbers = []
for r in ranges:
	start, end = parse_range(r)
	for n in range(start, end + 1): 
		all_numbers.append(n)


invalid_nums = []
for n in all_numbers:
	str_n = str(n)
	divisors = []
	for i in range (2, len(str_n)+1):
		if len(str_n) % i == 0:
			divisors.append(i)
	#print(f"Checking number {n} with divisors {divisors}")
	for d in divisors:
		part_length = len(str_n) // d
		parts = [str_n[i:i+part_length] for i in range(0, len(str_n), part_length)]
		if all(part == parts[0] for part in parts):
			invalid_nums.append(n)
			break


		
print("Invalid numbers:")
invalid_nums.sort()
print(invalid_nums)

sum_invalid = sum(invalid_nums)
print(f"Sum of invalid numbers: {sum_invalid}")