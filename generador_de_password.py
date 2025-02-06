import random

clave_valor1 = ""
c= 12

def formato1():
  x = 0
  clave_valor1 = ""
  while x < c:

    for cantidad_de_caractermayus in range(0,1):
        variable_alzar = random.randint(65,90)
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_de_caracter in range(0,1):
        variable_alzar = random.randint(97,122)   
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
    for cantidad_de_caracter in range(0,1):
        variable_alzar = random.randint(97,122)   
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break
        
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_de_simbolo in range (0,1):
        variable_alzar = random.randint(33,47)
        simbolo_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + simbolo_alzar
    x = x + 1
    if x == c:
        break
  return clave_valor1 

def formato2():
  x = 0
  clave_valor1 = ""
  while x < c:
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_de_caractermayus in range(0,1):
        variable_alzar = random.randint(65,90)
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
        
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_de_caracter in range(0,1):
        variable_alzar = random.randint(97,122)   
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
    for cantidad_de_caracter in range(0,1):
        variable_alzar = random.randint(97,122)   
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
        
    
    
    for cantidad_de_simbolo in range (0,1):
        variable_alzar = random.randint(33,47)
        simbolo_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + simbolo_alzar
    x = x + 1
    if x == c:
        break
  return clave_valor1

def formato3():
  x = 0
  clave_valor1 = ""
  while x < c:

    for cantidad_de_caractermayus in range(0,1):
        variable_alzar = random.randint(65,90)
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
        
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break
    
    for cantidad_de_caracter in range(0,1):
        variable_alzar = random.randint(97,122)   
        caracter_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + caracter_alzar
    x = x + 1
    if x == c:
        break
        
    for cantidad_numerica in range(0,1):
        variable_alzar = random.randint(48,57)
        numero_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + numero_alzar
    x = x + 1
    if x == c:
        break 
    
          
    for cantidad_de_simbolo in range (0,1):
        variable_alzar = random.randint(33,47)
        simbolo_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + simbolo_alzar
    x = x + 1
    if x == c:
        break
 
    for cantidad_de_simbolo in range (0,1):
        variable_alzar = random.randint(33,47)
        simbolo_alzar = chr(variable_alzar)
        clave_valor1 = clave_valor1 + simbolo_alzar
    x = x + 1
    if x == c:
        break

  return clave_valor1
