from asyncio import set_event_loop
from enum import verify
from .models import ModerationFlag

def run_moderation_checks(extension) -> list:
    """run automated checked on a submitted extension.
    Returns a list of ModerationFlag objects
    """
    flags = []

    # File size is too large
    if extension.extension_file.size > 10 * 1024 * 1024:
        flags.append(
                ModerationFlag(
                    extension=extension,
                    check_name="file_size_check",
                    severity="warning",
                    message=f"Large file size: {extension.extension_file.size / (1024*1024):.2f}MB",
                    )
                )

    # Description length is too long
    if len(extension.description) < 50:
        flags.append(
                ModerationFlag(
                    extension=extension,
                    check_name="description length",
                    severity="info",
                    message=f"Description is too short. Consider adding more details.",
                    )
                )


    if not any(char.isdigit() for char in extension.version):
        flags.append(
            ModerationFlag(
                extension=extension,
                check_name="version_format",
                severity="warning",
                message="Version should contain numbers (e.g., 1.0.0)",
            )
        )

    return flags
