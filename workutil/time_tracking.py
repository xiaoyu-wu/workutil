import re
from subprocess import check_output


class TimeTracker(object):

    def utt_report(self, date_str=''):
        command = "utt report " + date_str
        report = check_output(command.split())
        return report.decode('UTF-8')

    def get_work_time_per_activity(self, date_str=''):
        report = self.utt_report(date_str)
        report_lines = report.split('\n')
        match_index = []
        activity_line_match = re.compile(r"-+ Activities -+")
        detail_line_match = re.compile(r"-+ Details -+")
        for idx, line in enumerate(report_lines):
            if activity_line_match.match(line) or detail_line_match.match(line):
                match_index.append(idx)
        work_time_dict = {}
        assert len(match_index) == 2
        for line in report_lines[match_index[0] + 1 : match_index[1]]:
            line_list = line.split()
            if len(line_list) == 3:
                m = re.match(r"\((\d+)h(\d+)\)", line_list[0])
                work_time_dict[line_list[2]] = tuple(int(i) for i in m.groups())
        return work_time_dict


if __name__ == "__main__":
    tt = TimeTracker()
    result = tt.get_work_time_per_activity()
