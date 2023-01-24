import datetime
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from API.api_key import *
labels = ["Fecha", "Nombre del producto", "Cantidad (unidad)", "Precio(B/.)"]
data = [labels]
current_date = datetime.datetime.now()

Productos = {"AIRJ" : {"Nombre":"Air Jordan 1 - Red", "Precio Unitario": 110.00}}

def generate_invoice(message):
    # Get user input for product code and quantity
    product_code = Productos["AIRJ"]
    quantity = int(1)

    #lookup product and calculate subtotal
    product = Productos[product_code]
    subtotal = quantity * product["Precio Unitario"]

    # add product and quantity to data list
    data.append([current_date.date(), product["Nombre"], quantity, "$ {:,.2f}".format(product["Precio Unitario"])])

    data.append(["Subtotal","","","$ {:,.2f}".format(subtotal)])
    total = subtotal * 0.7
    data.append(["total","","","$ {:,.2f}".format(total)])

    # create invoice pdf template
    invoice_pdf = SimpleDocTemplate("recibo_compra.pdf", pagesize = A4)
    # use default reportlab style
    styles = getSampleStyleSheet()

    # style and positioning for title
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph("Unnamed Store", title_style)

    # style for table
    style = TableStyle(
        [
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
            ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.black ),
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige),
        ]
    )

    # create table with data and style
    receipt = Table(data, style = style)

    # build pdf with title and table
    invoice_pdf.build([title, receipt])
    chat_bot_key.send_document(chat_id=message.chat.id, document=open('recibo_compra.pdf', 'rb'))

