# Data Kvalitet & Kunskapskontroll - Harry Potter RAG Application

Detta projekt är en RAG-applikation (Retrieval-Augmented Generation) byggd i Jupyter Notebook samt ett gränssnitt med Streamlit. Applikationen laddar och strukturerar textdata från csv-filer med Harry Potter data samt böckerna i textformat, lagrar dem i en vektordatabas med verifierbar metadata, och chattgränssnitt används för att ställa frågor baserat på dokumenten.
*Viktigt* att poängtera att böckerna samt vektordatabasen finns inte med i detta repository på grund av att vi inte vill riskera bryta mot copyrightlagar. Om du vill använda koden till egetbruk krävs det att du hämta böckerna på egen hand. 

Streamlit koden är byggd på att notebooken är körd och en databas är skapad med embeddings.  

## 📁 Projektstruktur

* **data/** – Innehåller rådata och källmaterial; alltså csv filerna både dem städade och orginal filerna.
* **rag/** – Moduler för vektorladdning, embeddings och söklogik.
* **data_cleaning_2.ipynb** – Jupyter Notebook för preprocessing och rensning av textdata.
* **hp_rag_txt_final_v2.ipynb** – Experimentering och validering av RAG-pipelinen.
* **hp_streamlit_rag.py** – Huvudapplikationen för Streamlit-gränssnittet.
* **requirements.txt** – Lista över projektets Python-dependencies.

## 🚀 Kom igång

### 1. Klona repot och installera beroenden
Säkerställ att du har installerat alla nödvändiga bibliotek innan du startar applikationen:

```bash
pip install -r requirements.txt
```
### **2. Ladda ner Harry Potter-böckerna**
Hämta böckerna från t.ex. Kaggle och lägg in dem i data-mappen. 
