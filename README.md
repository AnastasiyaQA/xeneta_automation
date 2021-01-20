# xeneta_automation

Xeneta_automation is a project with realization of test task for Xeneta Test Automation Engineer position.

Please, visit the below link to read a full Test Automation Task:
https://github.com/xeneta/test-automation-task

Accortding to the task, the list of test cases is represented in Google Sheets. There are two tabs with test cases for both pages. 
The column 'Include in Automation?' contains marks for test cases, implemented in Automation Framework.
https://docs.google.com/spreadsheets/d/1Ocbi64agpmkASymGNPHcQcFhcUU40sP7Y1FQWZLXgug/edit?usp=sharing


## To run the project please do the following (for Windows OS):

1. Clone repository
2. Create virtual environment for the project.
3. Install all reqirements with the following command:
```bash
  pip install -r requirements.txt
```
4. Download Chromedriver.exe which is compatible with your Chrome Browser version.
5. Go to Environmental Variables on your computer and add PATH = [path to downloaded ChromeDriver]
6. Open 'Terminal' in Pycharm run test cases with simple command: 

```bash
pytest
```

Note: to run one specific test case use the command: 
```bash
pytest -m [test_case_mark]
```

e.g.:
```bash
pytest -m test_demo_page_18
```

To run test cases in multiple threads, pytest -n[number of threads], e.g.:
```bash
pytest -n4
```




