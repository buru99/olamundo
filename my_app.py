import flet as ft
import webbrowser

def main(page: ft.Page):
    
    def botao(e):
        page.add(ft.Text("olá"))
        page.update()
        
    
    button = ft.TextButton("link", on_click=botao)
    
    
    
    page.add(button)
    

ft.app(main)
