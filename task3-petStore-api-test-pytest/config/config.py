import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class APIConfig:
    """API configuration settings."""
    base_url: str
    timeout: int = 30
    verify_ssl: bool = True

@dataclass
class Config:
    """Global configuration settings."""
    api: APIConfig
    environment: str

def get_config() -> Config:
    """
    Get configuration based on environment.
    
    Returns:
        Config object with all settings
    """
    env = os.getenv("TEST_ENV", "local")
    
    # Configuration for different environments
    configs = {
        "local": Config(
            api=APIConfig(
                base_url="http://localhost:8080/api/v3",
            ),
            environment="local"
        ),
        "dev": Config(
            api=APIConfig(
                base_url="https://dev-petstore.swagger.io/api/v3",
            ),
            environment="dev"
        ),
        "staging": Config(
            api=APIConfig(
                base_url="https://staging-petstore.swagger.io/api/v3",
            ),
            environment="staging"
        )
    }
    
    return configs.get(env, configs["local"])

# Global config instance
config = get_config()
