.PHONY: help install test test-cov test-unit test-integration clean setup dev

# Default target
help:
	@echo "Available commands:"
	@echo "  setup     - Initial project setup"
	@echo "  install   - Install dependencies"
	@echo "  dev       - Start development servers"
	@echo "  test      - Run all tests"
	@echo "  test-cov  - Run tests with coverage"
	@echo "  test-unit - Run unit tests only"
	@echo "  clean     - Clean up temp files"

# Setup project
setup:
	@echo "🚀 Setting up Feature Voting System..."
	cd backend && python -m venv venv
	cd backend && source venv/bin/activate && pip install -r requirements.txt
	cd frontend && npm install
	@echo "✅ Setup complete!"

# Install dependencies
install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

# Start development servers
dev:
	@echo "🚀 Starting development servers..."
	# Start backend in background
	cd backend && source venv/bin/activate && python app.py &
	# Start frontend
	cd frontend && npm start

# Run all tests
test:
	cd backend && source venv/bin/activate && python -m pytest tests/ -v

# Run tests with coverage
test-cov:
	cd backend && source venv/bin/activate && python -m pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html

# Run unit tests only
test-unit:
	cd backend && source venv/bin/activate && python -m pytest tests/ -v -m "unit"

# Run integration tests only
test-integration:
	cd backend && source venv/bin/activate && python -m pytest tests/ -v -m "integration"

# Clean up
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf backend/htmlcov
	rm -rf backend/.coverage
	rm -rf backend/.pytest_cache
	rm -rf frontend/node_modules/.cache