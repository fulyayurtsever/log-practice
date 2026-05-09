def analyze_warnings(filepath="app.log"):
    count = 0
    with open(filepath) as f:
        for line in f:
            if "WARNING" in line:
                count += 1
    return count <= 5


def analyze_errors(filepath="app.log"):
    count = 0
    with open(filepath) as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    return count


def analyze_backup(filepath="backup.log"):
    counts = {"success": 0, "fail": 0}
    with open(filepath) as f:
        for line in f:
            if "SUCCESS" in line:
                counts["success"] += 1
            elif "FAIL" in line:
                counts["fail"] += 1
    return counts


def analyze_log(filepath="app.log"):
    sayilar = {"WARNING": 0, "ERROR": 0, "CRITICAL": 0}
    
    with open(filepath) as f:
        for line in f:
            if "WARNING" in line:
                sayilar["WARNING"] += 1
            elif "ERROR" in line:
                sayilar["ERROR"] += 1
            elif "CRITICAL" in line:
                sayilar["CRITICAL"] += 1
    
    if sayilar["WARNING"] > 5 or sayilar["ERROR"] > 0 or sayilar["CRITICAL"] > 0:
        sayilar["status"] = "FAIL"
    else:
        sayilar["status"] = "OK"
    
    return sayilar