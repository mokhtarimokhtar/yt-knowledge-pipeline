from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)

    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.lstrip("/")
        if not video_id:
            raise ValueError("Invalid YouTube short URL: missing video ID")
        return video_id

    if "youtube.com" in parsed.netloc:
        query_params = parse_qs(parsed.query)
        video_ids = query_params.get("v")
        if not video_ids or not video_ids[0]:
            raise ValueError("Invalid YouTube URL: missing 'v' parameter")
        return video_ids[0]

    raise ValueError("Unsupported YouTube URL format")


def fetch_transcript_text(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return "\n".join(entry["text"] for entry in transcript)


def save_transcript(
    output_dir: str | Path,
    video_id: str,
    video_url: str,
    transcript_text: str,
) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{video_id}.txt"
    content = (
        f"VIDEO_ID: {video_id}\n"
        f"URL: {video_url}\n\n"
        "TRANSCRIPT:\n"
        f"{transcript_text}\n"
    )
    file_path.write_text(content, encoding="utf-8")
    return file_path
