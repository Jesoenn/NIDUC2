import reedsolo

# Inicjalizacja koderu z 10 symbolami parzystości (to można dostosować)
rs = reedsolo.RSCodec(10)

# Przykładowy ciąg bitów
bits = "11010101010001101000"

# Przekształcamy ciąg bitów na bajty
# Grupujemy po 8 bitów, konwertujemy na bajty (dodaj zera, jeśli długość nie jest wielokrotnością 8)
byte_array = int(bits, 2).to_bytes((len(bits) + 7) // 8, byteorder='big')

# Kodowanie w Reed-Solomon
encoded = rs.encode(byte_array)

print("Zakodowane dane (w formie bajtów):", encoded)