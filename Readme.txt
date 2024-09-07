

# Masked Word Prediction with Flask

This project is a web application built with Flask that predicts masked words in sentences using a pre-trained BERT model (`bert-base-multilingual-cased`). The app allows users to input sentences with masked tokens (`[MASK]`) and receive top predictions for those masked tokens.

## Demo

![App Screenshot](path/to/your/screenshot.png)  <!-- Add a path to an image that shows your app in action -->

## Features

- Predict masked words in sentences using BERT.
- Simple and intuitive web interface.
- Supports multilingual text input.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Transformers**: Library from Hugging Face used for NLP models.
- **PyTorch**: Deep learning framework used to run the BERT model.
- **HTML/CSS**: For the frontend of the application.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Prerequisites

- Python 3.7 or above
- Git

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/story-generation-app.git
   cd story-generation-app
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

   **Note:** If `requirements.txt` is not available, manually install the dependencies:

   ```
   pip install flask transformers torch
   ```

### Running the Application

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

### Usage

1. Enter a sentence with a `[MASK]` token where you want predictions.
2. Click the "Predict" button.
3. The app will display the top predicted tokens for the masked position.

## Project Structure

```
story-generation-app/
│
├── app.py                # Main Flask application file
├── requirements.txt      # Dependencies for the project
├── templates/
│   └── index.html        # HTML file for the app's UI
└── static/
    └── styles.css        # CSS file for styling
```

## Screenshots

![App Screenshot](path/to/your/screenshot.png)  <!-- Update this with actual paths to your app's screenshots -->

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Hugging Face Transformers for providing pre-trained models.
- Flask documentation for guidance on building web applications.



