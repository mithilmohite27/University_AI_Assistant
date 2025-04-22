from dataclasses import dataclass, fields, asdict
import os
from typing import Any, Optional, Dict
from langchain_core.runnables import RunnableConfig

@dataclass(kw_only=True)
class Configuration:
    """Configuration settings for the AI research assistant."""
    max_web_research_loops: int = 3
    local_llm: str = "mistral:latest"  # Default to "mistral:latest"

    def items(self) -> Dict[str, Any]:
        """Make the configuration dict-like for compatibility."""
        return asdict(self).items()

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        configurable = getattr(config, "configurable", {}) if config else {}
        values = {
            f.name: os.getenv(f.name.upper(), configurable.get(f.name, getattr(cls, f.name)))
            for f in fields(cls) if f.init
        }
        
        valid_llms = ["llama2", "mistral:latest", "codellama", "qwen2.5:7b"]  # Ensure valid models
        selected_llm = values.get("local_llm", "mistral:latest")  # Fetch selected model

        if selected_llm not in valid_llms:
            raise ValueError(f"Invalid LLM specified: {selected_llm}")  # Proper validation
        
        return cls(**values)

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return asdict(self)
