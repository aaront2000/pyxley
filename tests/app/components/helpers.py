from flask import make_response
from pandas import DataFrame
from flask import Blueprint, jsonify
try:
    from StringIO import StringIO
except:
    from io import StringIO

from pyxley.filters import ReactSelect

def get_download_data():
    df = DataFrame({
        "piko": ["p", "p", "a", "p"],
        "taro": ["pen", "pineapple", "apple", "pen"]
    })
    dfbuffer = StringIO()

    df.to_csv(dfbuffer, encoding="utf-8", index=False)
    dfbuffer.seek(0)

    out_ = make_response(dfbuffer.getvalue())
    out_.headers["Content-Disposition"] = "download.csv"
    out_.headers["Content-type"] = "text/csv"
    return out_

def get_api_button_data():
    return jsonify({
        "data": ["Noctis", "Gladio", "Ignis", "Prompto"]
    })

def get_react_select_data():
    opts = ["Noctis", "Gladio", "Ignis", "Prompto"]
    return jsonify(ReactSelect.format_options(opts))

def get_mod():
    mod = Blueprint("pyxley-tests", __name__)
    mod.add_url_rule("/api/api_button/", view_func=get_api_button_data)
    mod.add_url_rule("/api/react-select/", view_func=get_react_select_data)
    mod.add_url_rule("/api/download/", view_func=get_download_data)
    return mod
