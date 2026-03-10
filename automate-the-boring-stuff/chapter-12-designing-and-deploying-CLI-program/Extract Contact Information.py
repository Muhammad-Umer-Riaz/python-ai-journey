# Extract Contact Information from Large Documents Using Regular Expressions and Pyperclip 
import pyperclip, re

# Create phone number regex.
phone_re = re.compile(r'''(
    # Pattern 1: International format (+358...)
    (
        \+358          # Country code
        [-\s]?         # Optional hyphen or space
        [1-9]          # First digit of prefix (not zero)
        \d{0,2}        # 0-2 more digits for prefix
        [-\s]?         # Optional hyphen or space
        \d{3,4}        # First part of number
        [-\s]?         # Optional hyphen or space
        \d{3,5}        # Second part of number
    )
    |
    # Pattern 2: Mobile numbers starting with 0
    (
        0              # Leading zero
        (
            4[05]?\d?  # 04, 040, 045, 0457
            |          # OR
            50?        # 05, 050
        )
        [-\s]?         # Optional hyphen or space
        \d{3,5}        # 3-5 digits
        [-\s]?         # Optional hyphen or space
        \d{2,5}        # 2-5 digits
    )
    |
    # Pattern 3: Other numbers starting with 0
    (
        0              # Leading zero
        [1-9]\d{0,2}   # Area code (1-3 digits)
        [-\s]?         # Optional hyphen or space
        \d{3,6}        # 3-6 digits for local number
        (
            [-\s]?      # Optional separator
            \d{1,4}     # Optional extension
        )?
    )
)''', re.VERBOSE | re.MULTILINE)

# Create email regex.
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # Username
    @  # @ symbol
    [a-zA-Z0-9.-]+  # Domain name
    (\.[a-zA-Z]{2,4})  # Dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for group in phone_re.findall(text):
    phone_num = ' '.join([group[1], group[2], group[3]])
    matches.append(phone_num)
for group in email_re.findall(text):
    matches.append(group[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')