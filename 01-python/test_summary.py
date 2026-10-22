
# Day 3: Test execution summary

test_results = ["Pass", "Pass", "Fail"]

passed = 0
failed = 0

for result in test_results:
    if result == "Pass":
        passed = passed + 1
    else:
        failed = failed + 1

print("Total tests:", len(test_results))
print("Passed:", passed)
print("Failed:", failed)
