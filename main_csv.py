import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv

window = tk.Tk()
window.title("Apple Stock")
window.minsize(800, 400)

button_frame = Frame()
button_frame.pack(
    fill=tk.X,
    pady=20,
    padx=20,
)


def addProduct():
    add = Toplevel(window)
    add.resizable(False, False)
    add.title("Add Product")

    detailFrame = Frame(add)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )
    Label(detailFrame, text="ID").pack(side="left")

    IDEntry = Entry(detailFrame)
    IDEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(detailFrame, text="Name").pack(side="left")

    NameEntry = Entry(detailFrame)
    NameEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    OPTIONS = [
        "32 GB",
        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB",
        "2 TB",
    ]

    Label(detailFrame, text="Storage").pack(side="left")

    variable = StringVar(add)
    variable.set(OPTIONS[0])
    storage = OptionMenu(
        detailFrame,
        variable,
        *OPTIONS,
    ).pack(side="left")

    colorFrame = Frame(add)
    colorFrame.pack(
        fill=tk.X,
        pady=5,
        padx=20,
    )

    Label(colorFrame, text="Color").pack(side="left")
    ColorEntry = Entry(colorFrame)
    ColorEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(colorFrame, text="Price").pack(side="left")
    PriceEntry = Entry(colorFrame)
    PriceEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(colorFrame, text="Quantity").pack(side="left")
    QuantityEntry = Entry(colorFrame)
    QuantityEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    button = tk.Button(
        add,
        text="OK",
        height=3,
        command=lambda: [
            addProductToCsv(
                IDEntry.get(),
                NameEntry.get(),
                variable.get(),
                ColorEntry.get(),
                PriceEntry.get(),
                QuantityEntry.get(),
            ),
            add.destroy(),
        ],
    )
    button.pack(
        fill=tk.X,
        expand=True,
        pady=10,
        padx=20,
    )


def addProductToCsv(
    productID, productName, productStorage, productColor, productPrice, productQuantity
):
    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[0] == productID:
                # ID already exists, show notification and return
                show_notification("Product with ID already exists.")
                return

    with open(path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                productID,
                productName,
                productStorage,
                productColor,
                productPrice,
                productQuantity,
            ]
        )

    load_data()


def show_notification(message):
    notification = tk.Toplevel(window)
    notification.title("Notification")
    notification.geometry("300x100")
    Label(notification, text=message).pack(padx=20, pady=20)
    notification.after(2000, notification.destroy)


def removeProduct():
    remove = Toplevel(window)
    remove.resizable(False, False)
    remove.title("Remove Product")

    detailFrame = Frame(remove)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )
    Label(detailFrame, text="ID").pack(side="left")

    IDEntry = Entry(detailFrame)
    IDEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    button = tk.Button(
        remove,
        text="OK",
        height=3,
        command=lambda: [
            confirmDeletion(IDEntry.get()),
            remove.destroy(),
        ],
    )
    button.pack(
        fill=tk.X,
        expand=True,
        pady=10,
        padx=20,
    )


def confirmDeletion(productID):
    confirm = Toplevel(window)
    confirm.resizable(False, False)
    confirm.title("Confirm Deletion")

    detailFrame = Frame(confirm)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )

    with open("product.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == productID:
                Label(detailFrame, text=f"ID: {row[0]}").pack(side="left")
                Label(detailFrame, text=f"Name: {row[1]}").pack(side="left")
                Label(detailFrame, text=f"Storage: {row[2]}").pack(side="left")
                Label(detailFrame, text=f"Color: {row[3]}").pack(side="left")
                Label(detailFrame, text=f"Price: {row[4]}").pack(side="left")
                Label(detailFrame, text=f"Quantity: {row[5]}").pack(side="left")

    buttonFrame = Frame(confirm)
    buttonFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )

    confirm_button = tk.Button(
        buttonFrame,
        text="Confirm Deletion",
        height=3,
        command=lambda: [
            removeProductFromCsv(productID),
            confirm.destroy(),
        ],
    )
    confirm_button.pack(side="left", fill=tk.X, expand=True, padx=10)

    cancel_button = tk.Button(
        buttonFrame,
        text="Cancel",
        height=3,
        command=confirm.destroy,
    )
    cancel_button.pack(side="left", fill=tk.X, expand=True, padx=10)


def removeProductFromCsv(productID):
    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != productID:
                writer.writerow(row)

    load_data()


def editProduct():
    edit = Toplevel(window)
    edit.resizable(False, False)
    edit.title("Edit Product")

    detailFrame = Frame(edit)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )
    Label(detailFrame, text="ID").pack(side="left")

    IDEntry = Entry(detailFrame)
    IDEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(detailFrame, text="Name").pack(side="left")

    NameEntry = Entry(detailFrame)
    NameEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    OPTIONS = [
        "32 GB",
        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB",
        "2 TB",
    ]

    Label(detailFrame, text="Storage").pack(side="left")

    variable = StringVar(edit)
    variable.set(OPTIONS[0])
    storage = OptionMenu(
        detailFrame,
        variable,
        *OPTIONS,
    ).pack(side="left")

    colorFrame = Frame(edit)
    colorFrame.pack(
        fill=tk.X,
        pady=5,
        padx=20,
    )

    Label(colorFrame, text="Color").pack(side="left")
    ColorEntry = Entry(colorFrame)
    ColorEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(colorFrame, text="Price").pack(side="left")
    PriceEntry = Entry(colorFrame)
    PriceEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(colorFrame, text="Quantity").pack(side="left")
    QuantityEntry = Entry(colorFrame)
    QuantityEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    button = tk.Button(
        edit,
        text="OK",
        height=3,
        command=lambda: [
            editProductInCsv(
                IDEntry.get(),
                NameEntry.get(),
                variable.get(),
                ColorEntry.get(),
                PriceEntry.get(),
                QuantityEntry.get(),
            ),
            edit.destroy(),
        ],
    )
    button.pack(
        fill=tk.X,
        expand=True,
        pady=10,
        padx=20,
    )


def editProductInCsv(
    productID, productName, productStorage, productColor, productPrice, productQuantity
):
    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == productID:
                if productName.strip():
                    row[1] = productName
                if productStorage.strip():
                    row[2] = productStorage
                if productColor.strip():
                    row[3] = productColor
                if productPrice.strip():
                    row[4] = productPrice
                if productQuantity.strip():
                    row[5] = productQuantity
            writer.writerow(row)

    load_data()


def findProduct():
    find = Toplevel(window)
    find.resizable(False, False)
    find.title("Find Product")

    detailFrame = Frame(find)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )
    Label(detailFrame, text="Product Name").pack(side="left")

    NameEntry = Entry(detailFrame)
    NameEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(detailFrame, text="Product Code").pack(side="left")

    CodeEntry = Entry(detailFrame)
    CodeEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    button = tk.Button(
        find,
        text="Find",
        height=3,
        command=lambda: [
            findProductInCsv(NameEntry.get(), CodeEntry.get()),
            find.destroy(),
        ],
    )
    button.pack(
        fill=tk.X,
        expand=True,
        pady=10,
        padx=20,
    )


def findProductInCsv(productName, productCode):
    for widget in window.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()
    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    cols = rows[0]
    tree = ttk.Treeview(window, columns=cols, show="headings")

    for col_name in cols:
        tree.heading(col_name, text=col_name)
    tree.pack(expand=True, fill="y")

    for row in rows[1:]:
        if (productName.lower() in row[1].lower() or not productName) and (
            productCode.lower() in row[0].lower() or not productCode
        ):
            tree.insert("", tk.END, values=row)


def sellProduct():
    sell = Toplevel(window)
    sell.resizable(False, False)
    sell.title("Sell Product")

    detailFrame = Frame(sell)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )
    Label(detailFrame, text="ID").pack(side="left")

    IDEntry = Entry(detailFrame)
    IDEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    Label(detailFrame, text="Quantity").pack(side="left")

    QuantityEntry = Entry(detailFrame)
    QuantityEntry.pack(side="left", fill=tk.X, expand=True, padx=10)

    button = tk.Button(
        sell,
        text="OK",
        height=3,
        command=lambda: [
            confirmSale(IDEntry.get(), QuantityEntry.get()),
            sell.destroy(),
        ],
    )
    button.pack(
        fill=tk.X,
        expand=True,
        pady=10,
        padx=20,
    )


def confirmSale(productID, quantity):
    confirm = Toplevel(window)
    confirm.resizable(False, False)
    confirm.title("Confirm Sale")

    detailFrame = Frame(confirm)
    detailFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )

    with open("product.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == productID:
                Label(detailFrame, text=f"ID: {row[0]}").pack(side="left")
                Label(detailFrame, text=f"Name: {row[1]}").pack(side="left")
                Label(detailFrame, text=f"Storage: {row[2]}").pack(side="left")
                Label(detailFrame, text=f"Color: {row[3]}").pack(side="left")
                Label(detailFrame, text=f"Price: {row[4]}").pack(side="left")
                Label(detailFrame, text=f"Quantity: {row[5]}").pack(side="left")
                Label(detailFrame, text=f"Sale Quantity: {quantity}").pack(side="left")

    buttonFrame = Frame(confirm)
    buttonFrame.pack(
        fill=tk.X,
        pady=10,
        padx=20,
    )

    confirm_button = tk.Button(
        buttonFrame,
        text="Confirm Sale",
        height=3,
        command=lambda: [
            sellProductByID(productID, quantity),
            confirm.destroy(),
        ],
    )
    confirm_button.pack(side="left", fill=tk.X, expand=True, padx=10)

    cancel_button = tk.Button(
        buttonFrame,
        text="Cancel",
        height=3,
        command=confirm.destroy,
    )
    cancel_button.pack(side="left", fill=tk.X, expand=True, padx=10)


def sellProductByID(productID, quantity):
    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == productID:
                current_quantity = int(row[5])
                new_quantity = current_quantity - int(quantity)
                if new_quantity < 0:
                    return
                row[5] = str(new_quantity)
            writer.writerow(row)

    load_data()


def load_data():
    for widget in window.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    path = "product.csv"
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    cols = rows[0]
    tree = ttk.Treeview(window, columns=cols, show="headings")

    for col_name in cols:
        tree.heading(col_name, text=col_name)
    tree.pack(expand=True, fill="y")

    for row in rows[1:]:
        tree.insert("", tk.END, values=row)


buttons = [
    ("Sell", sellProduct),
    ("Add", addProduct),
    ("Remove", removeProduct),
    ("Find", findProduct),
    ("Edit", editProduct),
    ("Refresh", load_data),
]
for text, command in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        height=5,
    )
    button.pack(
        side="left",
        fill=tk.X,
        expand=True,
        padx=10,
    )


load_data()
window.mainloop()
