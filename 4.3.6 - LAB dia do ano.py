def is_year_leap(year):
    # Condição para anos antes de 1582 (calendário gregoriano)
    if year < 1582:
        return False
    # As regras para anos bissextos
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Validação de ano e mês
    if year < 1582 or month < 1 or month > 12:
        return None
    
    # Lista com os dias de cada mês (janeiro a dezembro)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ajusta para fevereiro em ano bissexto
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days[month - 1] # -1 porque a lista é baseada em zero

def day_of_year(year, month, day):
    # Validação inicial dos argumentos
    if year < 1582 or month < 1 or month > 12 or day < 1:
        return None

    days_passed = 0
    # Soma os dias dos meses anteriores ao mês atual
    for m in range(1, month):
        md = days_in_month(year, m)
        if md is None: # Verifica se o mês anterior é válido (embora já validado no início)
            return None
        days_passed += md
    
    # Obtém o número de dias do mês atual
    md_current_month = days_in_month(year, month)
    if md_current_month is None: # Verifica se o mês atual é válido
        return None
    
    # Valida o dia no mês atual
    if day >= 1 and day <= md_current_month:
        return days_passed + day
    else:
        return None

# Testes para is_year_leap (do LAB 4.3.1.6)
print("--- Testes is_year_leap ---")
test_years_leap = [1900, 2000, 2016, 1987, 1582, 1700, 1600, 1800, 2020]
expected_leap_results = [False, True, True, False, True, False, True, False, True] # 1582 é bissexto pois é divisível por 4 e 100, mas não por 400. Ah, espera, 1582 não é bissexto. 1582 % 4 != 0.
                                                                                # 1582 % 4 == 2. Então 1582 é False.

# Correção da expectativa para is_year_leap:
# 1900 -> False (divisível por 100 mas não por 400)
# 2000 -> True (divisível por 400)
# 2016 -> True (divisível por 4)
# 1987 -> False (não divisível por 4)
# 1582 -> False (não divisível por 4)
# 1700 -> False (divisível por 100 mas não por 400)
# 1600 -> True (divisível por 400)
# 1800 -> False (divisível por 100 mas não por 400)
# 2020 -> True (divisível por 4)

expected_leap_results = [False, True, True, False, False, False, True, False, True]


for i in range(len(test_years_leap)):
    yr = test_years_leap[i]
    print(f"Ano: {yr} -> ", end="")
    result = is_year_leap(yr)
    if result == expected_leap_results[i]:
        print("OK")
    else:
        print(f"Fracassado (Esperado: {expected_leap_results[i]}, Obtido: {result})")

print("\n--- Testes days_in_month ---")
test_years_month = [1900, 2000, 2016, 1987, 2024, 2023, 1581, 2000, 2001, 2024, 2024, 2024]
test_months_month = [2, 2, 1, 11, 2, 6, 1, 13, 0, 4, 9, 12]
test_results_month = [28, 29, 31, 30, 29, 30, None, None, None, 30, 30, 31]

for i in range(len(test_years_month)):
    yr = test_years_month[i]
    mo = test_months_month[i]
    print(f"{yr}, {mo} -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results_month[i]:
        print("OK")
    else:
        print(f"Fracassado (Esperado: {test_results_month[i]}, Obtido: {result})")

print("\n--- Testes day_of_year ---")
# Testes para day_of_year
# Ano, Mês, Dia, Resultado Esperado
test_cases_day_of_year = [
    (2000, 12, 31, 366),  # Ano bissexto, último dia
    (2001, 12, 31, 365),  # Ano normal, último dia
    (2024, 3, 1, 61),     # Ano bissexto, 1º de março (31+29+1)
    (2023, 3, 1, 60),     # Ano normal, 1º de março (31+28+1)
    (1999, 1, 1, 1),      # Primeiro dia do ano
    (2000, 2, 29, 60),    # Dia 29 de fevereiro em ano bissexto (31+29)
    (2001, 2, 29, None),  # Dia 29 de fevereiro em ano normal (inválido)
    (2024, 1, 32, None),  # Dia inválido
    (2024, 13, 1, None),  # Mês inválido
    (1581, 1, 1, None),   # Ano inválido
    (2024, 6, 15, 167)    # (31+29+31+30+31+15) = 167
]

for year, month, day, expected in test_cases_day_of_year:
    print(f"Ano: {year}, Mês: {month}, Dia: {day} -> ", end="")
    result = day_of_year(year, month, day)
    if result == expected:
        print("OK")
    else:
        print(f"Fracassado (Esperado: {expected}, Obtido: {result})")