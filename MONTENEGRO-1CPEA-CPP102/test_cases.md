# Test Cases – Simulated Device Monitoring and Alert System

tested by: Montenegro, Angelica Verone O.        Date: October 12, 2026

ecording valid initial temperature readings. Rejecting zero or negative numbers as the number of initial readings. Rejecting temperatures outside the range of 0 to 100. Displaying all stored temperature readings. Recording a new temperature. Classifying temperatures as NORMAL, WARNING, or CRITICAL. Inspecting sensor statuses. Calculating the total and average temperatures. Generating the system performance report and determining the overall condition. Rejecting invalid menu choices and shutting down the program correctly. Full details are provided in test_cases.md.

Known Limitations Temperature readings are lost when the program closes because the data is not saved to a file or database. The program uses simulated temperature readings instead of collecting data from actual devices. The system accepts only whole-number temperature readings from 0 to 100. The program does not provide real-time monitoring or automatic temperature collection. The system operates through a text-based interface rather than a graphical user interface. Reflection The hardest part of developing this project was implementing the temperature classification system and ensuring that every reading was assigned the correct status. I also needed to make sure that the numerical summary correctly calculated the total, average, lowest, and highest temperatures. Input validation was important because it prevented invalid temperature values and menu choices from being accepted. Through this project, I learned how to use conditional statements, loops, functions, and lists to organize a Python program. In the future, I would improve the system by saving temperature readings to a file and adding real-time monitoring features and a graphical user interface.

Before submitting:

Replace the test counts with your actual results after running your 10 tests.

Create or update test_cases.md with the results of those tests.

Make sure the filename in your instructions (device_monitor.py) matches the name of your actual Python file.

Your program's title is Smart Temperature Control, while your project title is Simulated Device Monitoring and Alert System. You can keep both, but using the same title throughout would make the submission more consistent.