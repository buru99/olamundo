import flet as ft
import webbrowser

def main(page: ft.Page):
    
    def botao(e):
        link = "https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=8968211671279102359&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001540&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1"
        webbrowser.open(link)
    
    button = ft.TextButton("link", on_click=botao)
    
    
    
    page.add(button)
    

ft.app(main)
