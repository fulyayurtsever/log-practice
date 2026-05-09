from log_analyzer import analyze_warnings


def test_more_than_5_warnings_returns_false(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(["WARNING: something wrong"] * 6) + "\n")
    assert analyze_warnings(str(log_file)) == False


def test_3_warnings_returns_true(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(["WARNING: something wrong"] * 3) + "\n")
    assert analyze_warnings(str(log_file)) == True
