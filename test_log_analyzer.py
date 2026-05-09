from log_analyzer import analyze_warnings, analyze_errors


def test_more_than_5_warnings_returns_false(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(["WARNING: something wrong"] * 6) + "\n")
    assert analyze_warnings(str(log_file)) == False


def test_3_warnings_returns_true(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(["WARNING: something wrong"] * 3) + "\n")
    assert analyze_warnings(str(log_file)) == True


def test_3_errors_returns_3(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(["ERROR: something failed"] * 3) + "\n")
    assert analyze_errors(str(log_file)) == 3


def test_0_errors_returns_0(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("INFO: all good\nWARNING: minor issue\n")
    assert analyze_errors(str(log_file)) == 0
