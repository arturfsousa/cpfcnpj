# coding: utf-8

class Cnpj(object):

    def __init__(self, num):
        self.num = num

    def format(self):
        str_format = '{0}.{1}.{2}/{3}-{4}'
        return str_format.format(self.num[:2], self.num[2:5], self.num[5:8],
                                 self.num[8:12], self.num[12:])

    def validate(self):
        return True

    def __repr__(self):
        return self.format()
