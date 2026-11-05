# SPDX-License-Identifier: MIT
# Copyright (C) 2024-2025, Advanced Micro Devices, Inc. All rights reserved.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RequestOutput:
    """Output structure passed to stream callback."""

    request_id: int
    output_tokens: List[int]
    finished: bool
    finish_reason: Optional[str] = None
    kv_transfer_params_output: Optional[Dict[str, Any]] = None
    num_cached_tokens: int = 0
    # The request's prompt prefill was dispatched to the end
    # (`Sequence.prefill_dispatched`). Any output with a sampled token implies
    # it; a terminal output without one (an error, `max_tokens <= 0`) may not.
    prefill_complete: bool = True
