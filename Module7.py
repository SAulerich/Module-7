class CourseSchedule:
    def __init__(self):
        self.roomNumbers = {
            'CSC101': '3004',
            'CSC102': '4501',
            'CSC103': '6755',
            'NET110': '1244',
            'COM241': '1411'
        }
        self.instructors = {
            'CSC101': 'Haynes',
            'CSC102': 'Alvarado',
            'CSC103': 'Rich',
            'NET110': 'Burke',
            'COM241': 'Lee'
        }
        self.meetingTimes = {
            'CSC101': '8:00 a.m.',
            'CSC102': '9:00 a.m.',
            'CSC103': '10:00 a.m.',
            'NET110': '11:00 a.m.',
            'COM241': '11:00 p.m.'
        }
    def get_course_info(self, courseNumber):
        if courseNumber in self.roomNumbers:
            print(f"\nRoom Number: {self.roomNumbers[courseNumber]}")
            print(f"Instructor: {self.instructors[courseNumber]}")
            print(f"Meeting Time: {self.meetingTimes[courseNumber]}")
        else:
            print("\nError: Course can not be found")

if __name__ == "__main__":
    course_info = CourseSchedule()
    courseNumber = input("Enter the course number: ")
    course_info.get_course_info(courseNumber)
    input(f"\nPress 'Enter' to exit")