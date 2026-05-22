# Data Kvalitet & Kunskapskontroll - Harry Potter RAG Application

Detta projekt är en RAG-applikation (Retrieval-Augmented Generation) byggd i Python och Streamlit. Applikationen laddar och strukturerar textdata från Harry Potter-dokument, lagrar dem i en vektordatabas med verifierbar metadata, och erbjuder ett chattgränssnitt för att ställa frågor baserat på dokumenten.

## 📁 Projektstruktur

* **data/** – Innehåller rådata och källmaterial.
* **rag/** – Moduler för vektorladdning, embeddings och söklogik.
* **data_cleaning.ipynb** – Jupyter Notebook för preprocessing och rensning av textdata.
* **hp_rag_txt_final_v2.ipynb** – Experimentering och validering av RAG-pipelinen.
* **hp_streamlit_rag.py** – Huvudapplikationen för Streamlit-gränssnittet.
* **requirments.txt** – Lista över projektets Python-dependencies.

## 🚀 Kom igång

### 1. Klona repot och installera beroenden
Säkerställ att du har installerat alla nödvändiga bibliotek innan du startar applikationen:

```bash
pip install -r requirments.txt
