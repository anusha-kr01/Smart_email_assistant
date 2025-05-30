# Smart Email Assistant (Free Version)

A Streamlit web app that connects to your Gmail, fetches unread emails, provides smart summaries, and auto-generates formal replies based on your input.

## Features

- Connect securely to your Gmail account
- Fetch and display unread emails with sender, subject, and preview of the body
- Generate concise summaries of email bodies
- Write a brief reply and get a polished formal email generated automatically
- Copy generated subject lines and email bodies easily

## Tech Stack

- Python
- Streamlit (for UI)
- Gmail API (for fetching emails)
- Custom summarizer and reply generation modules

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anusha-kr01/smart_email_assistant.git
   cd smart_email_assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit google-auth google-auth-oauthlib google-api-python-client
   ```

3. **Set up Gmail API credentials**:
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Gmail API
   - Create OAuth 2.0 credentials and download the `credentials.json` file
   - Place the file in the project root directory

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Connect to Gmail**  
   Click the "Connect to Gmail" button to authenticate with your Google account.

2. **View Unread Emails**  
   - The app will display your unread emails with sender, subject, and preview text
   - Click on any email to see its full content

3. **Generate Summaries**  
   - Use the "Summarize" button to get a concise summary of the selected email

4. **Compose Replies**  
   - Type a brief response in the reply box
   - Click "Generate Formal Reply" to auto-create a polished email
   - The system will suggest both subject line and email body

5. **Copy & Send**  
   - Use the "Copy Subject" and "Copy Body" buttons to easily copy the generated content
   - Paste into your email client to send

## Contributors

We welcome contributions to improve this project! Here's how you can help:

### How to Contribute

1. **Report Bugs**  
   Open an issue describing the bug with steps to reproduce

2. **Suggest Features**  
   Share your ideas for new features or improvements

3. **Code Contributions**  
   ```bash
   # Fork the repository on GitHub to your account first
   # Clone your fork locally
   git clone https://github.com/anusha-kr01/smart_email_assistant.git
   # Create a feature branch
   git checkout -b feature/your-feature-name
   # Commit your changes
   git commit -m "Add your meaningful commit message"
   # Push to your fork
   git push origin feature/your-feature-name
   # Open a pull request from your fork to the original repository

   ```

### Areas Needing Improvement
- Email categorization system
- Better error handling for authentication
- Multi-language support
- Enhanced reply templates

## Notes

- This is a free version with basic functionality
- Requires Python 3.7 or higher
- First-time authentication will open a browser window for OAuth consent

## License

MIT License © Anusha K R

## Contact
anushakr719@gmail.com
Feel free to reach out if you have any questions or want to contribute!
