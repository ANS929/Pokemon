from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from learning.models import Badge, CompletedBadge
from account.models import UserLogin
from datetime import timedelta
from django.contrib import messages
from django.utils.timezone import now

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    today = now().date()
    UserLogin.objects.get_or_create(user=user, login_date=today)

    check_consecutive_logins(request, user)

def check_consecutive_logins(request, user, required_days=3):
    today = now().date()
    consecutive_days = [today - timedelta(days=i) for i in range(required_days)]

    logged_in_dates = UserLogin.objects.filter(user=user, login_date__in=consecutive_days).values_list('login_date', flat=True)

    if len(logged_in_dates) == required_days:
        # award the Theta Badge for consecutive logins
        if not CompletedBadge.objects.filter(student=user, badge__name='Theta Badge').exists():
            badge = Badge.objects.get(name='Theta Badge')
            CompletedBadge.objects.create(student=user, badge=badge)
            messages.success(request, "Congratulations! You've earned the Theta Badge!")