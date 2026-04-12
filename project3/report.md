Student’s Name: Eldon Wu
Professor’s Name: Huixin Wu
Class Number: ET721
Date: April 10, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Initially, the test coverage of the project was quite low. Only a few basic unit tests were provided, and several important methods such as average quantity, most common fruit, and validation edge cases were not tested. After adding additional unit tests, the test coverage significantly improved. I was able to cover nearly all the core functionality in the Fruit and FruitMetrics classes. In total, I ended up with 8 unit tests in the test_models.py file, ensuring that both normal behavior and edge cases were handled correctly.

## Untested Code: Effects

Without tests, it was difficult to fully understand all features and use cases of the code. I had to manually read through each function and try different inputs to see how the system behaved. Testing the API manually was time-consuming and not always reliable, since it is easy to miss edge cases. Having few tests made it harder to trust the code, and I was less confident about how the API would behave in unexpected situations.

## Adding Tests

To add more tests, I analyzed the existing code and identified missing functionality that needed validation. I focused on testing both normal cases and edge cases, such as invalid input values. A unit test focuses on testing small pieces of logic, like individual functions or methods, while an API test focuses on testing endpoints and how the system behaves as a whole. Both types of tests are important because unit tests ensure correctness of logic, while API tests verify real-world usage.

## Automation

It allows me to quickly verify that all parts of the application are working correctly after making changes. Automated tests reduces errors and saves time compared to manual testing. They also make it easier to maintain and scale the project.

## New Features

When adding new features, having tests already in place made the process much easier. I could quickly check if my changes broke any existing functionality. This gave me a sense of security and confidence when modifying the code.

## Future

From this experience, I learned the importance of writing tests early in development. In the future, I hope to always include testing as part of my workflow. It helps improve code quality, reliability, and overall confidence in the software.
