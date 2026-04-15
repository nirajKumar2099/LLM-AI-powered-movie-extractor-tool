
import streamlit as st
from dotenv import load_dotenv
import os


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel # for structured response validation (optional) : json schema validation can also be used if preferred
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser # for parsing model response into pydantic model (optional)

# Load environment variables
load_dotenv()

# for structor response in json fomrat using pydantic model (optional)
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: str
    director: Optional[str] = None
    main_cast: List[str]
    imdb_rating: Optional[float] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# Get API Key
mistral_key = os.getenv("MISTRAL_API_KEY")

if not mistral_key:
    st.error("MISTRAL_API_KEY is missing in .env file")
    st.stop()

# Model Initialization
model_initiate = ChatMistralAI(
    model="mistral-small-latest",
    api_key=mistral_key,
    temperature=0.2,
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert movie analyst.
            {format_instructions}
            """
        ),
        "human",
        """
        Movie Name: {movie_name},
        Summary Type: {summary_type}
        The summary type can be:
        - short
        - detailed
        - spoiler-free
        - full-spoiler
        """
    ]
)

# Streamlit Page Config
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #ff4b4b;
        margin-bottom: 10px;
    }

    .sub-title {
        font-size: 18px;
        text-align: center;
        color: #b0b0b0;
        margin-bottom: 30px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="main-title">🎬 Movie Information Extractor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Get complete movie details, cast, genre, themes, ending explanation and recommendations.</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Movie Input")

    movie_name = st.text_input("Enter Movie Name")

    summary_type = st.selectbox(
        "Select Summary Type",
        ["short", "detailed", "spoiler-free", "full-spoiler"]
    )

    generate_btn = st.button("Generate Movie Information")

with col2:
    st.subheader("Movie Analysis")

    if generate_btn:
        if not movie_name:
            st.warning("Please enter a movie name.")
        else:
            with st.spinner("Fetching movie information..."):
                final_prompt = prompt.invoke(
                    {
                        "movie_name": movie_name,
                        "summary_type": summary_type,
                        "format_instructions": parser.get_format_instructions()
                    }
                )

                response = model_initiate.invoke(final_prompt)

                st.success("Movie information generated successfully.")
                st.markdown(response.content)


