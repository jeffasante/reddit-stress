# Reddit Stress Detection

This repository contains code for a Reddit stress detection application, utilizing machine learning models to predict whether a given text contains indications of stress. It also includes functionality to fetch comments from Reddit for further analysis.

## Files Included

- `app.py`: Main Python script containing the Dash application setup and callbacks.
- `ml.py`: Python script containing machine learning model setup and prediction functions.
- `preprocess.py`: Python script containing text preprocessing functions.
- `reddit.py`: Python script containing functions for fetching comments from Reddit.
- `saved_models/`: Directory containing saved machine learning models.
- `.gitignore`: File to specify intentionally untracked files to ignore.
- `.DS_Store`: macOS system file to store custom attributes of a folder.

## Usage

1. **Installation**: Ensure you have the required dependencies installed. You can install them using `pip install -r requirements.txt`.

2. **Running the Application**: Execute `app.py` to run the Dash application. The application will start a server locally.

3. **Interacting with the Application**: Once the server is running, you can access the application through a web browser. The interface allows you to input text for stress prediction and fetch comments from Reddit for analysis.

4. **Predicting Stress**: Enter text into the text area and click the "Predict" button to see if the text contains indications of stress. The result will be displayed, along with the prediction label colored either red for "Stress" or blue for "Not Stressed".

5. **Fetching Reddit Comments**: Click the "Fetch Post" button to retrieve comments from a random Reddit post related to stress. The fetched comments will be displayed along with the title of the Reddit post.

## Dependencies

- `dash`: Dash web application framework for Python.
- `praw`: Python Reddit API Wrapper for accessing Reddit API.
- `joblib`: Library for saving and loading scikit-learn models.
- `scikit-learn`: Machine learning library for Python.

## Configuration

Before running the application, ensure you provide valid credentials for accessing the Reddit API. Update the `user_agent`, `client_id`, `client_secret`, `password`, and `username` variables in `reddit.py` with your Reddit API credentials.

## Note

- This application is intended for educational and demonstration purposes only. It is not intended to provide medical advice or diagnosis.
- Make sure to use the application responsibly and adhere to Reddit API usage guidelines and policies.
- Proper attribution to Reddit and its content creators should be maintained when using fetched Reddit comments.
- Remember to handle sensitive information securely, especially when dealing with user authentication credentials.
