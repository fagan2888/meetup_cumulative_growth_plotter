"""Plot a Meetup's membership .XLS file (for Admins) as an annotated cumulative growth plot"""
import datetime
from datetime import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import dateutil.parser as dt_parser

# to add
# xmas due to inflection
# point where we became largest group
# option to use different xls input files

if __name__ == "__main__":
    filename = "PyData-London-Meetup_Member_List_on_06-22-15.xls"
    df = pd.io.parsers.read_table(filename)
    # plot cumulative sum of members at pydata
    df['Joined Group on'] = df['Joined Group on'].map(lambda x: dt_parser.parse(x, dayfirst=False))
    df['Member growth'] = 1
    df.set_index('Joined Group on', inplace=True)
    df.sort(inplace=True)  # sort on the index
    df['Member growth'].cumsum().plot()

    plt.title("PyDataLondon Cumulative Membership Growth")
    plt.ylabel("Membership")
    plt.tight_layout()

    cum_sum = df['Member growth'].cumsum()
    plt.annotate("(1st Conference Feb 22nd)", (dt(2014, 5, 5), 0))
    plt.annotate("2nd Conference", (dt(2015,6,20), 1640), ha="right")

    x_dt = dt(2014,6,3)
    plt.annotate("1st Meetup!", (x_dt, cum_sum[x_dt].max()), ha="right")
    meetups = [dt(2014, 7, 1), dt(2014,8,5), dt(2014,9,2),
               dt(2014, 10,7), dt(2014,11,4), dt(2014,12,2),
               dt(2015, 1, 6), dt(2015,2,3), dt(2015,3,3),
               dt(2015,4,7), dt(2015,5,5)]
    for meetup_dt in meetups:
        plt.annotate("M", (meetup_dt, cum_sum[meetup_dt].max()), ha="right")

    x_dt = dt(2015, 5, 25)
    plt.annotate("Now Largest London Python Usergroup", (x_dt, cum_sum[x_dt].max()), ha="right")

    plt.xlim(xmin=datetime.datetime(2014,4,15))
    #plt.show()
    plt.savefig("pydatalondon_membership_growth.png")

    #df2=df.resample("1W", how="sum")
    #df2['Member growth'].plot()
