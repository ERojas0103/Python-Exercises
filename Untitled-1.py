def print_with_symbols(text):
    symbol_set = ["@", "#", "$", "%", "^", "&", "*", "-", "+",
                  "=", "~", "/", "(", ")", "[", "]", "{", "}", "|", "<", ">"]
    # Creamos una lista de símbolos disponibles
    symbol_index = 0
    # Establecemos el índice inicial de la lista en 0

    for char in text:
        if char == " ":
            print(" ", end="")
            continue
        symbol = symbol_set[symbol_index]
        # Obtenemos el símbolo actual de la lista
        print(symbol, end="")
        symbol_index = (symbol_index + 1) % len(symbol_set)
        # Actualizamos el índice para que apunte al siguiente símbolo de la lista

    print("")


text = input("Ingrese el texto a imprimir con símbolos: ")
print_with_symbols(text)
