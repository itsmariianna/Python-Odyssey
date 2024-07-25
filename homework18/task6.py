# Create a function to generate a report with both required and optional sections.
# Use positional arguments for required sections.
# Use keyword arguments for optional sections with default values.

def report(title, *subtitle, author = 'Anonymous', date = 'N\A', verified = 'No', **kwargs):
    print('\nReport')
    print(f'Title: {title}')
    for i in subtitle:
        print(f'--{i}')
    print(f'Author: {author}')
    print(f'Date: {date}')
    print(f'Verified: {verified}')

report('Project summary', 'Overview', 'Summary')

report('Financial Overview', 'Intoduction', 'Overview', 'Summary', author='Sam Smith', date='10.08.2023', verified='Yes')