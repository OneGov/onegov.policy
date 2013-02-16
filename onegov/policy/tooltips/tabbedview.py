from ftw.tooltip.interfaces import ITooltipSource
from onegov.policy import _
from onegov.policy.interfaces import IOneGovLayer
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements


class TabbedviewTooltipSource(object):
    implements(ITooltipSource)
    adapts(Interface, IOneGovLayer)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def global_condition(self):
        return True

    def tooltips(self):
        return [

            {'selector': u'a.rollover',
             'text': u'',  # Use title attribute
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-overview',
             'text': _(u'text_tab_overview',
                       default=u'Overview of folders and recent changes.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-documents',
             'text': _(u'text_tab_documents',
                       default=u'List all documents in this workspace.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-events',
             'text': _(u'text_tab_events',
                       default=u'Manage events and meetings.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-contacts',
             'text': _(u'text_tab_contacts',
                       default=u'List of contacts, which are related to this '
                       u'workspace but do not have access.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-tasks',
             'text': _(u'text_tab_tasks',
                       default=u'List and manage tasks.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-sharing',
             'text': _(u'text_tab_sharing',
                       default=u'Manage members of this workspace.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-participants',
             'text': _(u'text_tab_participants',
                       default=u'List of all members with '
                       u'access to this workspace.'),
             'condition': 'body.template-tabbed_view'},

            {'selector': u'.tabbedview-tabs a#tab-workspaces',
             'text': _(u'text_tab_workspaces',
                       default=u'Lists all workspaces you have access to.'),
             'condition': 'body.template-workspaces_view'},

            {'selector': u'.tabbedview-tabs a#tab-documents',
             'text': _(u'text_tab_workspaces_documents',
                       default=u'Lists all documents of all workspaces you'
                       u' have access to.'),
             'condition': 'body.template-workspaces_view'},

            {'selector': u'.tabbedview-tabs a#tab-events',
             'text': _(u'text_tab_workspaces_events',
                       default=u'Lists all events of all workspaces you'
                       u' have access to.'),
             'condition': 'body.template-workspaces_view'},

            ]
