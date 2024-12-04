# Flask English-French Translator

A web application built with Flask that provides real-time translation between English and French using IBM Watson Language Translator service.

## Features

- Bidirectional translation support (English ↔ French)
- RESTful API endpoints for translation services
- Clean, responsive web interface
- Comprehensive test suite
- IBM Watson Language Translator integration

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, JavaScript
- **Translation Service**: IBM Watson Language Translator
- **Testing**: Python unittest
- **Deployment**: IBM Cloud

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flask-english-french-translator.git
cd flask-english-french-translator
```

2. Set up a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the project root with your IBM Watson credentials:
```
apikey=your_api_key_here
url=your_service_url_here
```

## Usage

1. Start the Flask server:
```bash
python server.py
```

2. Access the application at `http://localhost:8080`

## API Endpoints

- `GET /englishToFrench?textToTranslate=<text>`: Translates English text to French
- `GET /frenchToEnglish?textToTranslate=<text>`: Translates French text to English

## Testing

Run the test suite:
```bash
python -m unittest final_project/machinetranslation/tests/tests.py
```

## Project Structure

```
final_project/
├── machinetranslation/
│   ├── tests/
│   │   └── tests.py
│   ├── translator.py
│   └── __init__.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── manifest.yml
├── Procfile
├── requirements.txt
├── runtime.txt
└── server.py
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

## License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.

## Deployment

The application is deployed on IBM Cloud. Access the live demo [here](https://flaskenglishfrenchtranslatorapp.mybluemix.net/).

## Acknowledgments

- IBM Watson Language Translator service
- Flask framework and community
- Contributors and testers
