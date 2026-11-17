import urllib.request
import json

# 1. Obtener el token JWT haciendo login
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
        token = json.loads(response.read().decode())["access"]
        print("¡Login exitoso para pruebas de SLAs!")
except (urllib.error.URLError, json.JSONDecodeError, KeyError) as e:
    print("Error en login:", e)
    exit()

# 2. Crear una política de SLA de prueba (POST /api/slas/)
slas_url = "http://127.0.0.1:8000/api/slas/"
new_sla_data = json.dumps({
    "name": "SLA Soporte Crítico",
    "priority": "CRITICAL",
    "response_time_hours": 1,
    "resolution_time_hours": 4,
    "organization": 1,  # Vinculada a la empresa de prueba (ID 1)
    "is_active": True
}).encode("utf-8")

req_post = urllib.request.Request(
    slas_url,
    data=new_sla_data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req_post) as response:
        created_sla = json.loads(response.read().decode())
        print("\n¡Política SLA creada con éxito!")
        print(json.dumps(created_sla, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al crear SLA {e.code}: {e.read().decode()}")

# 3. Listar todas las políticas SLA (GET /api/slas/)
req_get = urllib.request.Request(
    slas_url, 
    headers={"Authorization": f"Bearer {token}"}
)

try:
    with urllib.request.urlopen(req_get) as response:
        slas = json.loads(response.read().decode())
        print("\nListado actual de Políticas SLA:")
        print(json.dumps(slas, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al listar SLAs {e.code}: {e.read().decode()}")