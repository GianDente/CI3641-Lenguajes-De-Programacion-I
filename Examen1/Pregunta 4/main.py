import cuaterniones

print("\n")
print("Sean los cuaterniones:")
cuaternion1 = cuaterniones.Cuaternion(1, 1, 1, 1)
cuaternion2 = cuaterniones.Cuaternion(1, 1, 1, 1)

print(f"cuaternion1 = {cuaternion1}")
print(f"cuaternion2 = {cuaternion2}")
print("\n")

print("---pruebas unitarias---")

print("suma de dos cuaterniones (suma componente a componente):")
print(f"({cuaternion1}) + ({cuaternion2}) = {cuaternion1 + cuaternion2}")
print("suma de un cuaternion con un escalar:")
print(f"({cuaternion1}) + 7 = {cuaternion1 + 7}")
print("\n")

print("producto de dos cuaterniones:")
print(f"({cuaternion1}) * ({cuaternion2}) = {cuaternion1 * cuaternion2}")
print("producto de un cuaternion con un escalar:")
print(f"({cuaternion1}) * 7 = {cuaternion1 * 7}")

print("\n")

print("conjugada:")
print(f"~({cuaternion1}) = {~cuaternion1}")

print("\n")

print("medida o valor absoluto:") # reemplazando el simbolo & por el -
print(f"-({cuaternion1}) = {-cuaternion1}")

print("\n")

print("----------------------------------------------")
print("Sean los cuaterniones:")
a = cuaterniones.Cuaternion(1, 1, 1, 1)
b = cuaterniones.Cuaternion(2, 2, 2, 2)
c = cuaterniones.Cuaternion(3, 3, 3, 3)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("\n")

# Parte (b):
print(f"b + c = {b + c}")
print(f"a * b + c = {a * b + c}")
print(f"(b + b) * (c + ~a) = {(b + b) * (c + (~a))}")
print(f"-(c * b) = {-(c * b)}")
print("\n")

# Parte (c):
print(f"b + 3 = {b + 3}")
print(f"a * 3.0 + 7.0 = {a * 3.0 + 7.0}")
print(f"(b + b) * -c = {(b + b) * (-c)}")
