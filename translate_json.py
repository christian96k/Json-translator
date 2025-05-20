import json
import argparse
import re
from deep_translator import GoogleTranslator

#region placeholder utils
def extract_placeholders(text):
    """
    Trova placeholder comuni i18n e restituisce un mapping di sostituzione temporaneo.
    """
    pattern = re.compile(r"{{\s*[^}]+\s*}}|%\w|{\d+}")
    placeholders = pattern.findall(text)
    mapping = {}
    for i, ph in enumerate(placeholders):
        token = f"__PH_{i}__"
        mapping[token] = ph
    for token, ph in mapping.items():
        text = text.replace(ph, token)
    return text, mapping

def restore_placeholders(text, mapping):
    """
    Ripristina i placeholder originali nei punti corretti.
    """
    for token, ph in mapping.items():
        text = text.replace(token, ph)
    return text
#endregion

#region translation json
def translate_json(input_file, output_file, target_lang="en"):
    """Traduci i valori di un JSON mantenendo la struttura, proteggendo i placeholder."""
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    translator = GoogleTranslator(source="auto", target=target_lang)

    def translate_values(d, path=""):
        if isinstance(d, dict):
            return {key: translate_values(value, f"{path}.{key}") for key, value in d.items()}
        elif isinstance(d, list):
            return [translate_values(item, f"{path}[{i}]") for i, item in enumerate(d)]
        elif isinstance(d, str):
            print(f"🔄 Translating: {path} → {d}")
            safe_text, placeholders = extract_placeholders(d)
            translated_text = translator.translate(safe_text)
            restored_text = restore_placeholders(translated_text, placeholders)
            print(f"✅ Translated: {path} → {restored_text}")
            return restored_text
        return d

    translated_data = translate_values(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Translation completed! File saved as {output_file}")
#endregion

#region terminal arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traduci un file JSON in un'altra lingua.")
    parser.add_argument("input_file", help="Il file JSON di input (es: en.json)")
    parser.add_argument("output_file", help="Il file JSON di output (es: es.json)")
    parser.add_argument("language", help="Codice lingua di destinazione (es: 'es' per spagnolo)")

    args = parser.parse_args()
    translate_json(args.input_file, args.output_file, args.language)
#endregion
