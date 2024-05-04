
comandoLista = "scevtls -d postgresql:// --begin 01-01-2024 00:00:00 > lista_de_eventos.txt"
#subprocess.call(comandoLista, shell=True)
texto_busqueda = "Funvisis2024ewaxs"
 

with open("lista_de_eventosAdrianPrueba.txt", "r") as archivo:
    lineas = archivo.readlines()
        
    for linea in lineas:
        if texto_busqueda in linea:
            print(linea.strip())
                #comandoXml = "scxmldump -d postgresql:// -E " + linea.strip() + " -PAMF -o ultimo_id_evento.xml"
                #subprocess.call(comandoXml,shell=True)
                #comandoBoletin = "scbulletin -i /home/ndcuser/adrian/ReporteAutomatico/ultimo_id_evento.xml > /home/ndcuser/adrian/ReporteAutomatico/bulletin_ultimo_evento.txt"
                #subprocess.call(comandoBoletin,shell=True)
                # subprocess.call([python_path, 'leer.py'])
                # self.ui.stackedWidget_izq.setCurrentIndex(1)
                # image_widget = create_image_widget("./muestra.png",400,500)
                # self.ui.stackedWidget_der.insertWidget(1, image_widget)
                # self.ui.stackedWidget_der.setCurrentIndex(1)