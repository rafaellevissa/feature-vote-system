# Feature Voting System

A complete feature voting system with SQLite database, Flask API backend with clean architecture, and React Native mobile frontend.

## Features

- ✅ Users can post new feature requests
- ✅ Users can upvote/downvote features
- ✅ Features are sorted by popularity (upvotes)
- ✅ Real-time vote tracking per user
- ✅ Clean, modern mobile UI
- ✅ SQLite database with SQLAlchemy ORM
- ✅ RESTful API with layered architecture
- ✅ Cross-platform mobile app (iOS & Android)

## Architecture

### Backend (Flask + SQLAlchemy + Clean Architecture)
- **Database**: SQLite with SQLAlchemy ORM
- **Architecture**: Layered architecture with separation of concerns
  - **Models**: SQLAlchemy ORM models
  - **Repositories**: Data access layer
  - **Services**: Business logic layer
  - **Routes**: API endpoints (presentation layer)
  - **Schemas**: Request/response validation
- **Design Patterns**: Repository pattern, Service layer pattern
- **Features**: CRUD operations, vote tracking, user vote history

### Frontend (React Native)
- **Platform**: Cross-platform mobile app
- **State Management**: React hooks with AsyncStorage
- **UI**: Modern, responsive design with pull-to-refresh
- **User Management**: Automatic unique user ID generation

## Project Structure

```
backend/
├── app.py                 # Application entry point
├── config.py             # Configuration settings
├── database.py           # Database configuration
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── base.py          # Base model class
│   ├── feature.py       # Feature model
│   └── vote.py          # Vote model
├── repositories/         # Data access layer
│   ├── __init__.py
│   ├── base.py          # Base repository
│   ├── feature_repository.py
│   └── vote_repository.py
├── services/            # Business logic layer
│   ├── __init__.py
│   ├── feature_service.py
│   └── vote_service.py
├── routes/              # API routes/controllers
│   ├── __init__.py
│   ├── feature_routes.py
│   └── health_routes.py
└── schemas/             # Request/response schemas
    ├── __init__.py
    └── feature_schemas.py
```

## API Endpoints

- `GET /api/features` - Get all features (sorted by upvotes)
- `POST /api/features` - Create new feature
- `GET /api/features/{id}` - Get specific feature
- `DELETE /api/features/{id}` - Delete feature
- `POST /api/features/{id}/upvote` - Upvote a feature
- `DELETE /api/features/{id}/remove-vote` - Remove vote
- `GET /api/user/{user_id}/votes` - Get user's votes
- `GET /api/health` - Health check

## Database Schema

The application uses SQLAlchemy ORM with the following models:

### Feature Model
- `id` (Primary Key)
- `title` (String, required)
- `description` (Text, optional)
- `author` (String, required)
- `upvotes` (Integer, default 0)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Vote Model
- `id` (Primary Key)
- `feature_id` (Foreign Key to Feature)
- `user_id` (String, required)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- Unique constraint on (feature_id, user_id)

## Setup Instructions

### Backend Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server**:
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

### React Native Setup

1. **Install React Native CLI** (if not already installed):
   ```bash
   npm install -g react-native-cli
   ```

2. **Install project dependencies**:
   ```bash
   npm install
   ```

3. **Install iOS dependencies** (iOS only):
   ```bash
   cd ios && pod install && cd ..
   ```

4. **Configure API URL**:
   - Open `App.js`
   - Update `API_BASE_URL` based on your setup:
     - Android Emulator: `http://10.0.2.2:5000`
     - iOS Simulator: `http://localhost:5000`
     - Physical Device: `http://YOUR_COMPUTER_IP:5000`

5. **Run the app**:
   ```bash
   # For Android
   npx react-native run-android
   
   # For iOS
   npx react-native run-ios
   ```

## Architecture Benefits

### Scalability
- **Layered Architecture**: Easy to modify individual layers
- **Repository Pattern**: Database queries centralized and reusable
- **Service Layer**: Business logic separated from controllers
- **Clean Separation**: Easy to add new features or change implementations

### Maintainability
- **Single Responsibility**: Each class has one clear purpose
- **Dependency Injection**: Services can be easily mocked for testing
- **Error Handling**: Centralized error handling in services
- **Type Safety**: Clear interfaces and data structures

### Testability
- **Unit Testing**: Each layer can be tested independently
- **Mocking**: Repository layer can be mocked for service testing
- **Integration Testing**: API endpoints can be tested end-to-end

## Development Notes

### Backend Development
- Models define database structure using SQLAlchemy ORM
- Repositories handle all database operations
- Services contain business logic and validation
- Routes are thin controllers that handle HTTP requests/responses
- Database migrations can be handled with Flask-Migrate (not included)

### Adding New Features
1. **Create Model**: Add new SQLAlchemy model in `models/`
2. **Create Repository**: Add data access methods in `repositories/`
3. **Create Service**: Add business logic in `services/`
4. **Create Routes**: Add API endpoints in `routes/`
5. **Create Schemas**: Add validation schemas in `schemas/`

### Frontend Development
- User ID is automatically generated and stored locally
- Pull-to-refresh functionality for updating data
- Modal interface for adding new features
- Visual feedback for voted features
- Error handling with user-friendly alerts

### Network Configuration
- **Android Emulator**: Use `10.0.2.2` to access localhost
- **iOS Simulator**: Use `localhost` or `127.0.0.1`
- **Physical Devices**: Use your computer's IP address
- Ensure your computer firewall allows connections on port 5000

## Future Enhancements

- Add authentication/authorization
- Add feature categories
- Add commenting system
- Add feature status tracking (pending, in-progress, completed)
- Add admin panel
- Add email notifications
- Add database migrations
- Add comprehensive testing suite
- Add API documentation (Swagger)
- Add logging and monitoring
   ```

3. **Install iOS dependencies** (iOS only):
   ```bash
   cd ios && pod install && cd ..
   ```

4. **Configure API URL**:
   - Open `App.js`
   - Update `API_BASE_URL` based on your setup:
     - Android Emulator: `http://10.0.2.2:5000`
     - iOS Simulator: `http://localhost:5000`
     - Physical Device: `http://YOUR_COMPUTER_IP:5000`

5. **Run the app**:
   ```bash
   # For Android
   npx react-native run-android
   
   # For iOS
   npx react-native run-ios
   ```

## Development Notes

### Backend Development
- The Flask server runs with debug mode enabled
- Database is automatically initialized on first run
- CORS is enabled for React Native requests
- Each user vote is tracked to prevent duplicate voting

### Frontend Development
- User ID is automatically generated and stored locally
- Pull-to-refresh functionality for updating data
- Modal interface for adding new features
- Visual feedback for voted features
- Error handling with user-friendly alerts

### Network Configuration
- **Android Emulator**: Use `10.0.2.2` to access localhost
- **iOS Simulator**: Use `localhost` or `127.0.0.1`
- **Physical Devices**: Use your computer's IP address
- Ensure your computer firewall allows connections on port 5000

## Testing

1. **Start the backend server**
2. **Test API endpoints** using
