from typing_extensions import Literal
from langchain_ollama import ChatOllama
from langgraph.graph import START, END, StateGraph
from configuration import Configuration
from search_api_utils import deduplicate_and_format_sources, tavily_search, format_sources
from models import UniversitySearchState
from query_generation import analyze_and_summarize

def web_research(state: UniversitySearchState, config: Configuration):
    """Web research function using Tavily API."""
    print("\n🔍 Starting web research...")
    try:
        search_results = tavily_search(state.location, include_raw_content=True, max_results=3)
        print("✅ Tavily search completed")
        
        formatted_results = deduplicate_and_format_sources(search_results, max_tokens_per_source=1000, include_raw_content=True)
        print(f"✅ Found {len(formatted_results)} formatted results")
        
        sources = format_sources(search_results)
        print("✅ Sources formatted")
        
        return {
            "sources_gathered": [sources],
            "research_loop_count": state.research_loop_count + 1,
            "web_research_results": [formatted_results]
        }
    except Exception as e:
        print(f"❌ Error in web research: {str(e)}")
        raise

def summarize_sources(state: UniversitySearchState, config: Configuration):
    """Summarization function using LLM."""
    print("\n📝 Starting source summarization...")
    
    if not state.web_research_results:
        print("❌ No web research results found")
        return {"running_summary": "No data available to summarize."}
    
    try:
        configurable = Configuration.from_runnable_config(config)
        
        # Prepare the text to summarize
        text_to_summarize = (
            f"Location: {state.location}\n"
            f"Previous summary: {state.running_summary or 'None'}\n"
            f"New information: {state.web_research_results[-1]}"
        )
        
        current_summary = analyze_and_summarize(text_to_summarize, configurable.local_llm)
        print("✅ Summary generated")
        
        return {"running_summary": current_summary}
    except Exception as e:
        print(f"❌ Error in summarization: {str(e)}")
        raise

def route_research(state: UniversitySearchState, config: Configuration) -> Literal["finalize_summary", "web_research"]:
    """Route the research based on the follow-up query."""
    print(f"\n🔄 Current research loop: {state.research_loop_count}")
    configurable = Configuration.from_runnable_config(config)
    
    if state.research_loop_count <= configurable.max_web_research_loops:
        print("➡️ Routing to web_research")
        return "web_research"
    else:
        print("➡️ Routing to finalize_summary")
        return "finalize_summary"

def finalize_summary(state: UniversitySearchState):
    """Finalize the summary."""
    print("\n📊 Finalizing summary...")
    try:
        all_sources = "\n".join(state.sources_gathered)
        final_summary = f"## Summary\n\n{state.running_summary}\n\n### Sources:\n{all_sources}"
        print("✅ Summary finalized")
        return {"running_summary": final_summary}
    except Exception as e:
        print(f"❌ Error in finalizing summary: {str(e)}")
        raise

# Initialize the graph
print("\n🔧 Initializing state graph...")
builder = StateGraph(UniversitySearchState)

# Add nodes
builder.add_node("web_research", web_research)
builder.add_node("summarize_sources", summarize_sources)
builder.add_node("finalize_summary", finalize_summary)

# Add edges
builder.add_conditional_edges(
    "summarize_sources",
    route_research,
    {
        "web_research": "web_research",
        "finalize_summary": "finalize_summary"
    }
)
builder.add_edge("web_research", "summarize_sources")
builder.add_edge("finalize_summary", END)
builder.add_edge(START, "web_research")

# Compile the graph
graph = builder.compile()
print("✅ Graph compiled successfully")