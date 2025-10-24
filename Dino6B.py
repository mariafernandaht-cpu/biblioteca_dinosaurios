#🦖 Biblioteca de dinosaurios 🦕

# Lista prellenada de dinosaurios con su información
dinosaurios = [
    ("Tiranosaurio Rex", "Carnivoro", "12 metros", "Cretacico", "Tenía brazos muy cortos pero mandíbulas poderosas"),
    ("Triceratops", "Herbivoro", "9 metros", "Cretacico", "Tenía 3 cuernos y un gran volante óseo"),
    ("Velociraptor", "Carnivoro", "2 metros", "Cretacico", "Tenía una garra en forma de hoz en cada pata"),
    ("Brachiosaurus", "Herbivoro", "25 metros", "Jurasico", "Tenía un cuello larguísimo para alcanzar hojas altas"),
    ("Stegosaurio", "Herbivoro", "9 metros", "Jurasico", "Tenía placas en la espalda y púas en la cola"),
    ("Spinosaurus", "Carnivoro", "15 metros", "Cretacico", "Tenía una vela en la espalda y era semiacuático"),
    ("Ankylosaurus", "Herbivoro", "8 metros", "Cretacico", "Estaba acorazado y tenía una maza en la cola"),
    ("Pteranodon", "Carnivoro", "7 metros de envergadura", "Cretacico", "Era un reptil volador, pero no era un dinosaurio"),
    ("Diplodocus", "Herbivoro", "10 metros", "Jurasico", "Uno de los dinosaurios más largos que existieron"),
    ("Parasaurolophus", "Herbivoro", "10 metros", "Cretacico", "Tenía una cresta hueca para hacer sonidos"),
]

print("="*60)
print("🦖 Bienvenido a la biblioteca de dinosaurios 🦕")
print("="*60)
print("Pregunta por cualquier dinosaurio y te daré su información.")
print("Escribe 'lista' para ver todos los dinosaurios disponibles.")
print("Escribe 'salir' para terminar.\n")

while True:
    consulta = input("¿Qué dinosaurio quieres consultar? ").strip().lower()

    if consulta == "salir":
        print("👋 ¡Hasta luego, explorador de dinosaurios!")
        break

    if consulta == "lista":
        print("\n📝 Dinosaurios disponibles")
        for i, (nombre, _, _, _, _) in enumerate(dinosaurios, 1):
            print(f"{i}. {nombre}")
        print()
        continue

    # Buscar el dinosaurio en la lista
    encontrado = False
    for nombre, dieta, tamaño, periodo, dato_curioso in dinosaurios:
        if consulta in nombre.lower():
            print("\n" + "="*60)
            print(f"🦕 {nombre}")
            print("="*60)
            print(f"🍖 Dieta: {dieta}")
            print(f"📏 Tamaño: {tamaño}")
            print(f"⏳ Periodo: {periodo}")
            print(f"💡 Dato curioso: {dato_curioso}")
            print("="*60 + "\n")
            encontrado = True
            break
    if not encontrado:
        print(f"❌ No encontré información sobre '{consulta}'.")
        print("💡 Intenta escribir 'lista' para ver los dinosaurios disponibles.\n")