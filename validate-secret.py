import os

# Obtener el valor de la variable de entorno TEST_SECRET
test_secret = os.getenv('secret_variable')

# Imprimir el valor de la variable de entorno
print(f'Variable secreta: {test_secret}')