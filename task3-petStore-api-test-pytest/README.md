# PetStore API Test Framework

A Python-based API testing framework for the PetStore API using pytest and following the Page Object Model pattern.

## Project Structure

```
task3-petStore-api-test-pytest/
├── api/                    # API client layer
│   ├── base_client.py     # Base API client with error handling
│   └── endpoints/         # Endpoint-specific clients
├── config/                # Configuration management
├── models/               # Data models
├── tests/                # Test files
│   └── e2e/             # E2E test scenarios
└── utils/                # Utilities (logging, test data)
```

## Features

- Page Object Model pattern for API testing
- Environment-based configuration
- Comprehensive logging
- Data-driven testing
- Parallel test execution
- HTML and Allure reporting
- Type hints and data models
- Fixtures for test setup/teardown

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test types:
```bash
pytest -m e2e              # Run E2E tests
pytest -m negative        # Run negative tests
```

### Run tests in parallel:
```bash
pytest -n auto
```

### Generate reports:
```bash
# HTML report
pytest --html=reports/report.html

# Allure report
pytest --alluredir=allure_reports
allure serve allure_reports
```

## Test Coverage

1. End-to-End Flows:
   - Complete user lifecycle (Create -> Login -> Update -> Delete)
   - Bulk user operations
   - Authentication flows
   - Store order management (Create -> Get -> Delete)
   - Store inventory tracking
   - Negative scenarios:
     - Invalid order data validation
     - Non-existent order handling
     - Order status validation
     - Quantity and ID validation

2. API Endpoints Covered:
   - User creation
   - User authentication
   - User management (CRUD operations)
   - Bulk operations
   - Store order management (Create, Read, Delete)
   - Store inventory status

3. HTTP Status Codes:
   - 200 OK: Successful operation
   - 400 Bad Request: Invalid input provided
   - 401 Unauthorized: Authentication required
   - 404 Not Found: Resource not found
   - 422 Unprocessable Entity: Validation error (e.g., invalid order status, negative quantities)
   - 500 Internal Server Error: Unexpected server error

## Project Components

### API Client Layer
- `base_client.py`: Base API client with error handling and logging
- `endpoints/user_endpoints.py`: User-specific API endpoints
- `endpoints/store_endpoints.py`: Store-specific API endpoints:
  - get_inventory(): Get store inventory status
  - create_order(): Place an order for a pet
  - get_order_by_id(): Retrieve order by ID
  - delete_order(): Delete an order

### Models
- `user.py`: User data model with validation
- `order.py`: Store order model with fields:
  - id: Order identifier
  - petId: ID of the pet to order
  - quantity: Number of pets to order
  - shipDate: Expected shipping date
  - status: Order status (e.g., placed, approved, delivered)
  - complete: Order completion status

### Configuration
- Environment-based configuration
- Test execution settings
- Logging configuration

### Utilities
- Test data generation
- Logging setup
- Common helper functions

### Test Structure
- Fixtures for setup/teardown
- Page Object Model pattern
- Clear test organization

## Troubleshooting

### Common Issues:

1. API Connection:
   - Verify the API is running
   - Check environment configuration

2. Test Failures:
   - Check test data
   - Verify API responses
   - Review test logs
