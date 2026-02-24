from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def mostrar_menu():
    console.print("\n[bold green]=== SISTEMA INFORMATIVO DE FÚTBOL ===[/bold green]")
    console.print("1. Portero")
    console.print("2. Defensa")
    console.print("3. Mediocampista")
    console.print("4. Delantero")
    console.print("5. Ver todas las posiciones")
    console.print("6. Salir")

def mostrar_posicion(nombre, funcion, caracteristicas):
    table = Table(title=f"Posición: {nombre}")
    table.add_column("Función", style="cyan")
    table.add_column("Características", style="magenta")
    table.add_row(funcion, caracteristicas)
    console.print(table)

while True:
    mostrar_menu()
    opcion = Prompt.ask("Seleccione una opción")

    if opcion == "1":
        mostrar_posicion(
            "Portero",
            "Defender la portería y evitar goles",
            "Reflejos rápidos, liderazgo y buen posicionamiento"
        )

    elif opcion == "2":
        mostrar_posicion(
            "Defensa",
            "Evitar que el rival avance y recupere el balón",
            "Fuerza física, anticipación y marcaje"
        )

    elif opcion == "3":
        mostrar_posicion(
            "Mediocampista",
            "Conectar defensa y ataque",
            "Visión de juego, precisión en pases y resistencia"
        )

    elif opcion == "4":
        mostrar_posicion(
            "Delantero",
            "Anotar goles",
            "Velocidad, definición y movilidad ofensiva"
        )

    elif opcion == "5":
        mostrar_posicion(
            "Portero",
            "Defender la portería",
            "Reflejos y liderazgo"
        )
        mostrar_posicion(
            "Defensa",
            "Proteger la zona defensiva",
            "Marcaje y fuerza"
        )
        mostrar_posicion(
            "Mediocampista",
            "Organizar el juego",
            "Visión y precisión"
        )
        mostrar_posicion(
            "Delantero",
            "Finalizar jugadas",
            "Definición y velocidad"
        )

    elif opcion == "6":
        console.print("[bold red]Saliendo del programa...[/bold red]")
        break

    else:
        console.print("[red]Opción inválida[/red]")