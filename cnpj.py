# coding: utf-8

import re
import random

class Cnpj(object):

    def __init__(self, num):
        self._num = num
        self._validate()

    def _validate(self):
        # Remove non-digits chars
        self._num = filter(lambda c: c.isdigit(), self._num)

        if len(self._num) != 14:
            raise ValueError('Cnpj deve possuir 14 digitos')

        if self.calculate_dv(self._num[:12]) != self._num[-2:]:
            raise ValueError('Cnpj inválido')

    @classmethod
    def calculate_dv(cls, num):
        pesos = (
            (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
            (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
        )
        num_sem_dv = [int(i) for i in num]

        tabela = zip(num_sem_dv, pesos[0])
        soma = sum([c1*c2 for c1,c2 in tabela])
        mod = soma % 11
        dv1 = 0 if mod < 2 else 11 - mod

        tabela = zip(num_sem_dv + [int(dv1)], pesos[1])
        soma = sum([c1*c2 for c1,c2 in tabela])
        mod = soma % 11
        dv2 = 0 if mod < 2 else 11 - mod

        return str(dv1)+str(dv2)

    @classmethod
    def generate_random(cls, total):
        """Generates arbitrary distinct cnpj numbers"""
        cnpjs = {}
        while len(cnpjs) < total:
            inscricao = ''.join([str(random.randrange(9)) for d in range(8)])
            cd_matriz = '0001'
            dv = cls.calculate_dv(inscricao+cd_matriz)
            cnpj = inscricao+cd_matriz+dv
            cnpjs[cnpj] = Cnpj(cnpj)
        return cnpjs.values()

    def format(self):
        str_format = '{0}.{1}.{2}/{3}-{4}'
        return str_format.format(self._num[:2], self._num[2:5], self._num[5:8],
                                 self._num[8:12], self._num[12:])

    def unformat(self):
        return self._num

    def __repr__(self):
        return self.format()
