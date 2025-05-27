import logging
import requests
from requests import Response
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class BaseAPIClient:
    """Base class for API clients with enhanced error handling and logging."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
    
    def _build_url(self, endpoint: str) -> str:
        """Builds the full URL for the API request."""
        return f"{self.base_url}{endpoint}"
    
    def _log_request(self, method: str, url: str, **kwargs):
        """Log the API request details."""
        logger.info(f"Request: {method} {url}")
        if kwargs.get('json'):
            logger.info(f"Request body: {kwargs['json']}")
        if kwargs.get('params'):
            logger.info(f"Query params: {kwargs['params']}")
    
    def _log_response(self, response: Response):
        """Log the API response details."""
        logger.info(f"Response status: {response.status_code}")
        try:
            logger.info(f"Response body: {response.json()}")
        except ValueError:
            logger.info(f"Response text: {response.text}")
    
    def request(
        self, 
        method: str, 
        endpoint: str, 
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any
    ) -> Response:
        """
        Makes an HTTP request with enhanced logging and error handling.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint
            headers: Request headers
            **kwargs: Additional request parameters
        
        Returns:
            Response object
        """
        url = self._build_url(endpoint)
        
        # Set default headers if not provided
        if headers is None:
            headers = {"Content-Type": "application/json"}
        
        # Log request details
        self._log_request(method, url, **kwargs)
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                **kwargs
            )
            # Log response details
            self._log_response(response)
            
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def _get(self, endpoint: str, **kwargs: Any) -> Response:
        """Perform GET request."""
        return self.request('GET', endpoint, **kwargs)

    def _post(self, endpoint: str, **kwargs: Any) -> Response:
        """Perform POST request."""
        return self.request('POST', endpoint, **kwargs)

    def _put(self, endpoint: str, **kwargs: Any) -> Response:
        """Perform PUT request."""
        return self.request('PUT', endpoint, **kwargs)

    def _delete(self, endpoint: str, **kwargs: Any) -> Response:
        """Perform DELETE request."""
        return self.request('DELETE', endpoint, **kwargs)
