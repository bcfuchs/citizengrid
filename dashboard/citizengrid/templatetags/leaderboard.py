from django import template
from citizengrid.models import UsersApplications, UserInfo
import logging


logger = logging.getLogger("django")
register = template.Library()
logger.debug("leaderboard")

@register.inclusion_tag("widgets/leaderboard.html")
def leaderboard_widget(klass):
    """ widget to display user stats 
        usage {% leaderboard_widget "some-class" %}
        some-class will be added to the classes on the container div
    """
    stats = UsersApplications.objects.order_by("-run_count")
    ctx = {"hi":"there","stats":stats,"klass":klass}
    return ctx