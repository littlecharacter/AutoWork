from core.execute import OperateTypeEnum


def test_sort():
    source = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    print(source)
    source = sorted(source, key=lambda x: x['name'])
    print(source)


def test_enum():
    e = OperateTypeEnum.get_enum(1)
    print(e == OperateTypeEnum.LEFT_CLICK)


if __name__ == "__main__":
    pass
    # test_sort()
    test_enum()
