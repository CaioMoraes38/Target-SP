def inverte_string(string):
    inverted = ""
    for i in range(len(string)-1, -1, -1):
        inverted += string[i]

    return inverted

def main():
    string = input("Digite uma string: ")
    resultado = inverte_string(string)
    print("String invertida:", resultado)

if __name__ == "__main__":
    main()