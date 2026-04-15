from dotenv import load_dotenv
import os
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate



mistral_key = os.getenv("MISTRAL_API_KEY")
if not mistral_key:
    raise RuntimeError("MISTRAL_API_KEY is required in environment")

model_initiate = ChatMistralAI(
    model="mistral-small-latest",
    api_key=mistral_key,
    temperature=0.2,   
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert movie analyst.

Your task is to analyze the movie and provide a structured response.
Keep the response clean, detailed, and easy to understand.
"""
        ),
        (
            "human",
            """
Movie Name: {movie_name}
Summary Type: {summary_type}

The summary type can be:
- short
- detailed
- spoiler-free
- full-spoiler

Provide the response in the following format:

1. Movie Title
2. Release Year
3. Genre
4. Director
5. Main Cast
6. Language
7. Runtime
8. IMDb Rating
9. Short Story Summary
10. Main Characters and Their Roles
11. Key Themes of the Movie
12. Most Important Plot Points
13. Ending Explanation
14. Overall Mood of the Movie
15. Similar Movies Recommendation
16. Famous Dialogue or Tagline
17. Is the Movie Family Friendly?
18. Final Verdict
"""
        )
    ]
)

movie_name  = input("Enter the movie name: ")
summary_type = input("Enter the summary type (short, detailed, spoiler-free, full-spoiler): ")

final_prompt = prompt.invoke(
    {
        "movie_name": movie_name,
        "summary_type": summary_type
    }
)

response = model_initiate.invoke(final_prompt)
print(response.content)
