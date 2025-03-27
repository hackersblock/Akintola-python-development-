# Akintola-python-development Python Development Guide and Setup Instructions
## folahack starts
get to understand python from this examples i did
and few changes to come up with a better code

##

A comprehensive guide for setting up a Python development environment with various tools and configurations.

## Table of Contents
1. [Streamlit Setup](#streamlit-installation-and-usage-guide)
2. [Virtual Environment Setup](#virtual-environment-setup)
3. [Package Management](#package-management)
4. [Project Configuration](#project-configuration)
5. [Environment Variables](#environment-variables)

## Key Features
- Streamlit installation and usage instructions
- Virtual environment (.venv) setup guide
- Requirements.txt file management
- .gitignore file configuration
- Environment variables (.env) setup
- Integration with python-dotenv package

## Prerequisites
- Python installed on your system
- pip package manager
- Terminal/Command prompt access

## Usage
Follow the step-by-step instructions in each section to set up your Python development environment. The guide includes commands and best practices for:
- Installing and running Streamlit applications
- Setting up isolated Python environments
- Managing project dependencies
- Configuring version control
- Handling environment variables securely

## Note
Remember to:
- Never commit sensitive information in .env files
- Keep your requirements.txt updated
- Activate your virtual environment before installing packages
- Use appropriate .gitignore patterns for your project


# Streamlit Installation and Usage Guide

## Installation
1. Open your terminal/command prompt
2. Install Streamlit using in your terminal using the following command:
`pip:pip install streamlit`
3. Check if Streamlit is installed by running the following command in your terminal:
`streamlit --version`
4. If Streamlit is installed, you should see the version number. If not, please check the installation steps again.
5. To run Streamlit, use the following command:streamlit run [filename].py
6. Replace [filename] with the name of your Python file.

# how to set up the .venv file for this  python virtual environment
1. Open your terminal/command prompt
2. Create a new directory for your project
3. Navigate to the directory using the following command:
`cd [directory_name]`
4. Create a new virtual environment using the following command:
`python -m venv [venv_name]`
5. Activate the virtual environment using the following command:
`source [venv_name]/bin/activate`
6. Install the required packages using the following command:
`pip install -r requirements.txt`
7. Deactivate the virtual environment using the following command:
`deactivate`

# how to set up the requirements.txt file for this python packages
1. Create a new file in your project directory
2. Name the file requirements.txt
3. Add the names of the required packages to the requirements.txt file, with each package on a new line
4. Save the requirements.txt file
5. run the following command in your terminal to install the required packages:
`pip install -r requirements.txt`

# how to set up the gitignore file for this project
1. Create a new file in your project directory
2. Name the file .gitignore
3. Add the names of the files and directories you want to ignore in the .gitignore file, with each file or directory on a new line
4. Save the .gitignore file




# how to set up the .env file for this environment variables
1. Create a new file in your project directory
2. Name the file .env
3. Add your environment variables to the .env file in the following format:
`ENV_VARIABLE_NAME=VALUE`
4. Save the .env file


# to use env in py you need to install some cool packages with pip

in your terminal run the following commands:
`pip install python-dotenv`

# to use the env in your py file you need to import the package
`import os`
`from dotenv import load_dotenv`

# to load the env file in your py file you need to run the following command
`load_dotenv()`

# Initialize the genai client
`Name of the new variable  = os.getenv('Name of the env variable in the env file')`
# for other env variables you need to do the same thing
aka name the variable and assign it to the env variable

# to get the env variable in your py file you need to run the following command
`os.getenv('variable_name')`

# to run the streamlit app in your terminal you need to run the following command
`streamlit run [filename].py`

