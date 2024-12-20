import flet as ft
from sqlalchemy.orm import Session
from models import Habito
from config import SessionLocal
from datetime import datetime, timezone
from views.habit_actions import delete_habito, update_habito_status
from views.habit_edit import edit_habito_dialog  # Importando função de edição

db: Session = SessionLocal()

def get_habitos(order_by="id"):
    if order_by == "concluido":
        return db.query(Habito).order_by(Habito.concluido, Habito.data_criacao.desc()).all()
    elif order_by == "data":
        return db.query(Habito).order_by(Habito.data_criacao.desc(), Habito.concluido).all()
    else:
        return db.query(Habito).order_by(Habito.id.desc()).all()

def habit_list(page, atualizar, order_by="id"):
    habitos = get_habitos(order_by)

    if not habitos:
        controls = [ft.Text(value="Você não tem nenhum hábito cadastrado!", size=20, color=ft.Colors.WHITE)]
    else:
        controls = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=hl.titulo,
                            value=hl.concluido,
                            on_change=atualizar
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color=ft.Colors.YELLOW,
                                    on_click=lambda e, titulo=hl.titulo: edit_habito_dialog(page, titulo, atualizar)
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color=ft.Colors.RED,
                                    on_click=lambda e, titulo=hl.titulo: confirm_delete(page, titulo, atualizar)
                                )
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                padding=ft.padding.symmetric(vertical=5)  # Diminuindo o espaçamento vertical
            ) for hl in habitos
        ]

    return ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        bgcolor=ft.Colors.GREY_900,
        border_radius=ft.border_radius.all(20),
        margin=ft.margin.symmetric(vertical=30),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=5,  # Ajustar o espaçamento vertical entre os hábitos
            controls=controls
        )
    )

def confirm_delete(page, titulo, atualizar):
    def on_confirm(e):
        delete_habito(titulo)
        page.dialog.open = False
        atualizar()

    def on_cancel(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        title=ft.Text("Confirmação"),
        content=ft.Text("Você tem certeza que deseja deletar este hábito? Esta ação não poderá ser desfeita."),
        actions=[
            ft.TextButton("Deletar", on_click=on_confirm),
            ft.TextButton("Cancelar", on_click=on_cancel)
        ],
        on_dismiss=lambda e: print("Dialog dismissed!")
    )

    page.dialog = dialog
    dialog.open = True
    page.update()
