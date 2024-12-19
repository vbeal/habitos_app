import flet as ft

def main(page: ft.Page):
    page.padding = ft.padding.all(30)
    page.bgcolor = ft.colors.BLACK
    page.title = 'Hábitos App'
    page.window_width = 450
    page.window_height = 1000

    lista_de_habitos = [
        { 'titulo': 'Fazer exercícios', 'concluido': False},
        { 'titulo': 'Praticar Violão', 'concluido': False},
        { 'titulo': 'Estudar Inglês', 'concluido': False},
        { 'titulo': 'Fazer compras', 'concluido': False},
    ]

    def atualizar(e=None):
        print(e.control.value if e else "Atualizando barra de progresso")
        for hl in lista_de_habitos:
            if e and hl['titulo'] == e.control.label:
                hl['concluido'] = e.control.value
        
        concluido = list(filter(lambda x: x['concluido'], lista_de_habitos))
        total = len(concluido) / len(lista_de_habitos)
        
        progresso_barra.value = total  # Definindo como float
        progresso_texto.value = f'{total:.0%}'  # String formatada para texto
        
        progresso_barra.update()
        progresso_texto.update()
        print(f'{total:.0%}', total)
  
    def adicionar_habito(e):
        print(e.control.value)
        lista_de_habitos.append({'titulo': e.control.value, 'concluido': False})
        habitos.content.controls = [
            ft.Checkbox(
                label= hl['titulo'],
                value= hl['concluido'],
                on_change= atualizar
            ) for hl in lista_de_habitos
        ]
        habitos.update()
        e.control.value = ''
        e.control.update()
        e.control.focus()
        atualizar()  # Chamar atualizar para refletir a mudança na barra de progresso

    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(
                value= 'Que bom ter você por aqui!',
                size= 30,
                color= ft.colors.WHITE
            ),
            ft.Text(
                value= 'Como estão seu hábitos hoje?',
                size= 20,
                color= ft.colors.WHITE
            ),
            ft.Container(
                padding= ft.padding.all(30),
                bgcolor= ft.colors.INDIGO,
                border_radius= ft.border_radius.all(20),
                margin= ft.margin.symmetric(vertical=30),
                content= ft.Column(
                    controls=[
                        ft.Text(
                            value= 'Sua evolução hoje', size= 20, color= ft.colors.WHITE
                        ),
                        progresso_texto := ft.Text(
                            value= '0%', size=50, color= ft.colors.WHITE
                        ),
                        progresso_barra := ft.ProgressBar(
                            value= 0,
                            color= ft.colors.INDIGO_900,
                            bgcolor= ft.colors.INDIGO_100,
                            height= 20,
                        ),
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Text(
                value= 'Hábitos de hoje', 
                size= 20, 
                color= ft.colors.WHITE,
                weight= ft.FontWeight.BOLD
            ),
            ft.Text(
                value= 'Marcar suas tarefas como concluídas te motiva a continuar focado!',
                size= 15,
                color= ft.colors.WHITE
            ),
            habitos := ft.Container(
                expand= True,
                padding= ft.padding.all(30),
                bgcolor= ft.colors.GREY_900,
                border_radius= ft.border_radius.all(20),
                margin= ft.margin.symmetric(vertical=30),
                content= ft.Column(
                    expand= True,
                    scroll= ft.ScrollMode.ALWAYS,  # Garantir que a barra de rolagem esteja sempre visível
                    spacing= 20,
                    controls=[
                        ft.Checkbox(
                            label= hl['titulo'],
                            value= hl['concluido'],
                            on_change= atualizar,
                        ) for hl in lista_de_habitos
                    ]
                )
            ),
            ft.Text(
                value= 'Adicionar novo Hábito', size= 20, color= ft.colors.WHITE
            ),
            ft.TextField(
                hint_text= 'Digite um novo hábito',
                border_color= ft.colors.WHITE,
                border_width= 0.3,
                color= ft.colors.WHITE,
                on_submit= adicionar_habito
            )
        ]
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
