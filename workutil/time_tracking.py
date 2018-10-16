import subprocess


class TimeTracker(object):
    def utt_report(self):
        command = "utt report"
        subprocess.Popen(command.split())


if __name__ == "__main__":
    tt = TimeTracker()
    tt.utt_report()
