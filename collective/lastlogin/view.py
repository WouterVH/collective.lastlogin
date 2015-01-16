# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter 


class LastLogin(BrowserView):

    def memberinfo(self):

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal_url = portal_state.portal_url()
        mtool = getToolByName(self.context, 'portal_membership')

        for user in mtool.searchForMembers():
            yield({'id': user.getId(),
                   'login_time': user.getProperty('login_time'),
                   'last_login_time': user.getProperty('last_login_time'),
                   'author_url': portal_url + '/author/' + user.getId(),
                   })
