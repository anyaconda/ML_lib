#meta 2/18/2026 Sarah's EDA tricks - YData Profiling
# refer to https://docs.profiling.ydata.ai/latest/

#myNotes
#pip install ydata-profiling
# $error1: Could not find a version that satisfies the requirement ydata-profiling
# $fix1:needs a lower version of python 3.12.7 => able to install 3.13.12, after which profiling lib did get install

#$error2: 'from ydata_profiling import ProfileReport' throws an error "ModuleNotFoundError: No module named 'pkg_resources'"
# research: ydata-profiling depends on pkg_resources, which is part of the setuptools package, 
#           but it's not properly installed or accessible in your Python environment.
#           The issue is that setuptools 82.0.0 has deprecated pkg_resources. Let me install an older version that includes it
# 
#$fix2: The error was caused by setuptools 82.0.0, which removed pkg_resources. I downgraded to setuptools 69.5.1
# python -m pip install "setuptools<70"

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.DataFrame({
    "age": [25, 32, 47],
    "income": [50000, 64000, 120000],
})

profile = ProfileReport(df, title="My Report")
profile.to_file("report.html")
