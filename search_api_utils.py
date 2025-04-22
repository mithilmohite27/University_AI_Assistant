import os
from typing import Dict, Any, List
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def tavily_search(query: str, include_raw_content: bool = True, max_results: int = 3) -> Dict[str, Any]:
    """Executes a web search using the Tavily API."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY is missing from environment variables.")
    
    tavily_client = TavilyClient(api_key=api_key)
    return tavily_client.search(query, max_results=max_results, include_raw_content=include_raw_content)

def deduplicate_and_format_sources(sources: Dict[str, Any], max_tokens_per_source: int = 1000, include_raw_content: bool = True) -> List[Dict[str, str]]:
    """Deduplicates and formats search results."""
    if not sources or 'results' not in sources:
        return []
    
    formatted_sources = []
    seen_urls = set()
    
    for result in sources['results']:
        url = result.get('url', '')
        if url not in seen_urls:
            seen_urls.add(url)
            formatted_source = {
                'url': url,
                'title': result.get('title', ''),
                'content': result.get('content', '') if include_raw_content else ''
            }
            formatted_sources.append(formatted_source)
            
    return formatted_sources

def format_sources(sources: Dict[str, Any]) -> str:
    """Formats sources into a readable string."""
    if not sources or 'results' not in sources:
        return "No sources available"
    
    formatted = []
    for idx, result in enumerate(sources['results'], 1):
        formatted.append(f"{idx}. {result.get('title', 'No title')} - {result.get('url', 'No URL')}")
    
    return "\n".join(formatted)