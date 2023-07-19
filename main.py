import streamlit as st
import streamlit.components.v1 as com
from streamlit_extras.switch_page_button import switch_page


def main():
    st.set_page_config(page_title="Streamlit Web App", initial_sidebar_state="collapsed")
    st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, 
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
        switch_page("trial")


    st.markdown(
        """
            <div id="quotes">
            <h2>Reflections</h2>
            <div class="quote">
                <blockquote>"What mental health needs is more sunlight, more candor and more unashamed conversation"</blockquote>
                <cite>- Glenn Close </cite>
            </div>
            <div class="quote">
                <blockquote>"The greatest glory in living lies not in never falling, but in rising every time we fall"</blockquote>
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
                <p>All therapists are licensed, accredited professionals. BetterHelp allows you to connect with them in a safe and convenient online environment.</p>
            </div>
            <div class="story">
                <h3>It's Affordable.</h3>
                <p>Pay a low flat fee for both live sessions as well as messaging with your therapist. Therapy doesn't have to be expensive.</p>
            </div>
            <div class="story">
                <h3>It's Effective.</h3>
                <p>Thousands of people have benefitted from therapy (just check out their reviews!) With BetterHelp, you can switch therapists at any point if you don't feel you are getting enough benefit.</p>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

# Things to add next is to test the different prompts, and also start writing. 
