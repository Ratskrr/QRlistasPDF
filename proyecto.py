#bibliotecas
import pandas as pd
from fpdf import FPDF


#crear listas
datos = [
    {
        "Nombre": "Fabian",
        "Apellido": "Frias",
        "Dni": "51700999",
        "Dirección": "Vidal 740",
        "Carrera": "Programación",
        "Mail": "fabian.frias11@gmail.com"
    },
    {
        "Nombre": "Miguel",
        "Apellido": "Escalada",
        "Dni": "999000666",
        "Dirección": "Av. Uruguay 001",
        "Carrera": "Programación",
        "Mail": "miguesc@gmail.com"
    }
]

#convertir las listas en un dataFrame de pandas
df = pd.DataFrame(datos)

#crear una clase heredada de FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Listado de Personas", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, data):
        self.set_font("Arial", "", 12)
        for row in data:
            for key, value in row.items():
                self.cell(40, 10, f"{key}: ", align="L")
                self.cell(0, 10, str(value), align="L")
                self.ln()
            self.ln(5)

#crear una instancia de la clase pdf
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Listado de Personas")
pdf.chapter_body(df.to_dict("records"))

#guardar el pdf
pdf.output("listado_personas.pdf")
