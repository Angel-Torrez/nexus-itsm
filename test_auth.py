import urllib.request
import json

# 1. Hacer login enviando las credenciales por POST
login_url = "http://127.0.0.1:8000/api/auth/login/"
payload = json.dumps({
    "username": "admin_test",
    "password": "SuperPassword123!"
}).encode("utf-8")

req_login = urllib.request.Request(
    login_url, 
    data=payload, 
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req_login) as response:
        body = json.loads(response.read().decode())
        token = body["access"]
        print("¡Login exitoso! Token obtenido correctamente.")
except urllib.error.URLError as e:
    print("Error en login:", e)
    exit()

# 2. Consultar el endpoint protegido /api/auth/me/ enviando el token en el formato exacto Bearer
me_url = "http://127.0.0.1:8000/api/auth/me/"
req_me = urllib.request.Request(
    me_url, 
    headers={"Authorization": f"Bearer {token}"}
)

try:
    with urllib.request.urlopen(req_me) as response:
        profile = json.loads(response.read().decode())
        print("\n¡Acceso autorizado a /api/auth/me/!")
        print(json.dumps(profile, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP {e.code}: {e.read().decode()}")