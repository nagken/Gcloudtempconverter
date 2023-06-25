Temperature Converter
Welcome to the Temperature Converter repository! This guide will walk you through the steps to run the CI/CD pipeline and obtain the deployment URL for testing the project.

Prerequisites
Before getting started, make sure you have the following:

GitHub account
Docker installed
Google Cloud SDK installed
Google Cloud project created
CI/CD Pipeline
To run the CI/CD pipeline and obtain the deployment URL, follow these steps:

Fork the repository:

Go to the project repository on GitHub: https://github.com/nagken/Gcloudtempconverter
Click on the "Fork" button in the top right corner to create a copy of the repository under your GitHub account.
Set up Secrets (Optional):

Go to your forked repository on GitHub.
Navigate to the "Settings" tab.
In the left sidebar, click on "Secrets".
Click on "New repository secret" to create a new secret.
Add a secret with the following details:
Name: GCP_SERVICE_ACCOUNT_KEY
Value: Paste your Google Cloud service account key JSON content.
Update Workflow Configuration (Optional):

In the repository, navigate to the .github/workflows directory.
Open the main.yaml file.
Replace the placeholder values in the workflow file:
Replace PROJECT_ID with your Google Cloud project ID.
Save the file.
Trigger the Workflow:

Commit and push your changes to the repository.
Go to the "Actions" tab in your repository.
You will see the CI/CD workflow running. Wait for it to complete.
Deployment URL:

Once the workflow has completed successfully, go to the workflow run.
In the "Deploy to Cloud Run" step, find the output logs.
Look for the line starting with "Cloud Run Deployment URL:". The URL will be provided in the logs.
Alternatively, if you want to use your own secret key and GCP project ID:

Insert your secret key JSON content as a secret with the name GCP_SERVICE_ACCOUNT_KEY in the repository settings.
Update the workflow configuration file (main.yaml) and replace PROJECT_ID with your GCP project ID.
Commit and push the changes to the repository.
Follow the previous steps to trigger the workflow and obtain the deployment URL.
Troubleshooting
If you encounter any issues during the CI/CD pipeline execution or have questions, please feel free to reach out for support.

Contributing
I welcome contributions to this project. If you would like to contribute, please follow the guidelines mentioned in the project repository.

License
This project is licensed under the MIT License. For more details, see the LICENSE file.

Contact
If you have any questions or need assistance, please feel free to contact me at nagversion@gmail.com.

That's it! Customize this template to fit your project's specific instructions and details, and you'll have a comprehensive README.md file to guide users in running the CI/CD pipeline and obtaining the deployment URL for testing your project on GitHub.

future dev:
Add validation on the numerical value input field to ensure it accepts only valid numbers.
Implement server-side validation to handle edge cases and prevent malicious input.
Improve the user interface by adding error messages or feedback for invalid inputs or conversion errors.
Implement unit tests to ensure the accuracy and reliability of the temperature conversion logic.
Add more temperature unit options to provide a wider range of conversion choices.
Implement a responsive design to ensure the application is mobile-friendly.
Implement a history feature to track and display previous conversions.
Add a clear button to reset the form and allow users to start over.
Implement localization to support multiple languages and region-specific units.
Optimize the deployment process by automating the creation of Cloud Run services and handling any necessary environment configurations.
These development tasks can be prioritized based on your specific goals and requirements for the Temperature Converter project.
