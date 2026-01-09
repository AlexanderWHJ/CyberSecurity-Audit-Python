import os
import json

# Constante mayusculas (PEP 8)
DB_FILE = "auditoria_casino.json"
URGENTE_FILE = "URGENTE_REVISAR.json"

def procesar_auditoria():
    # 1. Entrada de datos simplificada
    print("-----  🛡 Sistema de auditoria casino  ----")
    nuevo_incidente = {
            "ip_atacante": input("IP atacante: ").strip().lower(),
            "puerto_afectado": input("Puerto afectado: ").strip().lower(),
            "gravedad": input("Gravedad del ataque: ").strip().lower()
        }
    
    # 2. Carga y actualiza la base de datos
    datos = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding = "utf-8") as f:
            datos = json.load(f)
            
    # El ID se genera de forma pitonica con max
    nuevo_id = max([int(k) for k in datos.keys()], default = 0) + 1
    datos[str(nuevo_id)] = nuevo_incidente
    
    # Guardado de la base maestra
    with open(DB_FILE, "w", encoding = "utf-8") as f:
        json.dump(datos, f, indent = 4, ensure_ascii = False)
    
    # 3. FILTRADO PITONISTA (list conprehesion 'in')
    # Extraemos solo gravedad alta o critica en un solo paso
    # El operador ** desempaqueta el diccionario original
    urgentes = [{"id": k, **v} for k, v in datos.items() if v['gravedad'] in {"alta", "critica"}] 
    
    # Guardar archivo de urgencia
    with open(URGENTE_FILE, "w", encoding = "utf-8") as f:
        json.dump(urgentes, f, indent = 4, ensure_ascii = False)
    
    print(f"\n✅ Proceso completado. {len(urgentes)} incidentes urgentes 'alta' y 'critica' detectados.")
    
if __name__ == "__main__":
    procesar_auditoria()
    
    