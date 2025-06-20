#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install googletrans==4.0.0-rc1')


# In[2]:


from deep_translator import GoogleTranslator
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko"
}
def translate_multiple_languages(text):
    print(f"\nOriginal Text: {text}\n")
    for lang_name, lang_code in languages.items():
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
            print(f"{lang_name:>10}: {translated}")
        except Exception as e:
            print(f"{lang_name:>10}: [Error] {e}")
input_text = input("Enter the text you want to translate: ")
translate_multiple_languages(input_text)


# In[ ]:




