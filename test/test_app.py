"""
Test suite for Media Dashboard Flask Application

This module contains comprehensive unit tests for all API endpoints
and core functionality of the streaming media analytics dashboard.

Test Categories:
- Basic endpoint functionality
- Data filtering logic
- Error handling
- Response structure validation
- Integration tests

Author: Media Dashboard Team
Version: 1.0
"""

import unittest
import json
import sys
import os
from datetime import datetime
from unittest.mock import patch, MagicMock
import pandas as pd

# Add the parent directory to sys.path to import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, df, get_params, filter_data


class MediaDashboardTestCase(unittest.TestCase):
    """Base test case for Media Dashboard application"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.app = app.test_client()
        self.app.testing = True
        
        # Sample test data
        self.sample_data = {
            'show_id': 's1',
            'type': 'Movie',
            'title': 'Test Movie',
            'director': 'Test Director',
            'cast': 'Test Actor, Another Actor',
            'country': 'United States',
            'date_added': '2023-01-15',
            'release_year': 2023,
            'rating': 'PG-13',
            'duration': '120 min',
            'listed_in': 'Action, Drama',
            'description': 'A test movie for unit testing',
            'platform': 'Netflix'
        }
    
    def tearDown(self):
        """Clean up after each test method"""
        pass


class TestBasicEndpoints(MediaDashboardTestCase):
    """Test basic endpoint functionality"""
    
    def test_home_endpoint(self):
        """Test the home endpoint returns HTML template"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'text/html', response.content_type.encode())
    
    def test_home_endpoint_contains_dashboard_title(self):
        """Test home page contains the dashboard title"""
        response = self.app.get('/')
        self.assertIn(b'Media Dashboard', response.data)
    
    def test_cors_headers(self):
        """Test CORS headers are properly set"""
        response = self.app.get('/api/dashboard/overview')
        self.assertIn('Access-Control-Allow-Origin', response.headers)


class TestFilterEndpoint(MediaDashboardTestCase):
    """Test /api/filter endpoint functionality"""
    
    def test_filter_endpoint_basic(self):
        """Test basic filter endpoint without parameters"""
        response = self.app.get('/api/filter')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('total_results', data)
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)
    
    def test_filter_by_platform(self):
        """Test filtering by platform"""
        response = self.app.get('/api/filter?platform=Netflix')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        
        # Check if all results are from Netflix
        if data['data']:
            for item in data['data']:
                self.assertEqual(item.get('platform', '').lower(), 'netflix')
    
    def test_filter_by_type(self):
        """Test filtering by content type"""
        response = self.app.get('/api/filter?type=Movie')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        
        # Check if all results are movies
        if data['data']:
            for item in data['data']:
                self.assertEqual(item.get('type', '').lower(), 'movie')
    
    def test_filter_by_release_year(self):
        """Test filtering by release year"""
        response = self.app.get('/api/filter?release_year=2020')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        
        # Check if all results are from 2020
        if data['data']:
            for item in data['data']:
                self.assertEqual(item.get('release_year'), 2020)
    
    def test_filter_by_date_range(self):
        """Test filtering by date range"""
        response = self.app.get('/api/filter?start_date=2020-01-01&end_date=2020-12-31')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        
        # Validate date format in response
        if data['data']:
            for item in data['data']:
                if item.get('date_added'):
                    date_added = datetime.strptime(item['date_added'], '%Y-%m-%d')
                    self.assertGreaterEqual(date_added, datetime(2020, 1, 1))
                    self.assertLessEqual(date_added, datetime(2020, 12, 31))
    
    def test_filter_multiple_parameters(self):
        """Test filtering with multiple parameters"""
        response = self.app.get('/api/filter?platform=Netflix&type=Movie&release_year=2020')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')


class TestDashboardOverviewEndpoint(MediaDashboardTestCase):
    """Test /api/dashboard/overview endpoint functionality"""
    
    def test_dashboard_overview_basic(self):
        """Test basic dashboard overview endpoint"""
        response = self.app.get('/api/dashboard/overview')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('total_titles', data)
        self.assertIn('charts', data)
    
    def test_dashboard_overview_structure(self):
        """Test dashboard overview response structure"""
        response = self.app.get('/api/dashboard/overview')
        data = json.loads(response.data)
        
        # Check main structure
        required_fields = ['status', 'total_titles', 'charts']
        for field in required_fields:
            self.assertIn(field, data)
        
        # Check charts structure
        charts = data['charts']
        required_charts = [
            'platform_distribution',
            'type_distribution', 
            'top_genres',
            'rating_distribution',
            'trends'
        ]
        
        for chart in required_charts:
            self.assertIn(chart, charts)
            self.assertIn('labels', charts[chart])
            self.assertIn('values', charts[chart])
            self.assertIsInstance(charts[chart]['labels'], list)
            self.assertIsInstance(charts[chart]['values'], list)
    
    def test_dashboard_overview_with_filters(self):
        """Test dashboard overview with filtering parameters"""
        response = self.app.get('/api/dashboard/overview?platform=Netflix&type=Movie')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIsInstance(data['total_titles'], int)
    
    def test_chart_data_consistency(self):
        """Test that chart data is consistent and valid"""
        response = self.app.get('/api/dashboard/overview')
        data = json.loads(response.data)
        
        charts = data['charts']
        
        # Check that labels and values have the same length
        for chart_name, chart_data in charts.items():
            labels = chart_data['labels']
            values = chart_data['values']
            self.assertEqual(len(labels), len(values), 
                           f"Labels and values length mismatch in {chart_name}")
            
            # Check that all values are non-negative integers
            for value in values:
                self.assertIsInstance(value, (int, float))
                self.assertGreaterEqual(value, 0)


class TestActorAnalyticsEndpoint(MediaDashboardTestCase):
    """Test /api/dashboard/actor endpoint functionality"""
    
    def test_actor_endpoint_missing_parameter(self):
        """Test actor endpoint without name parameter"""
        response = self.app.get('/api/dashboard/actor')
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertIn('message', data)
    
    def test_actor_endpoint_with_name(self):
        """Test actor endpoint with name parameter"""
        response = self.app.get('/api/dashboard/actor?name=Tom Hanks')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('actor', data)
        self.assertIn('total_works', data)
    
    def test_actor_endpoint_structure(self):
        """Test actor endpoint response structure"""
        response = self.app.get('/api/dashboard/actor?name=Actor')
        data = json.loads(response.data)
        
        if data['total_works'] > 0:
            # Check required fields for successful actor search
            required_fields = ['status', 'actor', 'total_works', 'charts', 'recent_works']
            for field in required_fields:
                self.assertIn(field, data)
            
            # Check charts structure
            charts = data['charts']
            required_charts = ['platform_distribution', 'top_genres', 'career_timeline']
            
            for chart in required_charts:
                self.assertIn(chart, charts)
                if charts[chart]['labels']:  # If there's data
                    self.assertIn('labels', charts[chart])
                    self.assertIn('values', charts[chart])
            
            # Check recent_works structure
            self.assertIsInstance(data['recent_works'], list)
            if data['recent_works']:
                work = data['recent_works'][0]
                work_fields = ['title', 'type', 'release_year', 'platform', 'listed_in']
                for field in work_fields:
                    self.assertIn(field, work)
    
    def test_actor_endpoint_nonexistent_actor(self):
        """Test actor endpoint with non-existent actor"""
        response = self.app.get('/api/dashboard/actor?name=NonexistentActor12345')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['total_works'], 0)
    
    def test_actor_endpoint_case_insensitive(self):
        """Test that actor search is case insensitive"""
        # Test with different cases (assuming there's data)
        response1 = self.app.get('/api/dashboard/actor?name=actor')
        response2 = self.app.get('/api/dashboard/actor?name=ACTOR')
        response3 = self.app.get('/api/dashboard/actor?name=Actor')
        
        # All should return 200
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)


class TestDataFilteringLogic(MediaDashboardTestCase):
    """Test the data filtering logic functions"""
    
    def test_get_params_function(self):
        """Test get_params function with mocked request"""
        with app.test_request_context('/?platform=Netflix&type=Movie'):
            params = get_params()
            self.assertEqual(params['platform'], 'Netflix')
            self.assertEqual(params['type'], 'Movie')
            self.assertIsNone(params['cast'])  # Should be None if not provided
    
    def test_filter_data_function(self):
        """Test filter_data function with sample data"""
        # Create a small test DataFrame
        test_df = pd.DataFrame([
            {
                'platform': 'Netflix',
                'type': 'Movie', 
                'title': 'Test Movie 1',
                'cast': 'Actor A, Actor B',
                'release_year': 2020,
                'date_added': pd.to_datetime('2020-01-15')
            },
            {
                'platform': 'Hulu',
                'type': 'TV Show',
                'title': 'Test Show 1', 
                'cast': 'Actor C, Actor D',
                'release_year': 2021,
                'date_added': pd.to_datetime('2021-02-10')
            }
        ])
        
        # Test platform filtering
        filtered = filter_data(test_df, platform='Netflix')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['platform'], 'Netflix')
        
        # Test type filtering
        filtered = filter_data(test_df, type='Movie')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['type'], 'Movie')
        
        # Test cast filtering (contains search)
        filtered = filter_data(test_df, cast='Actor A')
        self.assertEqual(len(filtered), 1)
        
        # Test release year filtering
        filtered = filter_data(test_df, release_year='2020')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered.iloc[0]['release_year'], 2020)


class TestErrorHandling(MediaDashboardTestCase):
    """Test error handling and edge cases"""
    
    def test_invalid_endpoint(self):
        """Test accessing invalid endpoint"""
        response = self.app.get('/api/invalid_endpoint')
        self.assertEqual(response.status_code, 404)
    
    def test_post_method_on_get_endpoint(self):
        """Test using POST method on GET-only endpoint"""
        response = self.app.post('/api/dashboard/overview')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed
    
    def test_invalid_date_format(self):
        """Test invalid date format in filtering"""
        response = self.app.get('/api/filter?start_date=invalid-date')
        # Should not crash, might return empty results or handle gracefully
        self.assertIn(response.status_code, [200, 400])
    
    def test_empty_parameters(self):
        """Test empty parameters"""
        response = self.app.get('/api/filter?platform=&type=')
        self.assertEqual(response.status_code, 200)


class TestIntegration(MediaDashboardTestCase):
    """Integration tests for complete workflows"""
    
    def test_full_dashboard_workflow(self):
        """Test complete dashboard workflow"""
        # 1. Load home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # 2. Get overview data
        response = self.app.get('/api/dashboard/overview')
        self.assertEqual(response.status_code, 200)
        overview_data = json.loads(response.data)
        
        # 3. Apply filters to overview
        response = self.app.get('/api/dashboard/overview?platform=Netflix')
        self.assertEqual(response.status_code, 200)
        filtered_overview = json.loads(response.data)
        
        # 4. Search for actor (if there's data)
        if overview_data['total_titles'] > 0:
            response = self.app.get('/api/dashboard/actor?name=Actor')
            self.assertEqual(response.status_code, 200)
    
    def test_data_consistency_across_endpoints(self):
        """Test data consistency across different endpoints"""
        # Get overview data
        overview_response = self.app.get('/api/dashboard/overview')
        overview_data = json.loads(overview_response.data)
        
        # Get filter data with same parameters
        filter_response = self.app.get('/api/filter')
        filter_data = json.loads(filter_response.data)
        
        # Total counts should match
        self.assertEqual(overview_data['total_titles'], filter_data['total_results'])


class TestPerformance(MediaDashboardTestCase):
    """Basic performance tests"""
    
    def test_response_time_overview(self):
        """Test that overview endpoint responds quickly"""
        import time
        start_time = time.time()
        response = self.app.get('/api/dashboard/overview')
        end_time = time.time()
        
        self.assertEqual(response.status_code, 200)
        # Should respond within 5 seconds (adjust based on data size)
        self.assertLess(end_time - start_time, 5.0)
    
    def test_large_filter_query(self):
        """Test filtering with multiple parameters"""
        response = self.app.get('/api/filter?platform=Netflix&type=Movie&rating=PG-13')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')


def create_test_suite():
    """Create and return the test suite"""
    test_suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestBasicEndpoints,
        TestFilterEndpoint,
        TestDashboardOverviewEndpoint,
        TestActorAnalyticsEndpoint,
        TestDataFilteringLogic,
        TestErrorHandling,
        TestIntegration,
        TestPerformance
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    return test_suite


if __name__ == '__main__':
    # Run all tests with verbose output
    print("="*70)
    print("MEDIA DASHBOARD - COMPREHENSIVE TEST SUITE")
    print("="*70)
    print(f"Testing Flask Application: {app}")
    print(f"Dataset Shape: {df.shape if 'df' in globals() else 'Not loaded'}")
    print("="*70)
    
    # Create and run the test suite
    test_suite = create_test_suite()
    runner = unittest.TextTestRunner(
        verbosity=2,
        descriptions=True,
        failfast=False
    )
    
    result = runner.run(test_suite)
    
    # Print summary
    print("="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"- {test}")
    
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"- {test}")
    
    print("="*70)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)