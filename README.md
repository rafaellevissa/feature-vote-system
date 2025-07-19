# Feature Voting System

A complete feature voting system with SQLite database, Flask API backend with clean architecture, and React Native (Expo) frontend that runs on Web, iOS, and Android.

## ✨ Features

- ✅ Users can post new feature requests
- ✅ Users can upvote/downvote features
- ✅ Features are sorted by popularity (upvotes)
- ✅ Real-time vote tracking per user
- ✅ Clean, modern mobile UI
- ✅ Cross-platform support (Web, iOS, Android)
- ✅ SQLite database with SQLAlchemy ORM
- ✅ RESTful API with layered architecture
- ✅ Comprehensive unit tests
- ✅ Pull-to-refresh functionality
- ✅ Form validation and error handling

## 🏗️ Architecture

### Backend (Flask + SQLAlchemy + Clean Architecture)
```
backend/
├── app.py                 # Application entry point
├── config.py             # Configuration settings
├── database.py           # Database configuration
├── models/               # SQLAlchemy models
├── repositories/         # Data access layer
├── services/            # Business logic layer
├── routes/              # API routes/controllers
├── schemas/             # Request/response schemas
└── tests/               # Unit tests
```

**Design Patterns**: Repository pattern, Service layer pattern, Dependency injection

### Frontend (React Native + Expo)
```
frontend/
├── App.js               # Root component
├── src/
│   ├── components/      # Reusable UI components
│   ├── screens/         # Screen components
│   ├── services/        # API and business logic
│   ├── hooks/           # Custom React hooks
│   ├── utils/           # Utility functions
│   ├── styles/          # Design system
│   └── navigation/      # Navigation setup
```

**Architecture**: Component-based architecture, Custom hooks, Service layer, Design system

## 🚀 Quick Start

### Prerequisites
- **Backend**: Python 3.8+, pip
- **Frontend**: Node.js 16+, npm
- **Mobile Development**: Expo CLI

### 1. Clone & Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd feature-voting-system

# Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

# In a new terminal, setup frontend
cd frontend
npm install
npm start
```

### 2. Access the Application
- **API**: http://localhost:5000
- **Web App**: Press `w` in Expo terminal or visit http://localhost:19006
- **Mobile**: Install Expo Go app and scan QR code
- **iOS Simulator**: Press `i` in Expo terminal (macOS only)
- **Android Emulator**: Press `a` in Expo terminal

## 📱 Platform Support

| Platform | Status | How to Run |
|----------|--------|------------|
| **Web** | ✅ Ready | `npm run web` or press `w` |
| **iOS** | ✅ Ready | `npm run ios` or press `i` |
| **Android** | ✅ Ready | `npm run android` or press `a` |

## 🛠️ Development Setup

### Backend Development

1. **Create virtual environment**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run development server**:
   ```bash
   python app.py
   ```
   Server runs on http://localhost:5000

4. **Run tests**:
   ```bash
   python -m pytest tests/ -v
   ```

### Frontend Development

1. **Install dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server**:
   ```bash
   npm start
   ```

3. **Platform-specific commands**:
   ```bash
   npm run web      # Web browser
   npm run ios      # iOS simulator
   npm run android  # Android emulator
   ```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/ -v --coverage
```

**Test Coverage**:
- ✅ Repository layer tests
- ✅ Service layer tests  
- ✅ API endpoint tests
- ✅ Model validation tests
- ✅ Error handling tests

### Frontend Tests (Coming Soon)
```bash
cd frontend
npm test
```

## 📚 API Documentation

### Base URL
- Development: `http://localhost:5000`
- Production: `https://your-domain.com`

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/features` | Get all features (sorted by upvotes) |
| `POST` | `/api/features` | Create new feature |
| `GET` | `/api/features/{id}` | Get specific feature |
| `DELETE` | `/api/features/{id}` | Delete feature |
| `POST` | `/api/features/{id}/upvote` | Upvote a feature |
| `DELETE` | `/api/features/{id}/remove-vote` | Remove vote |
| `GET` | `/api/user/{user_id}/votes` | Get user's votes |
| `GET` | `/api/health` | Health check |

### Request/Response Examples

**Create Feature**:
```json
POST /api/features
{
  "title": "Dark mode support",
  "description": "Add dark mode toggle to the app",
  "author": "John Doe"
}
```

**Response**:
```json
{
  "id": 1,
  "title": "Dark mode support",
  "description": "Add dark mode toggle to the app", 
  "author": "John Doe",
  "upvotes": 0,
  "created_at": "2025-01-20T10:30:00",
  "updated_at": "2025-01-20T10:30:00"
}
```

## 🗄️ Database Schema

### Feature Model
- `id` (Primary Key)
- `title` (String, required, max 200 chars)
- `description` (Text, optional, max 1000 chars)
- `author` (String, required, max 100 chars)
- `upvotes` (Integer, default 0)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Vote Model
- `id` (Primary Key)
- `feature_id` (Foreign Key to Feature)
- `user_id` (String, required)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- **Unique constraint**: (feature_id, user_id)

## 🎨 Design System

### Colors
- **Primary**: #007AFF (iOS Blue)
- **Success**: #34C759 (Green)
- **Error**: #FF3B30 (Red)
- **Background**: #F5F5F5 (Light Gray)

### Typography
- **Headings**: System font, bold weights
- **Body**: System font, regular weight
- **Captions**: System font, medium weight

### Components
- **Button**: Primary, secondary, outline variants
- **Input**: With validation and error states
- **Modal**: Consistent overlay design
- **Cards**: Material Design inspired

## 🔧 Configuration

### Backend Configuration
Edit `backend/config.py`:
```python
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///features.db'
```

### Frontend Configuration
Edit `frontend/src/utils/constants.js`:
```javascript
export const API_CONFIG = {
  BASE_URL: Platform.select({
    android: 'http://10.0.2.2:5000',
    ios: 'http://localhost:5000', 
    web: 'http://localhost:5000',
  }),
};
```

## 🚢 Deployment

### Backend Deployment
- **Heroku**: Ready for Heroku deployment
- **DigitalOcean**: Production-ready with Gunicorn
- **AWS/GCP**: Cloud deployment ready

### Frontend Deployment
- **Web**: Expo build for Netlify/Vercel
- **Mobile**: Expo build service for app stores
- **Progressive Web App**: PWA support included

## 🔒 Security Features

- ✅ Input validation and sanitization
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ CORS configuration
- ✅ Error handling without sensitive data exposure
- ✅ Request/response validation schemas

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and add tests
4. Run tests: `npm test` and `pytest`
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📝 Development Notes

### Adding New Features
1. **Backend**: Model → Repository → Service → Route → Test
2. **Frontend**: Component → Screen → Hook → Service → Style

### Code Style
- **Backend**: PEP 8 compliance, type hints recommended
- **Frontend**: ESLint + Prettier, functional components with hooks

### Performance Tips
- Backend: Use database indexing, implement caching
- Frontend: Lazy loading, image optimization, state management

## 🐛 Troubleshooting

### Common Issues

**Backend Issues**:
```bash
# Virtual environment activation
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Database reset
rm features.db
python app.py  # Recreates database
```

**Frontend Issues**:
```bash
# Clear Expo cache
expo start -c

# Reset Metro bundler
npx expo start --clear

# Install web dependencies
npx expo install react-native-web react-dom
```

### Platform-Specific Notes
- **Android Emulator**: Use `http://10.0.2.2:5000` for API calls
- **iOS Simulator**: Use `http://localhost:5000` for API calls  
- **Physical Device**: Use your computer's IP address
- **Web**: CORS must be enabled for API calls

## 👥 Team

- **Backend Architecture**: Clean architecture with Flask
- **Frontend Development**: React Native with Expo
- **Database Design**: SQLAlchemy ORM with SQLite
- **Testing**: Comprehensive unit test coverage

## 🔗 Links

- [Expo Documentation](https://docs.expo.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Native Documentation](https://reactnative.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Ready to vote on features? Let's build something amazing together! 🚀**

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