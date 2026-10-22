
# Day 3: Test execution summary

test_results = ["Pass", "Fail", "Skip", "Pass", "Skip"]

passed = 0
failed = 0
skipped = 0

for result in test_results:
    if result == "Pass":
        passed = passed + 1
    elif result == "Fail":
        failed = failed + 1
    else:
        skipped = skipped + 1
        
print("Total tests:", len(test_results))
print("Passed:", passed)
print("Failed:", failed)
print("Skipped:", skipped)
