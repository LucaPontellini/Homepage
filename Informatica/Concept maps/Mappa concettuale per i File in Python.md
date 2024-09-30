# File in Python
## File di testo
- Apertura: `open('file.txt', 'r')`
- Lettura: `f.read()`, `f.readline()`, `f.readlines()`
- Scrittura: `f.write(str)`, `f.writelines(list)`
- Chiusura: `f.close()`

## File binari
- Apertura: `open('file.bin', 'rb')` o `open('file.bin', 'wb')`
- Lettura: `f.read()`
- Scrittura: `f.write(bytes)`
- Chiusura: `f.close()`

## File CSV
- Apertura: `open('file.csv', 'r')`
- Lettura: `csv.reader(f)`
- Scrittura: `csv.writer(f).writerow(list)` o `csv.writer(f).writerows(list_of_lists)`
- Chiusura: `f.close()`

## File JSON
- Apertura: `open('file.json', 'r')`
- Lettura: `json.load(f)`
- Scrittura: `json.dump(dict, f)`
- Chiusura: `f.close()`

## File XML
- Apertura: `xml.etree.ElementTree.parse('file.xml')`
- Lettura: `tree.getroot()`
- Scrittura: `tree.write('file.xml')`

## File HTML
- Apertura: `open('file.html', 'r')`
- Lettura: `f.read()`
- Scrittura: `f.write(str)`
- Chiusura: `f.close()`

## File YAML
- Apertura: `open('file.yaml', 'r')`
- Lettura: `yaml.safe_load(f)`
- Scrittura: `yaml.safe_dump(dict, f)`
- Chiusura: `f.close()`

## File PDF
- Per lavorare con i file PDF, avrai bisogno della libreria specifica `PyPDF2`.
Questa libreria fornisce funzioni specifiche per leggere, scrivere e manipolare i file PDF.

## File DOCX
- Per i file DOCX, la libreria `python-docx` è necessaria. 
Questa libreria offre funzioni per leggere, scrivere e manipolare i file DOCX.

## File XLSX
- Per lavorare con i file XLSX, dovrai utilizzare la libreria `openpyxl`. 
Questa libreria fornisce funzioni specifiche per leggere, scrivere e manipolare i file XLSX.

## File PPTX
- Per i file PPTX, avrai bisogno della libreria `python-pptx`. 
Questa libreria offre funzioni per leggere, scrivere e manipolare i file PPTX