import pypinyin
import datetime


# 不带声调
def pin_yin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        # s += i[0].title()
        s += ''.join(i)
    return f"{s}{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"


# 带声调
def yin_jie(word):
    s = ''
    for i in pypinyin.pinyin(word, heteronym=True):
        s = s + ''.join(i) + " "
    return s


if __name__ == "__main__":
    print(datetime.datetime.now())
    print(pin_yin("最后的防守"))
    print(yin_jie("诗书继世长"))
