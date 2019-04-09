import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spamdetector.settings")

import django

django.setup()

from spam.models import spamdb


def save_review_from_row(review_row):
    review = spamdb()
    review.name = review_row[0]
    review.data = review_row[1]
    review.save()


# the main function for the script, called by the shell
if __name__ == "__main__":

    # Check number of arguments (including the command name)
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        reviews_df = pd.read_csv(sys.argv[1],encoding='latin1')
        print(reviews_df)

        # apply save_review_from_row to each review in the data frame
        reviews_df.apply(
            save_review_from_row,
            axis=1
        )

        print("There are {} reviews in DB".format(Review.objects.count()))

    else:
        print("Please, provide Reviews file path")

