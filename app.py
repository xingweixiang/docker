import csv
import json

def hello_world():
    print("Hello world")
    Q2 = 0;
    list = []
    dict = {"Q1":"Hello world"}
    with open("tcdata/num_list.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            list.append(int(line[0]))
            Q2 += int(line[0])
    print (sorted(list,reverse=True)[0:10])
    dict["Q2"] = Q2
    dict["Q3"] = sorted(list,reverse=True)[0:10]
    json_str = json.dumps(dict)
    with open('result.json', 'w') as json_file:
        json_file.write(json_str)


if __name__ == '__main__':
    hello_world()
