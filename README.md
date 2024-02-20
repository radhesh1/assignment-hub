# Flask Web Application with HTML/CSS, Prism.js, jQuery, and Tailwind CSS

This is a simple web application built using Flask for the backend, HTML/CSS for the frontend, Prism.js for code highlighting, jQuery for client-side scripting, and Tailwind CSS for styling.

## Requirements

- Python 3.x
- Flask
- Prism.js
- jQuery
- Tailwind CSS

## Installation and Setup

1. Clone this repository:


```bash
    git clone https://github.com/radhesh1/assignment-hub.git
    ```

2. Navigate into the project directory:

    ```bash
    cd assignment-hub
    ```

3. Install the required dependencies:

    ```bash
    pip install Flask
    ```

4. Start the Flask server:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000` to view the application.

## Project Structure

```
assignment-hub/
│
├── static/                  # Static files
│   ├── css/                 # CSS files
│   │   ├── styles.css       # Main stylesheet
│   │   └── ...              # Other stylesheets
│   ├── js/                  # JavaScript files
│   │   ├── app.js           # Main JavaScript file
│   │   └── ...              # Other JavaScript files
│   └── prism/               # Prism.js files
│       ├── prism.js         # Prism.js library
│       └── ...              # Prism.js plugins (if any)
│
├── templates/               # HTML templates
│   └── index.html           # Main HTML file
│
├── app.py                   # Flask application file
└── README.md                # This README file
```

## Usage

- The main HTML template is `templates/index.html`.
- CSS files are located in `static/css/`.
- JavaScript files are located in `static/js/`.
- Prism.js and Prism CSS files are located in `static/prism/`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any problems or have suggestions for improvement.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
