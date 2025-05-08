# ☁ AWS Project

## 📄 Descriprion

Web-application developed in this project allows user to interact with AWS techologies (e.g. S3 or E2) through UI.

---

## 🛠 Features

### S3

- **Create** a folder inside bucket
- **Delete** object (file or folder) from bucket
- **List** all objects inside a bucket
- **Upload** file to a (folder(s) in) backet
- **Download** file from server
- **Display** image from bucket

---

## ⚙ Requirements

- Python 3.10+
- Flask
- Boto3
- AWS account with access keys

---

## ⏬ Instalation

1. Clone the repository:

   ```bash
   git clone https://github.com/Pavliuk-Maksym/aws_web_app.git
   ```

   ```bash
   cd aws_web_app
   ```

2. Set up a virtual Environment

   ```bash
   python3 -m venv venv
   ```

   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your key:

   ```bash
   SECRET_KEY=your_secret_app_key
   ```

5. Set up `config`

   ```bash
   [default]
   region = your_region
   output = output_format
   ```

   and `credentials`

   ```bash
   [default]
   aws_access_key_id = your_aws_access_key_id
   aws_secret_access_key = your_aws_secret_access_key
   ```

   files at the:

   - `C:\Users\<username>\.aws` on Windows
   - `~/.aws/credentials` on Linux

6. Launch the application:

   ```bash
   flask run
   ```

7. Go to `http://127.0.0.1:5000` in your browser.
