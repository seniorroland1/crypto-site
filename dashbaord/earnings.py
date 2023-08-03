from . models import *
import datetime
from django.db.models import F


def earning_job():
    profiles = Profile.objects.all()
    for profile in profiles:
        plans = profile.plan_set.all()
        if plans != None:
            for plan in plans:
                if plan.active ==True:
                    duration = datetime.timedelta(minutes=plan.duration)
                    end_time = plan.created + duration
                    current_time = datetime.datetime.now()
                    current_time = current_time.replace(tzinfo=None)
                    end_time = end_time.replace(tzinfo=None)
                    if end_time >= current_time:
                        Profile.objects.filter(nickname=profile).update(balance=F('balance') +float(plan.payout))
                        Plan.objects.filter(created=plan.created).update(
                            profile = plan.profile,
                            payout = plan.payout,
                            duration = plan.duration,
                            active = False
                        )
                       