===============
Testing CpfCnpj
===============

  >>> from cnpj import Cnpj
  >>> cnpj = Cnpj('87552587000120')
  >>> cnpj
  87.552.587/0001-20

  >>> cnpj.validate()
  True
