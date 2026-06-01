class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.skills = ["React", "Tailwind CSS"]
        self.status = "Active Job-Seeker"

    def introduce(self):
        print(f"Developer: {self.name}")
        print(f"Role: {self.role}")
        print(f"Status: {self.status}")
        print("Currently mastering: Python & Data Structures")

# Initialize the track
me = Developer(name="Samson", role="Software Engineer")
me.introduce()
