pytest -s -v -m "sanity" --html=./Reports/report.html testCases/test_login.py --browser chrome
rem pytest -s -v -m "regression" --html=Reports\report.html testCases/test_login.py --browser chrome