# MonefyApptest-Android

This is a framework repository for automating the Monefy Android application using Python with pytest and the Page Object Model (POM) framework.

**Author:** Anam Siddiquee

## Pre-requisites

1. Download and setup Python 3 from: https://www.python.org/downloads/
2. Install Appium 2 using the official documentation: https://github.com/appium/appium
3. Install UiAutomator 2 plugin with Appium 2 drivers

## Setup the framework and requirements and execute tests

1. Navigate to the project directory:
   ```bash
   cd monefy-Appium
   ```
2. (Optional) Select the Python interpreter in your IDE preferences and create a virtual environment.
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run tests using pytest. Use the option `--device_name` to specify the Android simulator or device name. For example:
   ```bash
   pytest tests --alluredir=allure-results --device_name "<Your simulator name>"
   ```
6. Generate and view the Allure report:
   ```bash
   allure serve allure-results
   ```

## Project Structure

- `base` - Contains all the Appium drivers, common functions, and worker functions.
- `resources` - Contains APK files and URL configurations used throughout the project.
- `pages` - Contains all the page classes and their methods implementing the POM.
- `tests` - Contains the test classes to be executed.
- `allure-results` - Folder to save Allure reports.
  - Run `allure serve` to view the Allure report on localhost.
  - Run `allure generate` to generate an Allure report saved under `/allure-report`.
- `conftest.py` - Contains pytest fixtures and methods.
- `requirements.txt` - Contains all Python dependencies.

## Sample Allure Report

Allure is a flexible, lightweight multi-language test report tool that shows a clear representation of what has been tested in a neat web report form.

After running your tests with the `--alluredir` option, you can generate and serve the report locally:

```bash
allure serve allure-results
```

This command will start a local web server and open the test report in your default browser, showing detailed test execution results, including passed, failed, and skipped tests, along with logs and screenshots if configured.

For more information, visit the [Allure Framework website](https://docs.qameta.io/allure/).
