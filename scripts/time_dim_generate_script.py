import json
strfmt = "{:02d}:{:02d}"

result = []
for i in range(0,24):
    for j in range(0,60):
        result.append({"time" : strfmt.format(i,j)})

print(json.dumps(result))
