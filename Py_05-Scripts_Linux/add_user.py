import subprocess

def preguntar_si_no(mensaje):
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        print("Respuesta no válida. Introduce 's' o 'n'.")

def main():
    usuario = input("Introduce el nombre del nuevo usuario: ").strip()
    if not usuario:
        print("Nombre de usuario no válido.")
        return

    comando = ["useradd"]

    if preguntar_si_no("¿Deseas crear un directorio home para el usuario?"):
        comando.append("-m")

    if preguntar_si_no("¿Deseas asignar un shell específico?"):
        shell = input("Indica el shell (por ejemplo /bin/sh): ").strip()
        if shell:
            comando.extend(["-s", shell])

    if preguntar_si_no("¿Deseas establecer un UID específico?"):
        uid = input("Introduce el UID: ").strip()
        if uid.isdigit():
            comando.extend(["-u", uid])
        else:
            print("UID no válido. Se omitirá esta opción.")

    comando.append(usuario)

    print("\nComando a ejecutar:")
    print(" ".join(comando))

    try:
        subprocess.run(comando, check=True)
        print(f"\n✅ Usuario '{usuario}' creado correctamente.")
    except subprocess.CalledProcessError:
        print(f"\n❌ Error al crear el usuario '{usuario}'.")

if __name__ == "__main__":
    main()
