import random
import math

def generate_key(length):
    key = list(range(length))
    random.shuffle(key)
    return key

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    spaltenanzahl = len(key)
    zeilenanzahl = math.ceil(len(plaintext) / spaltenanzahl)
    padded_length = zeilenanzahl * spaltenanzahl
    plaintext = plaintext.ljust(padded_length, 'X')
    grid = [plaintext[i:i+spaltenanzahl] for i in range(0, len(plaintext), spaltenanzahl)]
    ciphertext = ''
    for col in key:
        for row in grid:
            ciphertext += row[col]
    return ciphertext

def decrypt(ciphertext, key):
    spaltenzahl = len(key)
    zeilenanzahl = len(ciphertext) // spaltenzahl
    grid = [''] * zeilenanzahl
    for i in range(zeilenanzahl):
        grid[i] = [''] * spaltenzahl
    #umgedrehter_key = [0] * len(key)
    #for i, k in enumerate(key):
    #    umgedrehter_key[k] = i
    index = 0
    for col in key:
        for row in range(zeilenanzahl):
            grid[row][int(col)] = ciphertext[index]
            index += 1
    plaintext = ''.join([''.join(row) for row in grid])
    return plaintext.rstrip('X')

if __name__ == "__main__":
    print('Spaltentranspositionschiffre')
    print('============================')
    print("1. Verschlüsseln")
    print("2. Entschlüsseln")
    print("3. Beenden")
    while True:
        wahl = input("Bitte Option wählen (1, 2 oder 3): ")
        if wahl == '1':
            text = input("Gib den Klartext ein: ")
            key_length = int(input("Schlüssel-Länge (Anzahl Spalten): "))
            key = generate_key(key_length)
            ciphertext = encrypt(text, key)
            decrypted = decrypt(ciphertext, key)
            print("\nVerschlüsselter Text:", ciphertext)
            print("Entschlüsselter Text:", decrypted)
            print("Verwendeter Schlüssel:", key)
        elif wahl == '2':
            ciphertext = input("Gib den Geheimtext ein: ")
            key = input("Gib den Key ein (z.B.: 3,1,2,0): ")
            key = key.split(",")
            decrypted = decrypt(ciphertext, key)
            print(f"Entschlüsselter Text: {decrypted}")
        elif wahl == '3':
            break
        else:
            print("Ungültige Auswahl. Bitte 1, 2 oder 3 eingeben.")
