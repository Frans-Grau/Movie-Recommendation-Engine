### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import SnowballStemmer
from string import punctuation
from wordcloud import WordCloud
import pickle
from PIL import Image
import requests
import streamlit_nested_layout

###Import Data
reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")

### Define columns:
st.set_page_config(page_title=None, page_icon="🎥", layout="wide", menu_items=None)

tab1, tab2, tab3 = st.tabs(["Inov Movie", "Recomendations", "Top Movies"])

with tab1:
    
   st.header("Inov Movie")
   st.image(image4, width=1000) 
    
with tab2:    
outer_cols = st.columns([2,0.5,2])

### Left side of screen
with outer_cols[0]:
    st.markdown('## Movie')
    title = st.text_input('Type the title and press Enter')
    if title:
            try: 
                url = f"https://www.omdbapi.com/?t={title}&apikey=38187759"
                re = requests.get(url)
                re = re.json()

                inner_cols = st.columns([1,2])
                with inner_cols[0]:
                    st.image(re['Poster'])

                with inner_cols[1]:
                    st.subheader(re['Title'])
                    st.caption(f"Gender:{re['Genre']} Year: {re['Year']} ")
                    st.write (re['Plot'])
                    st.text(f"Rating: {re['imdbRating']}")
                    st.progress(float(re['imdbRating'])/10)

                        ### Right side of screen    
                    with outer_cols[0]:
                        st.markdown('')
                        
                    with outer_cols[2]:
                        st.markdown('## Recommendations')
                        inner_cols = st.columns([1,2])
                        
                        with inner_cols[0]:
                            st.image(re['Poster'])
                        
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")
                            st.progress(float(re['imdbRating'])/10)
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.image(re['Poster'])
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")
                            st.progress(float(re['imdbRating'])/10)
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.image(re['Poster'], use_column_width='auto')
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")
                            st.progress(float(re['imdbRating'])/10)

            except:
                title = False
                st.markdown('''We currently don't have detailed information on this movie
                drop us an email and our scouting team will look into it and will send you our review''')
                contact_form = """
                <form action="https://formsubmit.co/inovmovie@gmail.com" method="POST">
                <input type="text" name="Suggestion" placeholder="Movie suggestion" required>
                <input type="text name="Name" placeholder="Your name" required>
                <button type="submit">Send</button>
                </form>
                """
                st.markdown (contact_form, unsafe_allow_html=True)
with tab3:
   st.header("Check the movies that everybody loves")
   col, col1, col2 = st.columns(3)
   col3, col4, col5 = st.columns(3)
   col6, col7, col8 = st.columns(3)
with col:
   st.video("https://www.youtube.com/watch?v=6hB3S9bIaco")
with col1:
   st.video("https://www.youtube.com/watch?v=sY1S34973zA")
with col2:
   st.video("https://www.youtube.com/watch?v=EXeTwQWrcwY")
with col3:    
   st.video("https://www.youtube.com/watch?v=r5X-hFf6Bwo")
with col4:
   st.video("https://www.youtube.com/watch?v=gG22XNhtnoY")
with col5:
   st.video("https://www.youtube.com/watch?v=OA1ij0alE0w")
with col6:
  st.video("https://www.youtube.com/watch?v=_13J_9B5jEk")
with col7: 
  st.video("https://www.youtube.com/watch?v=tGpTpVyI_OQ")
with col8:
  st.video("https://www.youtube.com/watch?v=8hP9D6kZseM")
