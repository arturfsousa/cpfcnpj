===============
Testing CpfCnpj
===============

  >>> from cnpj import Cnpj
  >>> Cnpj('127818212312311')
  Traceback (most recent call last):
    ...
  ValueError: Cnpj deve possuir 14 digitos

  >>> Cnpj('123456789123')
  Traceback (most recent call last):
    ...
  ValueError: Cnpj deve possuir 14 digitos

  >>> Cnpj('1234.678912a11')
  Traceback (most recent call last):
    ...
  ValueError: Cnpj deve possuir 14 digitos

  >>> Cnpj('87552587000220')
  Traceback (most recent call last):
    ...
  ValueError: Cnpj inválido

  >>> cnpj = Cnpj('87552587000120')
  >>> cnpj
  87.552.587/0001-20

  >>> cnpj.format()
  '87.552.587/0001-20'

  >>> cnpj.unformat()
  '87552587000120'

  >>> print cnpj
  87.552.587/0001-20

  >>> cnpjs = Cnpj.generate_random(100)
  >>> all([isinstance(cnpj, Cnpj) for cnpj in cnpjs])
  True

  >>> len({cnpj.format() for cnpj in cnpjs})
  100

