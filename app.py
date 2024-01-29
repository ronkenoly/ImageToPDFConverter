import tkinter as tk 
#provides dialogs for opening and saving files
from tkinter import filedialog
#aloows you to create pdf and draw various images,shapes and texts
from reportlab.pdfgen.canvas import canvas
#provides a variety of imaging  capabilities
from PIL import Image
import os
#a method is a function within a class and operates within it
#self is a convention word to access instance of a class(object),method of a class
class ImageToPDFConverter:
    def __init__(self, root):
        self.root =root
        self.image_paths = []
        #creates a a special type of variable that can be linked to one or more widgets to automatically update
        #their values whenever variable changes
        self.output_pdf_name = tk.StringVar()
        #listbox is a widget that displays a list of options from which the user can select one or more items
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

        def initialize_ui(self):
            title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
            #pck method is used to organize widgets in the root window
            title_label.pack(pady=10)
            # command paramater specifies the selectimage method to be called
            select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
            select_images_button.pack(pady=(0, 10))
            #packs a listbox widget
            self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)
            # creates a  label widget
            label = tk.Label(self.root, text="Enter output PDF name:")
            label.pack()
            #textvariable links the entry widget to the stringvar
            pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify="centre")
            pdf_name_entry.pack()
           #the command shows that convertimage topdf function to be called
            convert_button =tk.Button(self.root, text="Convert to PDF". command=self.convert_images_to_pdf)
            convert_button.pack(pady=(20,40))

           
        
        def select_images(self):
            #opens a file dialog using the askopenfilenames method called from the filedialog module
            self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=
            [("Image files", "*.png;*.jpg;*.jpeg")])
            self.update_selected_images_listbox()

        def update_selected_images_listbox(self):
            self.selected_images_listbox.delete(0, tk.END)

            for image_path in self.image_paths:
                _, image_path = os.path.split(image_path)
                self.selected_images_listbox.insert(tk.END, image_path)
                
        def convert_images_to_pdf(self):
            if not self.image_paths:
                return

            self.output_pdf_path = self.output_pdf_name.get() + "pdf" if self.output_pdf_name.get()else "output.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))

        for image_path in self.image_paths:
            img = Image.open(image_path)
            availabel_width = 540
            availabel_height = 720
            scale_factor = min(availabel_width / img.width, availabel_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            pdf.setFillColor(255, 255, 255) 
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInLineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

            pdf.save()   


        def main():
            root = tk.Tk()
            root.title("Image to PDF")
            converter = ImageToPDFConverter(root)
            root.geometry("400*600")
            root.mainloop()


            if__name__ == "__main__":  main()                     