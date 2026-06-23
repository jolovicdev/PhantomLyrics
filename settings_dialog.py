"""
Phantom Lyrics - Settings Dialog
=================================
A small QDialog that lets the user tweak overlay settings (font, opacity,
layout, auto-hide) from the system tray. Changes are saved to
~/.phantom_lyrics/config.json and applied to the overlay immediately.
"""

import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QDialogButtonBox,
    QLabel,
)

from config import Config

logger = logging.getLogger(__name__)

# Fonts offered in the settings dropdown. All are pre-installed on Windows.
_FONT_OPTIONS = [
    "Segoe UI",
    "Consolas",
    "Georgia",
]


class SettingsDialog(QDialog):
    """Modal dialog for editing Phantom Lyrics settings."""

    def __init__(self, config: Config, parent=None) -> None:
        super().__init__(parent)
        self._config = config
        self._result_config: Config | None = None

        self.setWindowTitle("Phantom Lyrics — Settings")
        self.setModal(True)
        self.setMinimumWidth(320)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        # ── Font ──
        self._font_family = QComboBox()
        self._font_family.addItems(_FONT_OPTIONS)
        # Select the current font, or fall back to the first option
        current_font = config.font_family
        idx = _FONT_OPTIONS.index(current_font) if current_font in _FONT_OPTIONS else 0
        self._font_family.setCurrentIndex(idx)
        form.addRow("Font family:", self._font_family)

        self._font_size = QSpinBox()
        self._font_size.setRange(8, 48)
        self._font_size.setValue(config.font_size)
        form.addRow("Font size (pt):", self._font_size)

        # ── Layout ──
        self._overlay_width = QSpinBox()
        self._overlay_width.setRange(200, 1200)
        self._overlay_width.setSingleStep(50)
        self._overlay_width.setValue(config.overlay_width)
        form.addRow("Overlay width (px):", self._overlay_width)

        self._max_lines = QSpinBox()
        self._max_lines.setRange(1, 10)
        self._max_lines.setValue(config.max_visible_lines)
        form.addRow("Visible lines:", self._max_lines)

        self._outline_width = QDoubleSpinBox()
        self._outline_width.setRange(0, 10)
        self._outline_width.setSingleStep(0.5)
        self._outline_width.setValue(config.outline_width_px)
        form.addRow("Outline width (px):", self._outline_width)

        # ── Opacity ──
        self._active_alpha = QSpinBox()
        self._active_alpha.setRange(0, 255)
        self._active_alpha.setValue(config.active_line_alpha)
        form.addRow("Active line opacity:", self._active_alpha)

        self._inactive_alpha = QSpinBox()
        self._inactive_alpha.setRange(0, 255)
        self._inactive_alpha.setValue(config.inactive_line_alpha)
        form.addRow("Inactive line opacity:", self._inactive_alpha)

        # ── Auto-hide ──
        self._auto_hide = QDoubleSpinBox()
        self._auto_hide.setRange(0, 120)
        self._auto_hide.setSingleStep(1)
        self._auto_hide.setSuffix(" s")
        self._auto_hide.setValue(config.auto_hide_timeout_s)
        form.addRow("Auto-hide timeout:", self._auto_hide)

        layout.addLayout(form)

        # ── Buttons ──
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._on_save)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _on_save(self) -> None:
        """Collect values into a new Config and accept the dialog."""
        c = self._config
        c.font_family = self._font_family.currentText()
        c.font_size = self._font_size.value()
        c.overlay_width = self._overlay_width.value()
        c.max_visible_lines = self._max_lines.value()
        c.outline_width_px = self._outline_width.value()
        c.active_line_alpha = self._active_alpha.value()
        c.inactive_line_alpha = self._inactive_alpha.value()
        c.auto_hide_timeout_s = self._auto_hide.value()
        c.save()
        self._result_config = c
        self.accept()

    def result_config(self) -> Config | None:
        """Return the updated Config if the user saved, else None."""
        return self._result_config
