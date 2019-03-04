
import pandas as pd

class Extracker:
    def __init__(self,file_names):
        self.Tracker = pd.read_excel(file_names, sheet_name='Tracker',
                        header=0, index_col=None,usecols ="A,B,H,O,S,AD")
        self.report_touched1 = None
        self.tat = None
        self.overall_rating1= None
        self.cleaned = False

    def clean(self):

        # clean Lab column then group by dict a, add an new column in Tracker
        a_Series = [str(item)[0:2]for item in self.Tracker.Lab ]
        a = {'BV': 'BV', 'IT': 'ITS', 'TU': 'TUV', 'na': 'na'}
        a_Series = [a[item] for item in a_Series]
        self.Tracker.loc[:, 'Lab_group'] = pd.Series(a_Series)
        self.cleaned = True

        return self.Tracker

    # calculate audited report number in a period
    def count_test_report(self,group_key, start_date=None,end_date=None):

        if self.cleaned:
            current_tracker = self.Tracker
            if start_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] >= start_date]
            if end_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] <= end_date]

            self.report_touched1 = current_tracker.groupby(group_key).Test_report_number.nunique()
        else:
            self.clean()
            self.count_test_report(group_key,start_date = start_date,end_date = end_date)
        return self.report_touched1

    def count_tat(self,group_key, start_date=None,end_date=None):
        if self.cleaned:
            current_tracker = self.Tracker
            if start_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] >= start_date]
            if end_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] <= end_date]
            self.tat = current_tracker.groupby(group_key).TAT.mean()
        else:
            self.clean()
            self.count_tat(group_key,start_date = start_date,end_date = end_date)
        return self.tat


    def overall_rating(self,group_key1, group_key2,start_date=None,end_date=None):
        if self.cleaned:
            current_tracker = self.Tracker
            if start_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] >= start_date]
            if end_date:
                current_tracker = current_tracker.loc[current_tracker['Audit Date'] <= end_date]
            self.overall_rating1 = current_tracker.groupby([group_key1, group_key2]).size()
        else:
            self.clean()
            self.overall_rating(group_key1,group_key2,start_date,end_date)
        return self.overall_rating1


if __name__ == '__main__':
    location = '/Users/yanjingy/Documents/work/on_going_project/Lab_audit/'
    file_names = ['Lab Audit Tracker.xlsx', 'lab Portal Audit WBR.xlsx', 'week_input.txt']
    tracker = Extracker(location+file_names[0])
    print(tracker.overall_rating('Lab_group','Overall Rating'))
    print(tracker.count_tat('Lab_group'))
    print(tracker.count_test_report('Lab_group'))