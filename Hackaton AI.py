#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install Pillow')


# In[2]:


from PIL import Image


# In[321]:


get_ipython().system('pip install easygui')


# In[3]:


import easygui


# In[4]:


imgpath = easygui.fileopenbox()
print(imgpath)


# In[5]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
mytext = pytesseract.image_to_string(Image.open(imgpath))
mytext


# In[66]:


get_ipython().system('pip install pyttsx3')


# In[6]:


import pyttsx3


# In[35]:


get_ipython().system('pip install googletrans')


# In[7]:


from googletrans import Translator


# In[8]:


translator = Translator()


# In[9]:


translatedtext = translator.translate(mytext)


# In[10]:


detlang = translatedtext.src
result = detlang
print(detlang)


# In[15]:


reqddest = input()


# In[16]:


translatedtext = translator.translate(mytext,dest=reqddest)


# In[17]:


engine = pyttsx3.init()


# In[18]:


engine.say(translatedtext)
engine.runAndWait()


# In[ ]:




