
import flet as ft
from vision_engine import VisionSystem


def main(page: ft.Page):
    page.title = "HackEnginePro"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#101116"
    page.padding = 20

    vision = VisionSystem()

    status = ft.Text(
        "SISTEMA PRONTO",
        color="#A78BFA",
        weight=ft.FontWeight.BOLD
    )

    results = ft.Text("Aguardando simulação...")
    log = ft.Text("HackEnginePro iniciado.")

    def scan(e):
        env = vision.scan_environment()
        target = vision.get_best_target()

        status.value = "SIMULAÇÃO CONCLUÍDA"

        results.value = (
            f"Jogadores simulados: {len(env['players'])}\n"
            f"Baús simulados: {len(env['chests'])}\n"
            f"Portas simuladas: {len(env['doors'])}\n"
            f"Nível de ameaça: {env['threat_level']}\n"
            f"Alvo de demonstração: "
            f"{target['type'] if target else 'Nenhum'}"
        )

        log.value = "Nova simulação executada."
        page.update()

    def clear(e):
        status.value = "SISTEMA PRONTO"
        results.value = "Aguardando simulação..."
        log.value = "Painel reiniciado."
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "HACK ENGINE PRO",
                    size=27,
                    weight=ft.FontWeight.BOLD,
                    color="#A78BFA"
                ),
                ft.Text("ANDROID CONTROL CENTER"),
                ft.Divider(),

                ft.Text("STATUS DO SISTEMA"),
                status,

                ft.Divider(),

                ft.Text(
                    "VISION SYSTEM",
                    size=19,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Container(
                    content=results,
                    bgcolor="#20212A",
                    padding=15,
                    border_radius=12
                ),

                ft.ElevatedButton(
                    "REALIZAR SIMULAÇÃO",
                    icon=ft.icons.SEARCH,
                    on_click=scan
                ),

                ft.OutlinedButton(
                    "REINICIAR PAINEL",
                    on_click=clear
                ),

                ft.Divider(),
                ft.Text("SYSTEM LOG"),
                log,

                ft.Text(
                    "HACK ENGINE PRO • V1.0",
                    color="#777777",
                    size=11
                )
            ],
            spacing=15
        )
    )


ft.run(main)
