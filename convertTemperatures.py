# Between Celcius and Fahrenheit
CtoF = lambda degs : (degs * (9/5)) + 32
FtoC = lambda degs : (degs - 32) * (5/9)

# Between Celcius and Kelvin
CtoK = lambda degs : degs + 273.15
KtoC = lambda degs : degs - 273.15

# Between Kelvin and Fahrenheit
KtoF = lambda degs : (degs - 273.15) * 9/5 + 32
FtoK = lambda degs : (degs - 32) * 5/9 + 273.15
