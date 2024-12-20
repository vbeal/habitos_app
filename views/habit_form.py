import flet as ft

def habit_form(atualizar):
    return ft.TextField(
        hint_text='Digite um novo hábito aqui e tecle enter',
        border_color=ft.colors.WHITE,
        border_width=0.3,
        color=ft.colors.WHITE,
        max_length=25,  # Limite de caracteres
        on_submit=atualizar
    )
