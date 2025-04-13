import sys
import logging
import os

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def count_file(file):
    """
    Count the number of lines, words, and characters in a file object.
    
    Args:
        file: A file object to read from.
    
    Returns:
        A tuple containing (lines, words, chars).
    """
    lines = words = chars = 0
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)
    return (lines, words, chars)

def get_counts(filename):
    """
    Get the counts of lines, words, and characters for a given filename.
    
    Args:
        filename: The name of the file to process.
    
    Returns:
        A tuple containing (lines, words, chars, filename) if successful, None otherwise.
    """
    try:
        with open(filename, 'r') as f:
            lines, words, chars = count_file(f)
            return (lines, words, chars, filename)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print(f"wc: {filename}: No such file or directory", file=sys.stderr)
    except PermissionError:
        logging.error(f"Permission denied: {filename}")
        print(f"wc: {filename}: Permission denied", file=sys.stderr)
    except IOError as e:
        logging.error(f"IO error occurred: {e}")
        print(f"wc: {filename}: {e}", file=sys.stderr)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"wc: {filename}: An unexpected error occurred", file=sys.stderr)
    return None

def print_counts(lines, words, chars, name):
    """
    Print the counts in a formatted manner with descriptive labels.
    
    Args:
        lines: Number of lines.
        words: Number of words.
        chars: Number of characters.
        name: The name of the file or 'stdin'.
    """
    print(f"Lines: {lines:<8} Words: {words:<8} Characters: {chars:<8} File: {name}")

def main():
    """
    Main function to handle command line arguments and process files or stdin.
    """
    filenames = sys.argv[1:]
    counts_list = []
    total_lines = total_words = total_chars = 0

    if not filenames:
        # Read from standard input
        try:
            lines, words, chars = count_file(sys.stdin)
            print_counts(lines, words, chars, 'stdin')
        except Exception as e:
            logging.error(f"Error reading from stdin: {e}")
            print(f"wc: stdin: {e}", file=sys.stderr)
        sys.exit(0)

    for filename in filenames:
        if filename == '-':
            # Handle standard input as a file
            try:
                lines, words, chars = count_file(sys.stdin)
                counts_list.append((lines, words, chars, '-'))
                total_lines += lines
                total_words += words
                total_chars += chars
            except Exception as e:
                logging.error(f"Error reading from stdin: {e}")
                print(f"wc: -: {e}", file=sys.stderr)
        else:
            counts = get_counts(filename)
            if counts is not None:
                l, w, c, name = counts
                counts_list.append((l, w, c, name))
                total_lines += l
                total_words += w
                total_chars += c

    # Print each file's counts
    for entry in counts_list:
        lines, words, chars, name = entry
        print_counts(lines, words, chars, name)

    # Print total line if more than one file processed
    if len(counts_list) > 1:
        print_counts(total_lines, total_words, total_chars, 'Total')

if __name__ == "__main__":
    main()