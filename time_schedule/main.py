import flet as ft

def main(page: ft.Page):
    # ページの設定
    page.title = "時間割アプリ"
    page.bgcolor = ft.colors.WHITE
    
    # タイトルバー
    title_bar = ft.Container(
        content=ft.Text("時間割", color=ft.colors.WHITE, size=24, weight="bold"),
        bgcolor=ft.colors.RED,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center
    )
    
    # 曜日行の作成
    days_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("月", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("火", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("水", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("木", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("金", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("土", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
            ft.Container(
                content=ft.Text("日", size=25, weight="bold"),
                alignment=ft.alignment.center,
                width=160
            ),
        ],
        alignment=ft.MainAxisAlignment.START, 
        spacing=5 #位置微調整
    )
    
    # 時間割セルの作成
    timetable_grid = ft.Column(spacing=5)
    for _ in range(5):  # 5行（コマ数）
        row = ft.Row(spacing=5)
        for _ in range(7):  # 7列（曜日数）
            cell = ft.Container(
                bgcolor=ft.colors.GREY_300,
                width=160,
                height=90,
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.all(5)
            )
            row.controls.append(cell)
        timetable_grid.controls.append(row)
    
    # 全体レイアウトの組み立て
    page.add(
        ft.Column(
            controls=[
                title_bar,
                ft.Container(height=10),  # タイトルバーとの余白
                days_row,
                ft.Container(height=10),  # 曜日行との余白
                timetable_grid
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
