import pyttsx3
import PyPDF2

book = open('mybook.pdf','rb') # Add path
pdf_reader = PyPDF2.PdfReader(book)
num_pages = len(pdf_reader.pages)
play = pyttsx3.init()
print('Playing Audio Book')

for num in range(0, num_pages): #iterating through all pages
    page = pdf_reader.pages[num]
    data = page.extract_text()  #extracting text

    play.say(data)
    play.runAndWait()

    # Coded with 💙 by Mr. Unity Buddy
