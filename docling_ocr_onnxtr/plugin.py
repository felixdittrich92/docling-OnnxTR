# Copyright (C) 2021-2025, Felix Dittrich.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://opensource.org/licenses/Apache-2.0> for full license details.

from .onnxtr_model import OnnxtrOcrModel


def ocr_engines():  # noqa: D103
    return {"ocr_engines": [OnnxtrOcrModel]}
