from typing import List
from langchain_ollama import ChatOllama

def generate_search_queries(location: str) -> List[str]:
    """Generates detailed and optimized search queries for students based on location."""
    
    base_queries = [
        f"Top-ranked universities in {location} for international and domestic students",
        f"Cost of studying in {location}: tuition, housing, food, and other expenses",
        f"Best universities in {location} with scholarships and financial aid options",
        f"Affordable student housing and dormitory options in {location}",
        f"Public transportation guide for students in {location}: buses, trains, metro, and passes",
        f"Campus safety and student security in universities of {location}",
        f"Internship and job opportunities for students in {location}",
        f"Student life in {location}: culture, social events, and networking opportunities",
        f"Best libraries, study spaces, and coworking spaces for students in {location}",
        f"University rankings in {location} based on academic performance and student reviews",
        f"Best universities in {location} for STEM, business, arts, and humanities",
        f"Visa requirements and work opportunities for international students in {location}",
        f"Top student discounts in {location} for food, travel, and entertainment",
        f"Best places to eat, relax, and explore for students in {location}",
        f"Comparison of public and private universities in {location}: pros and cons"
    ]

    return base_queries


def analyze_and_summarize(text: str, llm_model: str = "mistral:latest"):  # ✅ Changed "mistral" to "gemma"
    """Analyzes and summarizes the given text using LLM."""
    llm = ChatOllama(model=llm_model, temperature=0)

    prompt = f"""
    Please analyze and summarize the following information:
    {text}
    
    Focus on key points about:
    - University information
    - Cost details
    - Location specifics
    - Student life
    """

    result = llm.invoke(prompt)  # ✅ Fixed incorrect invocation
    return result.content
