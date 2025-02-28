#https://python.langchain.com/docs/how_to/document_loader_pdf/

from langchain_community.document_loaders import PyPDFLoader

def test():
    file_path = (
        "./doc/Large-scale cluster management at Google with Borg.pdf"
    )
    loader = PyPDFLoader(file_path)
    pages = []
    for page in loader.load():
        pages.append(page)
        
    print(f">> METADATA: {pages[0].metadata}\n")
    input()

    i = 1
    for page in pages:
        print(page.page_content)
        i += 1
        input()
    
def load(file_path):
    loader = PyPDFLoader(file_path)
    pages = []
    for page in loader.load():
        pages.append(page)
    return pages