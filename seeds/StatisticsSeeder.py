from flask_seeder import Seeder
from api.models import db, ListingsStatisticsModel


class ListingsStatisticsSeeder(Seeder):
    """
    This is the seeder for the listing statistics model.
    No other models will be affected by this.
    """

    # run() will be called by Flask-Seeder
    def run(self):
        statistics = [
            {
                'listing_id': 1,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 2,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 3,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 4,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 6,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 7,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 8,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 9,
                'views': 0,
                'applications': 0
            },
            {
                'listing_id': 11,
                'views': 0,
                'applications': 0
            }
        ]
        for stats in statistics:
            db.session.add(ListingsStatisticsModel(**stats))
            db.session.commit()