conj1 = {"a","b","c","d"}
conj2 = {"c","d","e","f"}

print("União:")
print(conj1 | conj2)

print("Intersecção:")
print(conj1 & conj2)

print("Diferença:")
print(conj1 - conj2)

print(f"Comprimento: {len(conj1)}")

print(f"Maior valor: {max(conj1)}, Menor valor: {min(conj1)}")