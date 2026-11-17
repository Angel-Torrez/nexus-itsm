import urllib.request
import json

# 1. Obtener el token JWT haciendo login con nuestro usuario admin
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
        print("¡Login exitoso para pruebas de organizaciones!")
except Exception as e:
    print("Error en login:", e)
    exit()

# 2. Listar las organizaciones (GET /api/organizations/)
orgs_url = "http://127.0.0.1:8000/api/organizations/"
req_get = urllib.request.Request(
    orgs_url, 
    headers={"Authorization": f"Bearer {token}"}
)

try:
    with urllib.request.urlopen(req_get) as response:
        orgs = json.loads(response.read().decode())
        print("\nListado actual de Organizaciones:")
        print(json.dumps(orgs, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al listar organizaciones {e.code}: {e.read().decode()}")

# 3. Crear una nueva organización de prueba (POST /api/organizations/)
new_org_data = json.dumps({
    "name": "Empresa de Prueba S.A.S.",
    "code": "NIT-900123456",
    "description": "Organización creada mediante script de prueba automatizado.",
    "is_active": True
}).encode("utf-8")

req_post = urllib.request.Request(
    orgs_url,
    data=new_org_data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req_post) as response:
        created_org = json.loads(response.read().decode())
        print("\n¡Organización creada con éxito!")
        print(json.dumps(created_org, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al crear organización {e.code}: {e.read().decode()}")