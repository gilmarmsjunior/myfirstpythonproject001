import dearpygui.dearpygui as dpg

# Criar contexto e viewport
dpg.create_context()
dpg.create_viewport(title="Exemplo", width=400, height=300)

# Criar janela
with dpg.window(label="Exemplo"):
    dpg.add_text("Oi Ju! 😄")
    dpg.add_button(label="Fechar", callback=lambda: dpg.stop_dearpygui())

# Mostrar a janela e iniciar
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
