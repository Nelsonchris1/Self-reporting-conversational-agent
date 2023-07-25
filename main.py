import streamlit as st
import streamlit.components.v1 as com
from streamlit_extras.switch_page_button import switch_page


def main():
    
    st.set_page_config(page_title="Streamlit Web App", initial_sidebar_state="collapsed", layout="wide")
    st.markdown("""
       
        """,
        unsafe_allow_html=True)
    st.markdown( """  <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style> [data-testid="collapsedControl"] { display: none } </style>
                  </head> """, 
                unsafe_allow_html=True)
    

    with open("style2.css") as s:
        st.markdown(f"""<style>
                    {s.read()}</style>""", unsafe_allow_html=True)
        
    

    # Render H1 tag at the center of the page
    st.markdown(
        """
         <div class="hero">
            <div class="content-container">
                <h1>Welcome to the <span class="app-name">MentBot</span></h1>
                <p>Here to help you navigate your mental well-being</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )


   
    col1, col2, col3 , col4, col5= st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        center_button = st.button('Get started')
    if center_button:
        switch_page("chat")


    st.markdown(
        """
            <div id="quotes">
            <h2>Reflections</h2>
            <div class="quote">
                <p>"What mental health needs is more sunlight, more candor and more unashamed conversation"</blockquote>
                <cite>- Glenn Close </cite>
            </div>
            <div class="quote">
                <p>"The greatest glory in living lies not in never falling, but in rising every time we fall"</blockquote>
                <cite>- Nelson Mandela </cite>
          </div>
          </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div id="stories">
            <div class="story">
                <h3>It's Assessible.</h3>
                <p>All you need is internet and you can access this from anywhere in the world</p>
            </div>
            <div class="story">
                <h3>It's Affordable.</h3>
                <p>It is completely free, you dont need to pay any upfront fee to be heard</p>
            </div>
            <div class="story">
                <h3>It's Effective.</h3>
                <p>Thousands of people have benefitted from therapy</p>
            </div>
            <div class="story">
                <h3>It's Annonymous.</h3>
                <p>We wont ask for your name, location, age e.t.c . We do not require these information to listen to you/p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

# Things to add next is to test the different prompts, and also start writing. 
