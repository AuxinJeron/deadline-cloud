# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

import sys
import pytest

# PySide6-essentials requires glibc 2.28+ which is not available in integration test env
pytest.mark.skipif(
    sys.platform.startswith("linux"),
    reason="Skipping tests on Linux",
)
