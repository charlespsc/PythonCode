### Meu código para verificar se um ano é bissexto ###

# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# test_data = [1900, 2000, 2016, 1987, 2032, 2024, 1600, 2400, 2023, 1800, 2100]
# test_results = [False, True, True, False, True, True, True, True, False, False, False]

# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "-> ", end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fracassado")


###############
### SOLUÇÃO ###
###############

def is_year_leap(year):
 if year % 4 != 0:
    return False
 elif year % 100 != 0:
    return True
 elif year % 400 != 0:
    return False
 else:
    return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
