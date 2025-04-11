#!/usr/bin/env python3
import sys


def split_diff_to_files(
    diff_text, before_filename="before.txt", after_filename="after.txt"
):
    """
    Splits a unified diff text into "before" and "after" versions and saves
    them to separate files.

    Args:
        diff_text: A string containing the unified diff output.
        before_filename: The filename to save the "before" version to.
        after_filename: The filename to save the "after" version to.

    Returns:
        A tuple containing the paths to the saved files (before_file_path, after_file_path).
    """
    before_extension = None
    after_extension = None

    # Extract file extensions if present
    for line in diff_text.splitlines():
        if line.startswith("--- a/"):
            parts = line.split(".")
            if len(parts) > 1:
                before_extension = parts[-1].strip()
        elif line.startswith("+++ b/"):
            parts = line.split(".")
            if len(parts) > 1:
                after_extension = parts[-1].strip()

    # Apply extensions if found
    if before_extension:
        before_filename = f"before.{before_extension}"
    if after_extension:
        after_filename = f"after.{after_extension}"

    # Process the diff using a more reliable approach
    lines = diff_text.splitlines()

    # Skip header lines
    i = 0
    while i < len(lines) and not lines[i].startswith("@@"):
        i += 1

    if i >= len(lines):
        print("No hunks found in diff")
        return None, None

    # Initialize the before and after content with empty strings
    before_content = []
    after_content = []

    # Process each line after the header
    while i < len(lines):
        line = lines[i]

        if line.startswith("@@"):
            # Skip hunk headers for before content
            after_content.append(line)
        elif line.startswith("-"):
            # Remove the "-" prefix for before content
            before_content.append(line[1:])
        elif line.startswith("+"):
            # Remove the "+" prefix for after content
            after_content.append(line[1:])
        elif line.startswith(" "):
            # Context lines go in both files, without the space
            before_content.append(line[1:])
            after_content.append(line[1:])
        else:
            # Other lines (index, etc.) go in both files
            before_content.append(line)
            after_content.append(line)

        i += 1

    # Write to files
    try:
        with open(before_filename, "w") as f:
            f.write("\n".join(before_content))
        with open(after_filename, "w") as f:
            f.write("\n".join(after_content))
        return before_filename, after_filename
    except Exception as e:
        print(f"Error writing to file: {e}")
        return None, None


def read_diff_from_file(filename):
    """Reads the diff text from a file."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None


def read_diff_from_stdin():
    """Reads the diff text from standard input."""
    return sys.stdin.read()


def main():
    # Determine input source (file or stdin)
    if len(sys.argv) > 1:
        input_source = "file"
        diff_filename = sys.argv[1]  # First argument is the filename
    else:
        input_source = "stdin"

    # Read diff text
    if input_source == "file":
        diff_text = read_diff_from_file(diff_filename)
    else:
        diff_text = read_diff_from_stdin()

    if not diff_text:
        print("No diff text received. Exiting.")
        return

    before_file, after_file = split_diff_to_files(diff_text)

    if before_file and after_file:
        print(f"Before version saved to: {before_file}")
        print(f"After version saved to: {after_file}")
    else:
        print("Failed to split and save the diff.")


if __name__ == "__main__":
    main()
