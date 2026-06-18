import re
import sys
from pathlib import Path

EXIT_SUCCESS = 0
EXIT_BUILD_FAILED = 1
EXIT_USAGE_ERROR = 2
EXIT_FILE_NOT_FOUND = 3


COMPILER_MESSAGE_PATTERN = re.compile(
    r"^(?P<file>.+?):(?P<line>\d+):(?P<column>\d+):\s*(?P<level>warning|error):\s*(?P<message>.+)$",
    re.IGNORECASE,
)

TEST_FAILURE_PATTERN = re.compile(
    r"^(?P<file>.+?):(?P<line>\d+):\s*(FAILED|FAILURE):\s*(?P<message>.+)$",
    re.IGNORECASE,
)


def analyze_build_log(log_text: str) -> dict:
    errors = []
    warnings = []
    failed_tests = []

    for line in log_text.splitlines():
        compiler_match = COMPILER_MESSAGE_PATTERN.match(line.strip())

        if compiler_match:
            item = compiler_match.groupdict()
            item["line"] = int(item["line"])
            item["column"] = int(item["column"])

            if item["level"].lower() == "error":
                errors.append(item)
            elif item["level"].lower() == "warning":
                warnings.append(item)

            continue

        test_match = TEST_FAILURE_PATTERN.match(line.strip())

        if test_match:
            item = test_match.groupdict()
            item["line"] = int(item["line"])
            failed_tests.append(item)

    return {
        "errors": errors,
        "warnings": warnings,
        "failed_tests": failed_tests,
    }


def print_summary(result: dict) -> None:
    print("Build Analysis Summary")
    print("----------------------")
    print(f"Errors: {len(result['errors'])}")
    print(f"Warnings: {len(result['warnings'])}")
    print(f"Failed tests: {len(result['failed_tests'])}")
    print()

    if result["errors"]:
        print("Errors:")
        for index, error in enumerate(result["errors"], start=1):
            print(f"{index}. File: {error['file']}")
            print(f"   Line: {error['line']}, Column: {error['column']}")
            print(f"   Message: {error['message']}")
        print()

    if result["warnings"]:
        print("Warnings:")
        for index, warning in enumerate(result["warnings"], start=1):
            print(f"{index}. File: {warning['file']}")
            print(f"   Line: {warning['line']}, Column: {warning['column']}")
            print(f"   Message: {warning['message']}")
        print()

    if result["failed_tests"]:
        print("Failed tests:")
        for index, failed_test in enumerate(result["failed_tests"], start=1):
            print(f"{index}. File: {failed_test['file']}")
            print(f"   Line: {failed_test['line']}")
            print(f"   Message: {failed_test['message']}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python build_log_analyzer.py path/to/build.log")
        sys.exit(EXIT_USAGE_ERROR)

    log_path = Path(sys.argv[1])

    if not log_path.exists():
        print(f"Error: file not found: {log_path}")
        sys.exit(EXIT_FILE_NOT_FOUND)

    log_text = log_path.read_text(encoding="utf-8")
    result = analyze_build_log(log_text)
    print_summary(result)

    if result["errors"] or result["failed_tests"]:
        sys.exit(EXIT_BUILD_FAILED)

    sys.exit(EXIT_SUCCESS)

sys.exit(0)

if __name__ == "__main__":
    main()