from datetime import time, timedelta


class Report:
    def __init__(self, name, start_time, minutes_duration, topic):
        self.name = name
        self.start_time = timedelta(
            hours=time.fromisoformat(start_time).hour,
            minutes=time.fromisoformat(start_time).minute,
        )
        self.duration = timedelta(minutes=int(minutes_duration))
        self.end_time = self.start_time + self.duration
        self.topic = topic

    def __str__(self):
        return f"Report {self.name} from {self.start_time} to {self.end_time} on topic {self.topic}"

    def __hash__(self):
        return hash(str(self))


class Conference:
    def __init__(self, name, reports=None):
        self.name = name
        self.reports = reports if reports else []

    def add_report(self, report: Report):
        self.reports.append(report)
        self.reports.sort(key=lambda x: x.start_time)
        i = self.reports.index(report)
        if len(self.reports) > 1:
            if i == 0 and self.reports[i + 1].start_time < report.end_time:
                self.reports.pop(i)
                raise ValueError("The report overlaps another")
            elif (
                i == len(self.reports) - 1
                and self.reports[i - 1].end_time > report.start_time
            ):
                self.reports.pop(i)
                raise ValueError("The report overlaps another")
            elif 0 < i < len(self.reports) - 1 and (
                self.reports[i - 1].end_time > report.start_time
                or self.reports[i + 1].start_time < report.end_time
            ):
                self.reports.pop(i)
                raise ValueError("The report overlaps another")

    def remove_report(self, report_name):
        reports_to_delete = []
        for i, el in enumerate(self.reports):
            if el.name == report_name:
                reports_to_delete.append(i)
        if not reports_to_delete:
            raise ValueError("No reports with this name")
        if len(reports_to_delete) == 1:
            self.reports.pop(reports_to_delete[0])
        else:
            print(
                *[
                    f"{self.reports[reports_to_delete[i]]} {i + 1}"
                    for i in range(len(reports_to_delete))
                ],
                sep="\n",
            )
            print(f"Enter a number 1-{len(reports_to_delete)} of report to delete")
            self.reports.pop(reports_to_delete[int(input()) - 1])


def conference_loop(conference: Conference):
    while True:
        try:
            print("\nEnter command:\nadd_report <name> <start_time> ", end="")
            print(
                "<minutes_duration> <topic>\nremove_report <name>\nprint_reports\nexit\n"
            )
            command = input().split()
            if command[0] == "add_report":
                conference.add_report(Report(*command[1:]))
                print("Report added")
            elif command[0] == "remove_report":
                conference.remove_report(command[1])
                print("Report removed")
            elif command[0] == "print_reports":
                print(*conference.reports, sep="\n")
            elif command[0] == "exit":
                exec("globals()[conference.name] = conference")
                break
            else:
                raise ValueError("Invalid command")
        except ValueError as e:
            print(e)


while True:
    try:
        print(
            "\nEnter command:\ncreate_conference <name>\nopen_conference <name>\nexit\n"
        )
        command = input().split()
        if command[0] == "create_conference":
            conference = Conference(command[1])
            conference_loop(conference)
        elif command[0] == "open_conference":
            conference = globals().get(command[1])
            if not conference or not isinstance(conference, Conference):
                raise ValueError("No conference with this name")
            conference_loop(conference)
        elif command[0] == "exit":
            break
        else:
            raise ValueError("Invalid command")
    except ValueError as e:
        print(e)
