import flet as ft
from views.habit_actions import update_habito

def edit_habito_dialog(page, titulo, atualizar):
    def on_submit(e):
        update_habito(old_title, new_title.value)
        page.dialog.open = False
        atualizar()

    def on_cancel(e):
        page.dialog.open = False
        page.update()

    old_title = titulo
    new_title = ft.TextField(label="Novo Título", value=titulo, width=300, max_length=25)  # Limite de 25 caracteres

    dialog_content = ft.Container(
        content=ft.Column([
            new_title,
            ft.Row([
                ft.ElevatedButton("Salvar", on_click=on_submit),
                ft.ElevatedButton("Cancelar", on_click=on_cancel)
            ], alignment=ft.MainAxisAlignment.CENTER)
        ]),
        width=350,
        height=150,
        padding=ft.padding.all(20),
        alignment=ft.alignment.center,
        # bgcolor=ft.Colors.GREY_800  # Fundo cinza escuro
    )

    dialog = ft.AlertDialog(
        bgcolor=ft.Colors.GREY_800,
        title=ft.Text("Editar Hábito"),
        content=dialog_content,
        on_dismiss=lambda e: print("Dialog dismissed!"),
        modal=True
    )

    page.dialog = dialog
    dialog.open = True
    page.update()
