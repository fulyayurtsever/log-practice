from log_analyzer import analyze_warnings, analyze_errors, analyze_backup


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


def test_backup_counts_success_and_fail(tmp_path):
    log_file = tmp_path / "backup.log"
    log_file.write_text(
        "2026-05-09 10:00 SUCCESS: db backup\n"
        "2026-05-09 11:00 FAIL: file backup\n"
        "2026-05-09 12:00 SUCCESS: config backup\n"
    )
    assert analyze_backup(str(log_file)) == {"success": 2, "fail": 1}


def test_backup_empty_file_returns_zero_counts(tmp_path):
    log_file = tmp_path / "backup.log"
    log_file.write_text("")
    assert analyze_backup(str(log_file)) == {"success": 0, "fail": 0}
