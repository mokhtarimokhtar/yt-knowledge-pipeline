from __future__ import annotations

import sys

from yt_pipeline.transcript import (
    extract_video_id,
    fetch_transcript_text,
    save_transcript,
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/get_transcript.py <youtube_url>")
        return 1

    video_url = sys.argv[1]

    try:
        video_id = extract_video_id(video_url)
        transcript_text = fetch_transcript_text(video_id)
        output_file = save_transcript(
            output_dir="outputs",
            video_id=video_id,
            video_url=video_url,
            transcript_text=transcript_text,
        )
    except Exception as exc:
        print(f"Error: {exc}")
        return 1

    print(f"Transcript saved to: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
