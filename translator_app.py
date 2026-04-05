import customtkinter as ctk
from deep_translator import GoogleTranslator
import pyperclip

# إعدادات شكل البرنامج
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة
        self.title("V!X AI Translator")
        self.geometry("700x500")

        # العنوان
        self.label = ctk.CTkLabel(self, text="AI Language Translator", font=("Arial", 26, "bold"))
        self.label.pack(pady=20)

        # قائمة اختيار اللغة اللي هنترجم ليها
        self.languages = {'Arabic': 'ar', 'English': 'en', 'French': 'fr', 'German': 'de', 'Spanish': 'es'}
        self.lang_menu = ctk.CTkOptionMenu(self, values=list(self.languages.keys()))
        self.lang_menu.set("Arabic")
        self.lang_menu.pack(pady=10)

        # صندوق إدخال النص
        self.input_text = ctk.CTkTextbox(self, width=600, height=100)
        self.input_text.insert("0.0", "Enter text here...")
        self.input_text.pack(pady=10)

        # زرار التشغيل
        self.btn_translate = ctk.CTkButton(self, text="Translate ✨", command=self.translate_logic)
        self.btn_translate.pack(pady=20)

        # صندوق النتيجة
        self.output_text = ctk.CTkTextbox(self, width=600, height=100, state="disabled")
        self.output_text.pack(pady=10)

        # زرار النسخ
        self.btn_copy = ctk.CTkButton(self, text="Copy Result", command=self.copy_text, fg_color="transparent", border_width=2)
        self.btn_copy.pack(pady=10)

    def translate_logic(self):
        text_to_translate = self.input_text.get("1.0", "end-1c")
        target_lang = self.languages[self.lang_menu.get()]
        
        if text_to_translate.strip():
            # عملية الترجمة
            translated = GoogleTranslator(source='auto', target=target_lang).translate(text_to_translate)
            
            # عرض النتيجة
            self.output_text.configure(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated)
            self.output_text.configure(state="disabled")

    def copy_text(self):
        content = self.output_text.get("1.0", "end-1c")
        if content:
            pyperclip.copy(content)
            self.btn_copy.configure(text="Copied! ✅")
            self.after(2000, lambda: self.btn_copy.configure(text="Copy Result"))

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()