import pandas as pd
import matplotlib.pyplot as plt
import tempfile
from shiny import App, ui, render

# Carga del dataset (puedes reemplazar esto con tu propio archivo CSV)
df = pd.read_csv("data/raw/laptop_price - dataset.csv")

# Interfaz de usuario
app_ui = ui.page_fluid(
    ui.h2("Gráfica de barras basada en un dataset"),
    ui.row(
        ui.column(4, ui.output_image("bar_plot1")),
        ui.column(4, ui.output_image("bar_plot2")),
        ui.column(4, ui.output_image("bar_plot3"))
    )
)

# Lógica del servidor
def server(input, output, session):
    @output
    @render.image
    def bar_plot1():
        # Crear la gráfica de barras
        fig, ax = plt.subplots()
        ax.bar(df['RAM (GB)'], df['Price (Euro)'], color='skyblue')
        ax.set_title("Gráfica de Barras")
        ax.set_xlabel("Company")
        ax.set_ylabel("price")
        
        # Guardar la gráfica como un archivo temporal
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        plt.savefig(temp_file.name)
        plt.close(fig)  # Cerrar la figura para liberar recursos
        
        # Retornar la ruta del archivo
        return {
            "src": temp_file.name,  # Ruta al archivo temporal
            "width": "100%",  # Ajustar el ancho según sea necesario
            "height": "auto"
        }

    @output
    @render.image
    def bar_plot2():
        # Crear la gráfica de barras
        fig, ax = plt.subplots()
        ax.bar(df['RAM (GB)'], df['Price (Euro)'], color='skyblue')
        ax.set_title("Gráfica de Barras")
        ax.set_xlabel("Company")
        ax.set_ylabel("price")
        
        # Guardar la gráfica como un archivo temporal
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        plt.savefig(temp_file.name)
        plt.close(fig)  # Cerrar la figura para liberar recursos
        
        # Retornar la ruta del archivo
        return {
            "src": temp_file.name,  # Ruta al archivo temporal
            "width": "100%",  # Ajustar el ancho según sea necesario
            "height": "auto"
        }

    @output
    @render.image
    def bar_plot3():
        # Crear la gráfica de barras
        fig, ax = plt.subplots()
        ax.bar(df['RAM (GB)'], df['Price (Euro)'], color='skyblue')
        ax.set_title("Gráfica de Barras")
        ax.set_xlabel("Company")
        ax.set_ylabel("price")
        
        # Guardar la gráfica como un archivo temporal
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        plt.savefig(temp_file.name)
        plt.close(fig)  # Cerrar la figura para liberar recursos
        
        # Retornar la ruta del archivo
        return {
            "src": temp_file.name,  # Ruta al archivo temporal
            "width": "100%",  # Ajustar el ancho según sea necesario
            "height": "auto"
        }

# Crear la aplicación
app = App(app_ui, server)
