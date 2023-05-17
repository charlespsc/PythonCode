###############################################################
#### 4.3.6   LAB   Dia do ano: escrevendo e usando funções ####
###############################################################

# Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) 
### e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

# Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código.

# def is_year_leap(year):
#  #
#  # Seu código do LAB anterior.
#  #

# def days_in_month(year, month):
#  #
#  # Seu código do Lab anterior.
#  #

# def day_of_year(year, month, day):
#  #
#  # Escreva seu código aqui.
#  #

# print(day_of_year(2000, 12, 31))


### DICA:

# def is_year_leap(year):
#  if year % 4 != 0:
#  return False
#  elif year % 100 != 0:
#  return True
#  elif year % 400 != 0:
#  return False
#  else:
#  return True

# def days_in_month(year, month):
#  if year < 1582 or month < 1 or month > 12:
#  return None
#  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  res = days[month - 1]
#  if month == 2 and is_year_leap(year):
#  res = 29
#  return res

# def day_of_year(year, month, day):
#  days = 0
#  for m in range(1, month):
#  # ...
#  # if statement
#  # ...
#  days += md
#  md = days_in_month(year, month)
#  if day >= 1 and day <= md:
#  # ...
#  else:
#  # ...

# print(day_of_year(2000, 12, 31))


### SOLUÇÃO:

def is_year_leap(year):
 if year % 4 != 0:
    return False
 elif year % 100 != 0:
    return True
 elif year % 400 != 0:
    return False
 else:
    return True

def days_in_month(year, month):
 if year < 1582 or month < 1 or month > 12:
    return None
 days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 res = days[month - 1]
 if month == 2 and is_year_leap(year):
    res = 29
    return res

def day_of_year(year, month, day):
 days = 0
 for m in range(1, month):
    md = days_in_month(year, m)
 if md == None:
    return None
 days += md
 md = days_in_month(year, month)
 if day >= 1 and day <= md:
    return days + day
 else:
    return None

print(day_of_year(2000, 12, 31))


