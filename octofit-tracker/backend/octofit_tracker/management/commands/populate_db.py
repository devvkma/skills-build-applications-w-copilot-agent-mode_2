from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

User = get_user_model()
class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        for user in User.objects.all():
            if not user.is_superuser:
                user.delete()
        self.stdout.write(self.style.SUCCESS('Deleted all data.'))

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.stdout.write(self.style.SUCCESS('Created teams Marvel and DC.'))

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]
        self.stdout.write(self.style.SUCCESS('Created superhero users.'))

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20)
        Activity.objects.create(user=users[2], type='swim', duration=45, distance=2)
        Activity.objects.create(user=users[3], type='run', duration=50, distance=10)
        self.stdout.write(self.style.SUCCESS('Created activities.'))

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all')
        Workout.objects.create(name='Strength Training', description='Strength for all')
        self.stdout.write(self.style.SUCCESS('Created workouts.'))

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=80)
        Leaderboard.objects.create(user=users[2], score=90)
        Leaderboard.objects.create(user=users[3], score=95)
        self.stdout.write(self.style.SUCCESS('Created leaderboard.'))
