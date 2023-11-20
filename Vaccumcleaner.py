class VacuumCleaner:
    def __init__(self, position, status):
        self.position = position  # 0 for 'A', 1 for 'B'
        self.status = status  # 0 for 'Dirty', 1 for 'Clean'

    def clean(self):
        print(f"Vacuum Cleaner is cleaning at position {chr(ord('A') + self.position)}")
        self.status = 1  

def vacuum_cleaner_problem():
    locations = ['A', 'B']
    
    initial_position = int(input("Enter the initial position of the vacuum cleaner (0 for 'A', 1 for 'B'): "))
    initial_status = int(input("Enter the initial status of the location (0 for 'Dirty', 1 for 'Clean'): "))
    vacuum = VacuumCleaner(initial_position, initial_status)
    if vacuum.status == 0:
        vacuum.clean()
    vacuum.position = 1 - vacuum.position  
    if vacuum.status == 0:
        vacuum.clean()

    print("Vacuum Cleaner has completed the cleaning process.")
vacuum_cleaner_problem()
