import json


def json_to_object(source, target):
    pass


if __name__ == '__main__':
    filename = '../db/work_flow.json'
    with open(filename) as f:
        data = json.load(f)
    for d in data:
        print(d)
        for k, v in d.items():
            if v == 20220315154547:
                print(f"k:{k},v:{v}")

