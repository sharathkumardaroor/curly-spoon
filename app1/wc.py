import sys

def count_file(file):
    lines = words = chars = 0
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)
    return (lines, words, chars)

def get_counts(filename):
    try:
        with open(filename, 'r') as f:
            lines, words, chars = count_file(f)
            return (lines, words, chars, filename)
    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"wc: {filename}: {e}", file=sys.stderr)
    return None

if __name__ == "__main__":
    filenames = sys.argv[1:]
    counts_list = []
    total_lines = total_words = total_chars = 0

    if not filenames:
        # Read from standard input
        try:
            lines, words, chars = count_file(sys.stdin)
            print(f"{lines:8}{words:8}{chars:8}")
        except Exception as e:
            print(f"wc: standard input: {e}", file=sys.stderr)
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
        print(f"{lines:8}{words:8}{chars:8} {name}")

    # Print total line if more than one file processed
    if len(counts_list) > 1:
        print(f"{total_lines:8}{total_words:8}{total_chars:8} total")