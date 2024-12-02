#definimos la estructura del grafo con sus aristas

def crear_grafo():
    return {
        "Almacen":{"CiudadA": 5, "CiudadB": 2},
        "CiudadA":{"Almacen": 5, "CiudadB": 1, "CiudadC": 7},
        "CiudadB":{"Almacen": 2, "CiudadA": 1, "CiudadD": 4},
        "CiudadC":{"CiudadA": 7, "CiudadD": 3},
        "CiudadD":{"CiudadB": 4, "CiudadC": 3},
    }

def obtener_aritas():
    return [
        ("Almacen", "CiudadA", 5),
        ("Almacen", "CiudadB", 2),
        ("CiudadA", "CiudadB", 1),
        ("CiudadA", "CiudadC", 7),
        ("CiudadB", "CiudadD", 4),
        ("CiudadC", "CiudadD", 3)
    ]

def obtener_nodos():
    return {"Almacen", "CiudadA", "CiudadB", "CiudadC", "CiudadD"}