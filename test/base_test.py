def test_sort():
    source = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    print(source)
    source = sorted(source, key=lambda x: x['name'])
    print(source)


if __name__ == "__main__":
    pass
    test_sort()
