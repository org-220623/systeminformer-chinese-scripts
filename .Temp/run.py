with open("data.txt", "r", encoding="utf-8") as file:
	read = file.read().split("\n")

data = ""

for line in read:
	line_split = line.strip().split('": "')
	original = line_split[0] + '"'
	new = '"计数器: ' + original[1:]
	new_line = original + ": " + new
	data += (new_line + ",\n")
	
with open("data_1.txt", "w", encoding="utf-8") as file:
	file.write(data)
	