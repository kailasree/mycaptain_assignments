file_extensions = {
    ".py":"Python",
    ".docx":"Microsoft word",
    ".pdf":"PDF",
    
    }

file=input("Enter filename")

if ".py" in file:
    print("filename " + file + " is the extension of Python")
elif ".docx" in file:
    print("filename " + file + " is the extension of Microsoft word")
elif ".pdf" in file:
    print("filename " + file + " is the extension of pdf")
else:
    print("file extension does not exist")