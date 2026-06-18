import build_log_analyzer


def test_detects_errors():
    log = "src/main.cpp:12: error: undefined reference"
    result = build_log_analyzer.analyze_build_log(log)
    assert len(result["errors"]) == 1


def test_detects_warnings():
    log = "src/main.cpp:42: warning: unused variable"
    result = build_log_analyzer.analyze_build_log(log)
    assert len(result["warnings"]) == 1


def test_detects_failed_tests():
    log = "tests/test_controller.cpp:21: FAILED: expected 42 but got 0"
    result = build_log_analyzer.analyze_build_log(log)
    assert len(result["failed_tests"]) == 1


def test_empty_log_returns_empty_results():
    result = build_log_analyzer.analyze_build_log("")
    assert result["errors"] == []
    assert result["warnings"] == []
    assert result["failed_tests"] == []