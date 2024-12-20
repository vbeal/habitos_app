import flet as ft
from views.habit_list import habit_list, get_habitos
from views.habit_actions import add_habito, update_habito_status  # Importando funções refatoradas
from views.habit_form import habit_form

def main(page: ft.Page):
    page.padding = ft.padding.all(30)
    page.bgcolor = ft.colors.BLACK
    page.title = 'Hábitos App'
    page.window_width = 450
    page.window_height = 1000

    def atualizar(e=None):
        if e:
            if e.control.__class__.__name__ == 'Checkbox':
                update_habito_status(e.control.label, e.control.value)
            elif e.control.__class__.__name__ == 'TextField' and e.control.value.strip() != '':
                add_habito(e.control.value.strip())
        
        atualizar_progresso()
        atualizar_lista_habitos()
        if e and e.control.__class__.__name__ == 'TextField':
            e.control.value = ''
            e.control.update()
            e.control.focus()

    def atualizar_lista_habitos(order="id"):
        habitos_container.content = habit_list(page, atualizar, order)
        page.update()

    def atualizar_progresso():
        lista_de_habitos = get_habitos(order_by.value)
        concluido = list(filter(lambda x: x.concluido, lista_de_habitos))
        total = len(concluido) / len(lista_de_habitos) if len(lista_de_habitos) > 0 else 0

        progresso_barra.value = total
        progresso_texto.value = f'{total:.0%}'
        progresso_barra.update()
        progresso_texto.update()

    order_by_label = ft.Text(
        value="Ordenar por:",
        size=15,
        color=ft.Colors.WHITE
    )

    order_by = ft.Dropdown(
        options=[
            ft.dropdown.Option("id", "ID de Cadastro"),
            ft.dropdown.Option("concluido", "Concluído"),
            ft.dropdown.Option("data", "Data de Criação")
        ],
        value="id",
        width=200,  # Ajustar a largura para ser menor
        on_change=lambda e: atualizar_lista_habitos(e.control.value)
    )

    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(
                value='Que bom ter você por aqui!',
                size=30,
                color=ft.Colors.WHITE
            ),
            ft.Text(
                value='Como estão seus hábitos hoje?',
                size=20,
                color=ft.Colors.WHITE
            ),
            ft.Container(
                padding=ft.padding.all(30),
                bgcolor=ft.Colors.INDIGO,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=30),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Sua evolução hoje', size=20, color=ft.Colors.WHITE
                        ),
                        progresso_texto := ft.Text(
                            value='0%', size=50, color=ft.Colors.WHITE
                        ),
                        progresso_barra := ft.ProgressBar(
                            value=0,
                            color=ft.Colors.INDIGO_900,
                            bgcolor=ft.Colors.INDIGO_100,
                            height=20,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Text(
                value='Hábitos de hoje',
                size=20,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                value='Marcar suas tarefas como concluídas te motiva a continuar focado!',
                size=15,
                color=ft.Colors.WHITE
            ),
            ft.Row(
                controls=[order_by_label, order_by],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,  # Espaçamento entre o rótulo e o dropdown
            ),
            habitos_container := ft.Container(expand=True),
            habit_form(atualizar)
        ],
        spacing=10  # Ajustar o espaçamento para aproximar os elementos
    )

    page.add(layout)
    atualizar_progresso()  # Atualizar progresso ao abrir o aplicativo
    atualizar_lista_habitos()

if __name__ == '__main__':
    from database import *
    ft.app(target=main)
