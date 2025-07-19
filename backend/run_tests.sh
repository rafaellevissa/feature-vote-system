echo "🧪 Running Feature Voting System Tests..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    print_warning "Virtual environment not detected. Activating..."
    source venv/bin/activate || {
        print_error "Failed to activate virtual environment"
        exit 1
    }
fi

# Install test dependencies if not present
print_status "Checking test dependencies..."
pip install -q pytest pytest-cov pytest-flask

# Create test database directory if needed
mkdir -p tests/temp

# Run different test suites
echo ""
echo "🧪 Running Unit Tests..."

# Run all tests with coverage
pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html --cov-fail-under=80

test_exit_code=$?

# Run specific test categories
echo ""
echo "📊 Test Results Summary:"

if [ $test_exit_code -eq 0 ]; then
    print_status "All tests passed!"
else
    print_error "Some tests failed!"
fi

# Generate coverage report
if [ -f htmlcov/index.html ]; then
    print_status "Coverage report generated: htmlcov/index.html"
fi

# Run tests by category
echo ""
echo "🏷️  Running tests by category..."

echo "📝 Model Tests:"
pytest tests/test_models.py -v

echo "🗄️  Repository Tests:"
pytest tests/test_repositories.py -v

echo "⚙️  Service Tests:"
pytest tests/test_services.py -v

echo "🌐 API Route Tests:"
pytest tests/test_routes.py -v

echo "📋 Schema Tests:"
pytest tests/test_schemas.py -v

# Performance tests
echo ""
echo "⚡ Running Performance Tests..."
pytest tests/ -v -m "not slow" --tb=short

echo ""
if [ $test_exit_code -eq 0 ]; then
    print_status "Test suite completed successfully! 🎉"
else
    print_error "Test suite completed with failures! 😞"
    exit 1
fi
