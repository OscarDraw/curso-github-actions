import os

def main():
    nombre = os.getenv("USERNAME")
    ocupation = os.getenv("OCUPATION")
    print(f"*******************************************")
    print(f"Se confirma que {nombre} es un {ocupation}!")
    print(f"*******************************************")

if __name__ == "__main__":
    main()