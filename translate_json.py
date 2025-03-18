import json
import argparse
from deep_translator import GoogleTranslator

#region translation json
def translate_json(input_file, output_file, target_lang="en"):
    """Default language is (en) English."""
    """Translate JSON's values, maintaining the keys structure."""
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
            translated_text = translator.translate(d)
            print(f"✅ Translated: {path} → {translated_text}")
            return translated_text
        return d

    translated_data = translate_values(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 Translation completed! File saved as {output_file}")
#endregion translation json

#region terminal arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traduci un file JSON in un'altra lingua.")
    parser.add_argument("input_file", help="Il file JSON di input (es: en.json)")
    parser.add_argument("output_file", help="Il file JSON di output (es: es.json)")
    parser.add_argument("language", help="Codice lingua di destinazione (es: 'es' per spagnolo)")

    args = parser.parse_args()
    translate_json(args.input_file, args.output_file, args.language)
#endregion terminal arguments
