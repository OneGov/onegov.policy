from ftw.tooltip.interfaces import ITooltipSource
from onegov.policy import _
from onegov.policy.interfaces import IOneGovLayer
from zope.component import adapts
from zope.interface import implements, Interface


class DashboardTooltipSource(object):
    implements(ITooltipSource)
    adapts(Interface, IOneGovLayer)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def global_condition(self):
        return True

    def tooltips(self):
        return [

            {'selector': u'a.dashboardButton.buttonClose',
             'text': _(u'text_dashboard_close',
                       default=u'Toggle portlet'),
             'condition': 'body.template-dashboard'},

            {'selector': u'span.dashboardButton.buttonMove',
             'text': _(u'text_dashboard_move',
                       default=u'Move portlet'),
             'condition': 'body.template-dashboard'},

            {'selector': u'a.dashboardButton.buttonRemove',
             'text': _(u'text_dashboard_remove',
                       default=u'Delete portlet'),
             'condition': 'body.template-dashboard'},

            {'selector': u'a.dashboardButton.buttonEdit',
             'text': _(u'text_dashboard_edit',
                       default=u'Edit portlet'),
             'condition': 'body.template-dashboard'},

            ]
