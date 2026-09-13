# Test Suite Documentation

## Overview
Comprehensive test suite for the Media Dashboard Flask application, covering all API endpoints, data processing logic, and integration scenarios.

## Test Categories

### 🏠 Basic Endpoints (`TestBasicEndpoints`)
- Home page rendering
- CORS headers validation
- HTML template content verification

### 🔍 Filter Functionality (`TestFilterEndpoint`)
- Platform filtering (Netflix, Amazon Prime, Disney+, Hulu)
- Content type filtering (Movie, TV Show)
- Release year filtering
- Date range filtering
- Multiple parameter combinations

### 📊 Dashboard Overview (`TestDashboardOverviewEndpoint`)
- Chart data structure validation
- Response format verification
- Data consistency checks
- Filter parameter integration

### 👤 Actor Analytics (`TestActorAnalyticsEndpoint`)
- Actor search functionality
- Error handling for missing parameters
- Case-insensitive search validation
- Response structure verification

### ⚙️ Data Processing (`TestDataFilteringLogic`)
- `get_params()` function testing
- `filter_data()` function validation
- Edge case handling

### 🚨 Error Handling (`TestErrorHandling`)
- Invalid endpoint access
- HTTP method validation
- Invalid parameter handling
- Empty parameter processing

### 🔗 Integration Tests (`TestIntegration`)
- Complete workflow testing
- Cross-endpoint data consistency
- End-to-end functionality

### ⚡ Performance Tests (`TestPerformance`)
- Response time validation
- Large query handling
- Resource utilization checks

## Running Tests

### Method 1: Using the Test Runner Script
```bash
# Run all tests with detailed output
python run_tests.py

# Run with coverage report
python run_tests.py --coverage

# Run specific category
python run_tests.py --category basic

# Generate comprehensive report
python run_tests.py --report
```

### Method 2: Direct unittest execution
```bash
# Run all tests
python test/test_app.py

# Run specific test class
python -m unittest test.test_app.TestBasicEndpoints -v

# Run specific test method
python -m unittest test.test_app.TestBasicEndpoints.test_home_endpoint -v
```

### Method 3: Using pytest (if installed)
```bash
# Install pytest
pip install pytest pytest-cov pytest-flask

# Run all tests
python run_tests.py --pytest

# Run with coverage
python run_tests.py --pytest --coverage
```

### Method 4: Discover tests automatically
```bash
# Auto-discover and run all tests
python -m unittest discover test/ -v
```

## Test Data Requirements

### Required Files
- `data/processed/final_cleaned.csv`: Main dataset
- `templates/index.html`: Dashboard template

### Data Validation
The test suite automatically validates:
- Dataset structure and columns
- Data type consistency
- Response format compliance

## Coverage Expectations

### Target Coverage
- **API Endpoints**: 100% coverage of all routes
- **Data Processing**: 95% coverage of filtering logic
- **Error Handling**: 90% coverage of edge cases
- **Integration**: 85% coverage of workflows

### Coverage Report Generation
```bash
# Generate HTML coverage report
python run_tests.py --pytest --coverage

# View report
open test_reports/htmlcov/index.html
```

## Test Environment Setup

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt

# Ensure data file exists
ls data/processed/final_cleaned.csv
```

### Configuration
- Tests use Flask's test client
- No external database required
- Uses in-memory data processing
- Mocked request contexts for parameter testing

## Continuous Integration

### GitHub Actions Example
```yaml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.12
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python run_tests.py --pytest --coverage
```

## Expected Test Results

### Successful Test Run Output
```
MEDIA DASHBOARD - COMPREHENSIVE TEST SUITE
======================================================================
Testing Flask Application: <Flask 'app'>
Dataset Shape: (20000, 15)
======================================================================

test_home_endpoint (test.test_app.TestBasicEndpoints) ... ok
test_filter_endpoint_basic (test.test_app.TestFilterEndpoint) ... ok
...
======================================================================
TEST SUMMARY
======================================================================
Tests Run: 45
Failures: 0
Errors: 0
Success Rate: 100.0%
```

## Troubleshooting

### Common Issues

#### Data File Not Found
```
FileNotFoundError: data/processed/final_cleaned.csv
```
**Solution**: Ensure the dataset is properly placed in the data/processed/ directory

#### Import Errors
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

#### Permission Errors
```
PermissionError: [Errno 13] Permission denied
```
**Solution**: Check file permissions or run with appropriate privileges

### Debug Mode
```bash
# Run tests with Python debug output
python -v test/test_app.py

# Run with pytest debug information
python -m pytest test/ -v -s --tb=long
```

## Contributing to Tests

### Adding New Tests
1. Choose appropriate test class
2. Follow naming convention: `test_feature_description`
3. Include docstring explaining test purpose
4. Add assertions for all expected behaviors

### Test Guidelines
- Each test should be independent
- Use descriptive assertion messages
- Test both positive and negative cases
- Mock external dependencies when needed

### Example Test Structure
```python
def test_new_feature(self):
    """Test description explaining what this validates"""
    # Setup
    test_data = {...}
    
    # Execute
    response = self.app.get('/api/endpoint', data=test_data)
    
    # Assert
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertEqual(data['status'], 'success')
```