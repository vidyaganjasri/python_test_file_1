"""
Dependency Compatibility Tests
-------------------------------
Purpose : Catch breaking changes when dependency versions are bumped.
Standard : Each dependency gets its own test class.
           Tests cover: import, version check, core API usage.
           If ANY test fails → build fails → RAG suggests fix.
"""

import pytest


# ══════════════════════════════════════════
# flask
# ══════════════════════════════════════════
class TestFlask:

    def test_import(self):
        """Flask must be importable"""
        import flask
        assert flask is not None

    def test_version_exists(self):
        """Flask must expose a version"""
        import flask
        assert hasattr(flask, "__version__")

    def test_app_creation(self):
        """Core API: Flask app must be creatable"""
        from flask import Flask
        app = Flask(__name__)
        assert app is not None

    def test_route_registration(self):
        """Core API: Routes must be registerable"""
        from flask import Flask
        app = Flask(__name__)

        @app.route("/test")
        def test_route():
            return "ok"

        assert "/test" in [r.rule for r in app.url_map.iter_rules()]

    def test_test_client(self):
        """Core API: Test client must work"""
        from flask import Flask
        app = Flask(__name__)

        @app.route("/ping")
        def ping():
            return {"status": "ok"}

        with app.test_client() as client:
            r = client.get("/ping")
            assert r.status_code == 200


# ══════════════════════════════════════════
# requests
# ══════════════════════════════════════════
class TestRequests:

    def test_import(self):
        """requests must be importable"""
        import requests
        assert requests is not None

    def test_version_exists(self):
        """requests must expose a version"""
        import requests
        assert hasattr(requests, "__version__")

    def test_get_method_exists(self):
        """Core API: get() must exist"""
        import requests
        assert callable(requests.get)

    def test_post_method_exists(self):
        """Core API: post() must exist"""
        import requests
        assert callable(requests.post)

    def test_response_object(self):
        """Core API: Response object must have status_code"""
        from requests.models import Response
        r = Response()
        assert hasattr(r, "status_code")
        assert hasattr(r, "text")
        assert hasattr(r, "json")

    def test_exceptions_exist(self):
        """Core API: Standard exceptions must exist"""
        from requests.exceptions import (
            ConnectionError,
            Timeout,
            RequestException
        )
        assert ConnectionError is not None
        assert Timeout is not None
        assert RequestException is not None


# ══════════════════════════════════════════
# numpy
# ══════════════════════════════════════════
class TestNumpy:

    def test_import(self):
        """numpy must be importable"""
        import numpy as np
        assert np is not None

    def test_version_exists(self):
        """numpy must expose a version"""
        import numpy as np
        assert hasattr(np, "__version__")

    def test_array_creation(self):
        """Core API: array() must work"""
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr is not None
        assert len(arr) == 3

    def test_basic_operations(self):
        """Core API: mean, sum, std must work"""
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert np.mean(arr) == 3.0
        assert np.sum(arr) == 15
        assert np.min(arr) == 1
        assert np.max(arr) == 5

    def test_array_dtype(self):
        """Core API: dtype must be accessible"""
        import numpy as np
        arr = np.array([1, 2, 3])
        assert arr.dtype is not None

    def test_reshape(self):
        """Core API: reshape must work"""
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5, 6])
        reshaped = arr.reshape(2, 3)
        assert reshaped.shape == (2, 3)


# ══════════════════════════════════════════
# pandas
# ══════════════════════════════════════════
class TestPandas:

    def test_import(self):
        """pandas must be importable"""
        import pandas as pd
        assert pd is not None

    def test_version_exists(self):
        """pandas must expose a version"""
        import pandas as pd
        assert hasattr(pd, "__version__")

    def test_dataframe_creation(self):
        """Core API: DataFrame must be creatable"""
        import pandas as pd
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        assert df is not None
        assert len(df) == 3

    def test_dataframe_columns(self):
        """Core API: columns must be accessible"""
        import pandas as pd
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        assert "a" in df.columns
        assert "b" in df.columns

    def test_read_csv_exists(self):
        """Core API: read_csv must exist"""
        import pandas as pd
        assert callable(pd.read_csv)

    def test_series_creation(self):
        """Core API: Series must work"""
        import pandas as pd
        s = pd.Series([1, 2, 3])
        assert len(s) == 3
        assert s.mean() == 2.0
