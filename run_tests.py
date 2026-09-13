#!/usr/bin/env python3
"""
Test Runner Script for Media Dashboard

This script provides multiple ways to run the test suite:
1. Run all tests with detailed output
2. Run specific test categories
3. Generate coverage reports
4. Run performance benchmarks

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py --category basic   # Run specific category
    python run_tests.py --coverage        # Run with coverage
    python run_tests.py --fast            # Skip slow tests
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def run_unittest_suite():
    """Run the complete unittest suite"""
    print("🧪 Running Media Dashboard Test Suite with unittest...")
    
    # Import and run the test suite
    from test.test_app import create_test_suite
    import unittest
    
    test_suite = create_test_suite()
    runner = unittest.TextTestRunner(
        verbosity=2,
        descriptions=True,
        failfast=False,
        stream=sys.stdout,
        buffer=False
    )
    
    result = runner.run(test_suite)
    return result.wasSuccessful()

def run_pytest_suite(coverage=False, category=None):
    """Run tests using pytest"""
    print("🧪 Running Media Dashboard Test Suite with pytest...")
    
    cmd = ['python', '-m', 'pytest', 'test/', '-v']
    
    if coverage:
        cmd.extend(['--cov=app', '--cov-report=html', '--cov-report=term-missing'])
    
    if category:
        cmd.extend(['-k', category])
    
    try:
        result = subprocess.run(cmd, cwd=project_root, capture_output=False)
        return result.returncode == 0
    except FileNotFoundError:
        print("❌ pytest not found. Install with: pip install pytest pytest-cov")
        return False

def check_dependencies():
    """Check if required dependencies are available"""
    print("🔍 Checking dependencies...")
    
    required_packages = ['flask', 'pandas', 'flask_cors']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies available")
    return True

def check_data_file():
    """Check if the data file exists"""
    data_file = project_root / 'data' / 'processed' / 'final_cleaned.csv'
    
    if data_file.exists():
        print(f"✅ Data file found: {data_file}")
        return True
    else:
        print(f"⚠️  Data file not found: {data_file}")
        print("Some tests may fail without the dataset")
        return False

def run_specific_tests(test_pattern):
    """Run specific test patterns"""
    print(f"🎯 Running specific tests: {test_pattern}")
    
    cmd = ['python', '-m', 'unittest', f'test.test_app.{test_pattern}', '-v']
    
    try:
        result = subprocess.run(cmd, cwd=project_root)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running specific tests: {e}")
        return False

def generate_test_report():
    """Generate a comprehensive test report"""
    print("📊 Generating test report...")
    
    # Create reports directory
    reports_dir = project_root / 'test_reports'
    reports_dir.mkdir(exist_ok=True)
    
    # Run tests with XML output for CI/CD
    cmd = [
        'python', '-m', 'pytest', 'test/', 
        '--junit-xml=test_reports/junit.xml',
        '--cov=app',
        '--cov-report=xml:test_reports/coverage.xml',
        '--cov-report=html:test_reports/htmlcov',
        '-v'
    ]
    
    try:
        result = subprocess.run(cmd, cwd=project_root)
        if result.returncode == 0:
            print(f"📈 Test report generated in: {reports_dir}")
        return result.returncode == 0
    except FileNotFoundError:
        print("❌ pytest not available for report generation")
        return False

def main():
    """Main test runner function"""
    parser = argparse.ArgumentParser(description='Media Dashboard Test Runner')
    parser.add_argument('--coverage', action='store_true', help='Run tests with coverage')
    parser.add_argument('--category', help='Run specific test category')
    parser.add_argument('--pytest', action='store_true', help='Use pytest instead of unittest')
    parser.add_argument('--fast', action='store_true', help='Skip slow tests')
    parser.add_argument('--report', action='store_true', help='Generate comprehensive test report')
    parser.add_argument('--specific', help='Run specific test pattern')
    
    args = parser.parse_args()
    
    print("🚀 Media Dashboard Test Runner")
    print("=" * 50)
    
    # Pre-flight checks
    if not check_dependencies():
        return 1
    
    check_data_file()
    print()
    
    # Run tests based on arguments
    success = True
    
    if args.report:
        success = generate_test_report()
    elif args.specific:
        success = run_specific_tests(args.specific)
    elif args.pytest:
        success = run_pytest_suite(coverage=args.coverage, category=args.category)
    else:
        success = run_unittest_suite()
    
    # Print final result
    print("\n" + "=" * 50)
    if success:
        print("✅ All tests passed! Dashboard is ready for deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please review the output above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())