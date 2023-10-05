from tkinter import *
from tkinter import ttk  # Importa el módulo ttk para el scrollbar
from ui import get_user_input
from api import generate_sample_data

def display_data(data):
    # Crear una ventana emergente
    window = Tk()

    # Configurar la ventana
    window.title("Datos del departamento")
    window.geometry("800x600")

    # Crear un canvas para agregar la barra de desplazamiento vertical
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Agregar una barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configurar el canvas para que funcione con la barra de desplazamiento
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Crear un frame dentro del canvas para mostrar los datos
    table = Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor="nw")

    # Crear las etiquetas de encabezado
    headers = ['Ciudad/Municipio', 'Departamento', 'Edad', 'Fuente/Tipo de Contagio', 'Estado', 'País Viajó']
    for i, header in enumerate(headers):
        label = Label(table, text=header, font=("Arial", 12, "bold"), padx=10, pady=10)
        label.grid(row=0, column=i)

    # Mostrar los datos en la tabla
    for i, row in data.iterrows():
        for j, value in enumerate(row):
            label = Label(table, text=value, font=("Arial", 12), padx=10, pady=10)
            label.grid(row=i + 1, column=j)

    # Configurar el evento de desplazamiento en el canvas
    def on_canvas_scroll(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    canvas.bind_all("<MouseWheel>", on_canvas_scroll)

    # Crear un botón para cerrar la ventana
    close_button = Button(window, text="Cerrar", font=("Arial", 12), command=window.destroy)
    close_button.pack(side=BOTTOM, padx=10, pady=10)

    # Mostrar la ventana
    window.mainloop()

def main():
    # Obtener los datos de entrada del usuario
    departamento, limite_registros = get_user_input()

    # Obtener los datos de la API
    data = generate_sample_data(departamento, limite_registros)

    # Verificar que data no es None antes de seleccionar las columnas
    if data is not None:
        # Seleccionar solo las columnas requeridas
        data = data[['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']]

        # Mostrar los datos en una ventana emergente
        display_data(data)
        print("Datos obtenidos correctamente.\n", data)
    else:
        print("No se pudo obtener datos para el departamento ingresado.")

if __name__ == "__main__":
    main()