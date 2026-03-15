"""Skyvern Cloud Browser SDK — minimal interface for browser session lifecycle."""

from .client import AsyncSkyvernCloud, SkyvernCloud
from .exceptions import (
    AuthenticationError,
    CloudBrowserError,
    NetworkError,
    ProviderError,
    QuotaExceededError,
    SessionNotFoundError,
    TimeoutError,
)
from .models import (
    ContextAttach,
    FingerprintConfig,
    ManagedProxyConfig,
    ProxyConfig,
    RecordingConfig,
    SessionInfo,
    ViewportConfig,
)

# Backward compatibility aliases
Skyvern = SkyvernCloud
AsyncSkyvern = AsyncSkyvernCloud

__all__ = [
    # Clients
    "SkyvernCloud",
    "AsyncSkyvernCloud",
    "Skyvern",
    "AsyncSkyvern",
    # Models
    "SessionInfo",
    "ContextAttach",
    "FingerprintConfig",
    "ViewportConfig",
    "ProxyConfig",
    "ManagedProxyConfig",
    "RecordingConfig",
    # Exceptions
    "CloudBrowserError",
    "AuthenticationError",
    "QuotaExceededError",
    "SessionNotFoundError",
    "ProviderError",
    "TimeoutError",
    "NetworkError",
]
