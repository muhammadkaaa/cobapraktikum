import flet as ft
import time

def main (page : ft.Page) :
    # t = ft.Text(value="Hello World", color="red")
    # t = ft.Text()

    # for i in range (5) :
    #     t.value = f"ini nomor ke {i}"
    #     page.update()
    #     print(page.controls)
    #     time.sleep(1)
    #     print(f"detik ke {i+1}")
    # # page.controls.append(t)
    page.add(
    ft.Row(controls=[
        ft.Text("D"),
        ft.Text("B"),
        ft.Text("C")
    ])
)

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

ft.app(target=main)