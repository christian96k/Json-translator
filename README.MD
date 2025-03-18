# JSON Translator

Questo è un progettino semplice che serve a creare traduzioni automatiche utilizzando la libreria `deep_translator` e importando `GoogleTranslator`.

## Requisiti

- Python 3.6 o superiore installato

## Utilizzo

Per utilizzare questo progetto, è necessario avere un file JSON da cui attingere. Segui questi passaggi:

1. Assicurati di avere Python installato nella versione compatibile.
2. Installa la libreria `deep_translator` se non l'hai già fatto:
    ```bash
    pip install deep-translator
    ```
3. Esegui lo script di traduzione con il seguente comando:
    ```bash
    python translate_json.py "file_da_cui_attingere.json" "nome_file_desiderato.json" "lingua_scelta_in_codice"
    ```

Esempio:
```bash
python translate_json.py "input.json" "output.json" "it"
```

Questo comando tradurrà il contenuto del file `input.json` e salverà il risultato tradotto nel file `output.json` in italiano.


## Importante
Evitare di includere nella repository i file json prodotti per consentirne l'utilizzo a tutti