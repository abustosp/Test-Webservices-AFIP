from zeep import Client
from tkinter.messagebox import showinfo

def dummy():

    client = Client("https://wswhomo.afip.gov.ar/wsfe/service.asmx?WSDL")

    dummy = client.service.FEDummy()

    showinfo("Respuesta", dummy)

if __name__ == '__main__':
    dummy()