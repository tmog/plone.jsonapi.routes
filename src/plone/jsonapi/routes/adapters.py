# -*- coding: utf-8 -*-

__author__ = 'Ramon Bartl <ramon.bartl@googlemail.com>'
__docformat__ = 'plaintext'

from zope import interface
from zope import component

from Products.ZCatalog.interfaces import ICatalogBrain
from Products.ATContentTypes.interfaces import IATDocument
from Products.ATContentTypes.interfaces import IATEvent

from interfaces import IInfo


class Base(object):
    """ Base Adapter
    """
    interface.implements(IInfo)

    def __init__(self, context):
        self.context = context

    def to_dict(self, context):
        return {}

    def __call__(self):
        return self.to_dict(self.context)


class BaseInfo(Base):
    """ Catalog Brain Adapter
    """
    interface.implements(IInfo)
    component.adapts(ICatalogBrain)

    def to_dict(self, brain):
        return {
            "id":          brain.getId,
            "uid":         brain.UID,
            "title":       brain.Title,
            "description": brain.Description,
            "url":         brain.getURL(),
            "portal_type": brain.portal_type,
            "created":     brain.created.ISO8601(),
            "modified":    brain.modified.ISO8601(),
            "effective":   brain.effective.ISO8601(),
            "type":        brain.portal_type,
            "tags":        brain.subject,
        }


class DocumentInfo(Base):
    """ Document Adapter
    """
    interface.implements(IInfo)
    component.adapts(IATDocument)

    def to_dict(self, obj):
        return {
            "text":          obj.getText(),
            "presentation":  obj.presentation,
            "tableContents": obj.tableContents,
            "text_format":   obj.tableContents,
            "plain_text":    obj.getText(mimetype="text/plain").decode("utf-8"),
        }


class EventInfo(Base):
    """ Document Adapter
    """
    interface.implements(IInfo)
    component.adapts(IATEvent)

    def to_dict(self, obj):
        return {
            "text":       obj.getText(),
            "plain_text": obj.getText(mimetype="text/plain").decode("utf-8"),
            "start":      obj.start().ISO8601(),
            "end":        obj.end().ISO8601(),
            "location":   obj.location,
            "attendees":  obj.attendees,
            "event_url":  obj.eventUrl,
        }

# vim: set ft=python ts=4 sw=4 expandtab :