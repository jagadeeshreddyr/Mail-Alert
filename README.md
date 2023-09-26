# Mail-Alert

## Project Overview

The Mail-Alert project simplifies error tracking by allowing you to receive email notifications in Python when an exception is raised in your code. This eliminates the need for complex logger setups and ensures that you stay informed about critical issues in your applications.

<<<<<<< HEAD
## Project Structure
=======
3 - Main folder contains the _mail_alert.py file you can change the subject as needed and need to change the location of config file of your directory. 
>>>>>>> f4a429a2a2a61e30ec599e98693839ac6a430733

1. **Config Folder:** Contains the necessary configuration files, primarily `config.ini`, where you can customize your email settings.

2. **Main Folder:** Houses the `_mail_alert.py` file. You can modify the email subject to match your requirements and specify the location of the config file within your directory.

## Getting Started

To set up and use the Mail-Alert project, follow these steps:

1. **Clone Repository:** Clone this repository to your local machine.

2. **Configuration:** Navigate to the `config` folder and edit the `config.ini` file. Here, you can configure your email settings, such as SMTP server, port, sender email, and recipient email.

3. **Main File:** In the main folder, you'll find `_mail_alert.py`. This is the core file responsible for sending email alerts.

4. **Testing:** The main file can be used for testing purposes. You can customize it with your code logic and use it to trigger email alerts upon exceptions.

5. **Environment Setup:** Run the requirements file to create a virtual environment for your project:

   ```bash
   pip install -r requirements.txt

## Run the Code
    
    Now that your environment is activated, you can run your code. Ensure that exceptions are properly handled and trigger email alerts as needed.


