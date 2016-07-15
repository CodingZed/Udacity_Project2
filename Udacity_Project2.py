import unicodecsv

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open('enrollments.csv', 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
		

daily_engagement = read_csv('daily_engagement.csv')
enrollments = read_csv('enrollments.csv')
project_submissions = read_csv('project_submissions.csv')

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del [engagement_record['acct']]
	
def get_unique_students(data):
    unique_students = set ()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students
	
len(enrollments)

unique_enrollments_students=get_unique_students(enrollments)
print len(unique_enrollments_students)

unique_enrollments_students=set()
for enrollment in enrollments:
    unique_enrollments_students.add(enrollment['account_key'])
    
len(unique_enrollments_students)

len(daily_engagement)

unique_engagement_students=get_unique_students(daily_engagement)
print len(unique_engagement_students)

unique_project_submissions_students=get_unique_students(project_submissions)
print len(unique_project_submissions_students)


for special_case in enrollments:
    student=special_case['account_key']
    if student not in unique_engagement_students:
        print special_case
        break

		
num_problem_students = 0

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students \
    and enrollment['join_date']!=enrollment['cancel_date']:
        num_problem_students+= 1
        print enrollment
    
num_problem_students



from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date=='':
        return None
    else:
        return dt.strptime(date,'%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i=='':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled']=='True'
    enrollment['is_udacity'] = enrollment['is_udacity']=='True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    
enrollments[10]