import random
import string


class randomUtil:
    def __init__(self):
        pass
    # 生成给定长度的随机数字
    def random_shuzi(self, length):
        return ''.join(random.choices(string.digits, k=length))

    # 生成给定长度的随机小写字母
    def random_xiaoxie_zimu(self, length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    # 生成给定长度的随机大写字母
    def random_daxie_zimu(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    # 生成给定长度的随机大小写字母加数字
    def random_zimu_shuzi(self, length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

if __name__ == '__main__':
    r = randomUtil()
    print(r.random_shuzi(6))
    print(r.random_xiaoxie_zimu(6))
    print(r.random_daxie_zimu(6))
    print(r.random_zimu_shuzi(6))