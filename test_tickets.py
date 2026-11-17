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
        print("¡Login exitoso para pruebas de Tickets!")
except urllib.error.URLError as e:
    print("Error en login:", e)
    exit()

# 2. Crear un Ticket de prueba (POST /api/tickets/)
tickets_url = "http://127.0.0.1:8000/api/tickets/"
new_ticket_data = json.dumps({
    "title": "Falla en el servidor de base de datos",
    "description": "El servidor principal de MySQL no responde tras el reinicio nocturno.",
    "status": "OPEN",
    "priority": "CRITICAL",
    "organization": 1,  # Empresa de prueba S.A.S. (ID 1)
    "sla_policy": 1     # SLA Soporte Crítico (ID 1)
}).encode("utf-8")

req_post = urllib.request.Request(
    tickets_url,
    data=new_ticket_data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

try:
    with urllib.request.urlopen(req_post) as response:
        created_ticket = json.loads(response.read().decode())
        print("\n¡Ticket creado con éxito!")
        print(json.dumps(created_ticket, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al crear ticket {e.code}: {e.read().decode()}")

# 3. Listar todos los tickets (GET /api/tickets/)
req_get = urllib.request.Request(
    tickets_url, 
    headers={"Authorization": f"Bearer {token}"}
)

try:
    with urllib.request.urlopen(req_get) as response:
        tickets = json.loads(response.read().decode())
        print("\nListado actual de Tickets:")
        print(json.dumps(tickets, indent=4))
except urllib.error.HTTPError as e:
    print(f"Error HTTP al listar tickets {e.code}: {e.read().decode()}")