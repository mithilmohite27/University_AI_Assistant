import os
from dotenv import load_dotenv
from search_api_utils import tavily_search
from query_generation import generate_search_queries, analyze_and_summarize
from updated_agent import graph
from models import UniversitySearchState
from configuration import Configuration

# Load environment variables
load_dotenv()

def run_tests():
    # Test if environment variables are loaded correctly
    print("🔍 Testing API Keys...")
    assert os.getenv("TAVILY_API_KEY"), "❌ ERROR: TAVILY_API_KEY not found in .env"
    print("✅ Environment Variables Loaded!")

    # Test Tavily API Connection
    print("\n🔍 Testing Tavily API Search...")
    try:
        response = tavily_search("best universities in USA", max_results=1)
        assert "results" in response, "❌ ERROR: Tavily API response invalid!"
        print("✅ Tavily API Working!")
    except Exception as e:
        print(f"❌ Tavily API Error: {e}")
        raise

    # Test Query Generation
    print("\n🔍 Testing Query Generation...")
    try:
        queries = generate_search_queries("Ahmedabad")
        print(f"✅ Generated Queries: {queries}")
    except Exception as e:
        print(f"❌ Query Generation Error: {e}")
        raise

    # Test University Search Workflow
    print("\n🔍 Testing University Search Workflow...")
    try:
        state = UniversitySearchState(location="Ahmedabad")
        config = Configuration()
        config_dict = {"configurable": config.to_dict()}
        
        print("Starting graph execution...")
        output = graph.invoke(state, config=config_dict)
        print(f"Graph execution completed. Output keys: {output.keys() if output else 'No output'}")
        
        assert output is not None, "❌ ERROR: No output from graph"
        assert "running_summary" in output, "❌ ERROR: University search failed!"
        print("✅ University Search Completed Successfully!")
        
        return output
    except Exception as e:
        print(f"❌ University Search Error: {e}")
        raise

if __name__ == "__main__":
    try:
        output = run_tests()
        print("\n🎉 ALL TESTS PASSED! PROJECT IS WORKING PERFECTLY! 🎉")
        print("\nFinal Summary:")
        print(output.get("running_summary", "No summary available"))
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")