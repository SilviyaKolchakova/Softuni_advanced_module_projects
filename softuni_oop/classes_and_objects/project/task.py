class Task:
    def __init__(self, name, due_date, ):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_due_date):
        if new_due_date == self.due_date:
            return "Date cannot be the same."
        self.due_date = new_due_date
        return self.due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number >= len(self.comments):
            print("Cannot find comment.")

        self.comments[comment_number] = new_comment
        return f"{', '.join([f'{x}' for x in self.comments])}"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"




# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
