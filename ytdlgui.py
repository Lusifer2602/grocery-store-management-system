import os
import sys
import threading
from pathlib import Path
import customtkinter as ctk
import yt_dlp
## pip install yt-dlp, customtkinter and ffmpeg before running
## pip --upgrade yt-dlp to upgrade the yt-dlp version incase download breaks

# --- Monochromatic Theme Configuration ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

COLOR_BG = "#121212"
COLOR_CARD = "#1E1E1E"
COLOR_CARD_BORDER = "#2C2C2C"
COLOR_TEXT_PRIMARY = "#FFFFFF"
COLOR_TEXT_MUTED = "#8E8E8E"
COLOR_INPUT_BG = "#181818"
COLOR_BTN_PRIMARY = "#E0E0E0"
COLOR_BTN_PRIMARY_HOVER = "#FFFFFF"
COLOR_BTN_TEXT = "#121212"
COLOR_BTN_SECONDARY = "#262626"
COLOR_BTN_SECONDARY_HOVER = "#333333"


class MediaDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MEDIA DOWNLOADER // YT-DLP")
        self.geometry("640x700")
        self.minsize(560, 600)
        self.configure(fg_color=COLOR_BG)

        # Default path: ~/Downloads
        self.download_dir = Path.home() / "Downloads"
        if not self.download_dir.exists():
            self.download_dir = Path.home()

        self.is_downloading = False
        self._build_ui()

    def _build_ui(self):
        # Container
        self.main_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color="#333333",
            scrollbar_button_hover_color="#444444"
        )
        self.main_frame.pack(fill="both", expand=True, padx=24, pady=24)

        # Header
        header = ctk.CTkLabel(
            self.main_frame,
            text="MEDIA DOWNLOADER",
            font=ctk.CTkFont(family="Courier", size=20, weight="bold"),
            text_color=COLOR_TEXT_PRIMARY
        )
        header.pack(anchor="w", pady=(0, 4))

        sub_header = ctk.CTkLabel(
            self.main_frame,
            text="yt-dlp core • minimalist pipeline",
            font=ctk.CTkFont(family="Courier", size=12),
            text_color=COLOR_TEXT_MUTED
        )
        sub_header.pack(anchor="w", pady=(0, 16))

        # URL Input Section
        self.url_label = ctk.CTkLabel(
            self.main_frame,
            text="SOURCE URL",
            font=ctk.CTkFont(family="Courier", size=11, weight="bold"),
            text_color=COLOR_TEXT_MUTED
        )
        self.url_label.pack(anchor="w", pady=(4, 2))

        self.url_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Paste YouTube or media link here...",
            fg_color=COLOR_INPUT_BG,
            border_color=COLOR_CARD_BORDER,
            text_color=COLOR_TEXT_PRIMARY,
            placeholder_text_color="#555555",
            height=40,
            corner_radius=6
        )
        self.url_entry.pack(fill="x", pady=(0, 12))

        # Download Path Frame
        path_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=COLOR_CARD,
            border_width=1,
            border_color=COLOR_CARD_BORDER,
            corner_radius=6
        )
        path_frame.pack(fill="x", pady=(0, 12), ipady=6)

        path_title = ctk.CTkLabel(
            path_frame,
            text="TARGET DIRECTORY",
            font=ctk.CTkFont(family="Courier", size=10, weight="bold"),
            text_color=COLOR_TEXT_MUTED
        )
        path_title.pack(anchor="w", padx=12, pady=(4, 2))

        path_inner = ctk.CTkFrame(path_frame, fg_color="transparent")
        path_inner.pack(fill="x", padx=12, pady=(0, 4))

        self.path_display = ctk.CTkLabel(
            path_inner,
            text=str(self.download_dir),
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXT_PRIMARY,
            anchor="w"
        )
        self.path_display.pack(side="left", fill="x", expand=True)

        browse_btn = ctk.CTkButton(
            path_inner,
            text="BROWSE",
            width=70,
            height=28,
            fg_color=COLOR_BTN_SECONDARY,
            hover_color=COLOR_BTN_SECONDARY_HOVER,
            text_color=COLOR_TEXT_PRIMARY,
            font=ctk.CTkFont(family="Courier", size=11, weight="bold"),
            corner_radius=4,
            command=self._select_directory
        )
        browse_btn.pack(side="right")

        # Advanced Toggle
        self.adv_switch = ctk.CTkSwitch(
            self.main_frame,
            text="Show Advanced Configuration",
            font=ctk.CTkFont(family="Courier", size=12),
            text_color=COLOR_TEXT_PRIMARY,
            progress_color="#666666",
            command=self._toggle_advanced
        )
        self.adv_switch.pack(anchor="w", pady=(6, 12))

        # Advanced Options Container (Hidden by default)
        self.adv_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=COLOR_CARD,
            border_width=1,
            border_color=COLOR_CARD_BORDER,
            corner_radius=6
        )

        # Mode Selection: Video vs Audio-Only
        ctk.CTkLabel(
            self.adv_frame,
            text="MEDIA STREAM",
            font=ctk.CTkFont(family="Courier", size=10, weight="bold"),
            text_color=COLOR_TEXT_MUTED
        ).pack(anchor="w", padx=12, pady=(10, 2))

        self.mode_selector = ctk.CTkSegmentedButton(
            self.adv_frame,
            values=["Video + Audio", "Audio Only"],
            selected_color="#444444",
            selected_hover_color="#555555",
            unselected_color="#181818",
            unselected_hover_color="#222222",
            text_color=COLOR_TEXT_PRIMARY,
            command=self._on_mode_change
        )
        self.mode_selector.set("Video + Audio")
        self.mode_selector.pack(fill="x", padx=12, pady=(0, 8))

        # Format & Quality Selectors
        selectors_grid = ctk.CTkFrame(self.adv_frame, fg_color="transparent")
        selectors_grid.pack(fill="x", padx=12, pady=(0, 8))

        # Format Dropdown
        fmt_col = ctk.CTkFrame(selectors_grid, fg_color="transparent")
        fmt_col.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.fmt_label = ctk.CTkLabel(
            fmt_col,
            text="CONTAINER FORMAT",
            font=ctk.CTkFont(family="Courier", size=10, weight="bold"),
            text_color=COLOR_TEXT_MUTED
        )
        self.fmt_label.pack(anchor="w")

        self.format_menu = ctk.CTkOptionMenu(
            fmt_col,
            values=["mp4", "mkv", "webm"],
            fg_color=COLOR_INPUT_BG,
            button_color="#2C2C2C",
            button_hover_color="#3D3D3D",
            text_color=COLOR_TEXT_PRIMARY,
            dropdown_fg_color=COLOR_CARD,
            dropdown_text_color=COLOR_TEXT_PRIMARY
        )
        self.format_menu.pack(fill="x", pady=(2, 0))

        # Resolution / Bitrate Dropdown
        res_col = ctk.CTkFrame(selectors_grid, fg_color="transparent")
        res_col.pack(side="right", fill="x", expand=True, padx=(6, 0))

        self.quality_label = ctk.CTkLabel(
            res_col,
            text="MAX RESOLUTION",
            font=ctk.CTkFont(family="Courier", size=10, weight="bold"),
            text_color=COLOR_TEXT_MUTED
        )
        self.quality_label.pack(anchor="w")

        self.quality_menu = ctk.CTkOptionMenu(
            res_col,
            values=["Best Available", "2160p (4K)", "1440p (2K)", "1080p", "720p", "480p"],
            fg_color=COLOR_INPUT_BG,
            button_color="#2C2C2C",
            button_hover_color="#3D3D3D",
            text_color=COLOR_TEXT_PRIMARY,
            dropdown_fg_color=COLOR_CARD,
            dropdown_text_color=COLOR_TEXT_PRIMARY
        )
        self.quality_menu.pack(fill="x", pady=(2, 0))

        # Extra Checkboxes
        self.embed_thumb = ctk.CTkCheckBox(
            self.adv_frame,
            text="Embed metadata & thumbnail (via FFmpeg)",
            font=ctk.CTkFont(size=12),
            text_color=COLOR_TEXT_PRIMARY,
            checkmark_color=COLOR_TEXT_PRIMARY,
            fg_color="#333333",
            border_color="#555555"
        )
        self.embed_thumb.pack(anchor="w", padx=12, pady=(4, 12))

        # Download Action Button
        self.download_btn = ctk.CTkButton(
            self.main_frame,
            text="DOWNLOAD MEDIA",
            height=44,
            fg_color=COLOR_BTN_PRIMARY,
            hover_color=COLOR_BTN_PRIMARY_HOVER,
            text_color=COLOR_BTN_TEXT,
            font=ctk.CTkFont(family="Courier", size=13, weight="bold"),
            corner_radius=6,
            command=self._start_download_thread
        )
        self.download_btn.pack(fill="x", pady=(12, 12))

        # Progress / Status Section
        self.progress_bar = ctk.CTkProgressBar(
            self.main_frame,
            height=4,
            corner_radius=2,
            fg_color="#222222",
            progress_color=COLOR_TEXT_PRIMARY
        )
        self.progress_bar.set(0)
        self.progress_bar.pack(fill="x", pady=(0, 6))

        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="READY",
            font=ctk.CTkFont(family="Courier", size=11),
            text_color=COLOR_TEXT_MUTED
        )
        self.status_label.pack(anchor="w")

    def _select_directory(self):
        selected = ctk.filedialog.askdirectory(initialdir=str(self.download_dir))
        if selected:
            self.download_dir = Path(selected)
            self.path_display.configure(text=str(self.download_dir))

    def _toggle_advanced(self):
        if self.adv_switch.get() == 1:
            self.adv_frame.pack(fill="x", pady=(0, 12), before=self.download_btn)
        else:
            self.adv_frame.pack_forget()

    def _on_mode_change(self, choice):
        if choice == "Audio Only":
            self.fmt_label.configure(text="AUDIO ENCODING")
            self.format_menu.configure(values=["mp3", "flac", "wav", "m4a"])
            self.format_menu.set("mp3")

            self.quality_label.configure(text="AUDIO QUALITY")
            self.quality_menu.configure(values=["320 kbps", "256 kbps", "192 kbps", "128 kbps"])
            self.quality_menu.set("320 kbps")
        else:
            self.fmt_label.configure(text="CONTAINER FORMAT")
            self.format_menu.configure(values=["mp4", "mkv", "webm"])
            self.format_menu.set("mp4")

            self.quality_label.configure(text="MAX RESOLUTION")
            self.quality_menu.configure(values=["Best Available", "2160p (4K)", "1440p (2K)", "1080p", "720p", "480p"])
            self.quality_menu.set("Best Available")

    def _progress_hook(self, d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            downloaded = d.get("downloaded_bytes", 0)
            if total > 0:
                fraction = min(max(downloaded / total, 0.0), 1.0)
                self.progress_bar.set(fraction)
                speed = d.get("_speed_str", "N/A")
                eta = d.get("_eta_str", "N/A")
                self.status_label.configure(
                    text=f"FETCHING: {int(fraction * 100)}% | SPEED: {speed} | ETA: {eta}"
                )
        elif d["status"] == "finished":
            self.progress_bar.set(1.0)
            self.status_label.configure(text="PROCESSING VIA FFMPEG...")

    def _start_download_thread(self):
        url = self.url_entry.get().strip()
        if not url:
            self.status_label.configure(text="ERROR: No URL provided.")
            return

        if self.is_downloading:
            return

        self.is_downloading = True
        self.download_btn.configure(state="disabled", text="PROCESSING...")
        self.progress_bar.set(0)
        self.status_label.configure(text="INITIALIZING PIPELINE...")

        thread = threading.Thread(target=self._run_ytdlp, args=(url,), daemon=True)
        thread.start()

    def _build_options(self):
        outtmpl = str(self.download_dir / "%(title)s.%(ext)s")
        opts = {
            "outtmpl": outtmpl,
            "progress_hooks": [self._progress_hook],
            "quiet": True,
            "no_warnings": True
        }

        # Default Mode (Best single stream or auto-mux)
        if self.adv_switch.get() == 0:
            opts["format"] = "bestvideo*+bestaudio/best"
            opts["merge_output_format"] = "mp4"
            return opts

        # Advanced Mode
        is_audio = self.mode_selector.get() == "Audio Only"
        selected_fmt = self.format_menu.get()

        if is_audio:
            bitrate = self.quality_menu.get().split(" ")[0]
            opts["format"] = "bestaudio/best"
            opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": selected_fmt,
                    "preferredquality": bitrate,
                }
            ]
        else:
            quality_map = {
                "2160p (4K)": "2160",
                "1440p (2K)": "1440",
                "1080p": "1080",
                "720p": "720",
                "480p": "480"
            }
            res = self.quality_menu.get()
            if res in quality_map:
                res_h = quality_map[res]
                opts["format"] = f"bestvideo[height<={res_h}]+bestaudio/best[height<={res_h}]"
            else:
                opts["format"] = "bestvideo+bestaudio/best"

            opts["merge_output_format"] = selected_fmt

        if self.embed_thumb.get() == 1:
            if "postprocessors" not in opts:
                opts["postprocessors"] = []
            opts["writethumbnail"] = True
            opts["postprocessors"].extend([
                {"key": "FFmpegMetadata"},
                {"key": "EmbedThumbnail"}
            ])

        return opts

    def _run_ytdlp(self, url):
        opts = self._build_options()
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            self.after(0, self._on_success)
        except Exception as e:
            self.after(0, lambda err=str(e): self._on_error(err))

    def _on_success(self):
        self.is_downloading = False
        self.progress_bar.set(1.0)
        self.status_label.configure(text="COMPLETE: Saved to Downloads folder.")
        self.download_btn.configure(state="normal", text="DOWNLOAD MEDIA")

    def _on_error(self, err_msg):
        self.is_downloading = False
        self.progress_bar.set(0)
        # Display short error format
        summary = err_msg.split(":")[-1].strip() if ":" in err_msg else err_msg
        self.status_label.configure(text=f"FAILED: {summary[:50]}")
        self.download_btn.configure(state="normal", text="DOWNLOAD MEDIA")


if __name__ == "__main__":
    app = MediaDownloaderApp()
    app.mainloop()