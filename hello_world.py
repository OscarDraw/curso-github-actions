import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, soy {nombre} desde GitHub!")


if __name__ == "__main__":
    main()