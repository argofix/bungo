# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Bem-vindo!")
    return dict(message=T('Bem-vindo ao Bungo!'))

def LIC_ZON():
    form = SQLFORM.factory(
        Field('emp', label=('Enquadramento:'), requires=IS_IN_SET(['EIA', 'SEIA', 'NALIC'])),
        Field('UC', label=('Zoneamento:'), requires=IS_IN_SET(['CZA', 'SZA', 'NAZA']))
        )
    if form.process().accepted:
        session.flash = 'Opções inserida com sucesso!'
        session.emp = form.vars.emp
        session.UC = form.vars.UC
    if form.vars.UC == 'CZA':
        redirect(URL('UCCZA'))
    if form.vars.UC == 'SZA':
        if form.vars.emp == 'EIA':
            redirect(URL('UCSZA3'))
        if form.vars.emp == 'SEIA':
            redirect(URL('UCSZA2'))
        if form.vars.emps == 'NALIC':
            redirect(URL('UCNALIC'))
    if form.vars.UC == 'NAZA':
        redirect(URL('UCNAZA'))
    return dict(form=form)

def UCCZA():
    form = SQLFORM.factory(
        Field('uccza', label=('Localização do empreendimento/atividade?'), requires=IS_IN_SET(['IUC', 'IZA', 'FZA']))
    )
    if form.process().accepted:
        response.flash = 'Opção inserida com sucesso!'
        session.uccza = form.vars.uccza
        redirect(URL('resultado'))
    return dict(form=form)

def UCSZA3():
    form = SQLFORM.factory(
        Field('ucsza3', label=('Localização do empreendimento/atividade?'), requires=IS_IN_SET(['IUC', 'ZPD3', 'FZPD3']))
    )
    if form.process().accepted:
        response.flash = 'Opção inserida com sucesso!'
        session.ucsza3 = form.vars.ucsza3
        redirect(URL('resultado'))
    return dict(form=form)


def UCSZA2():
    form = SQLFORM.factory(
        Field('ucsza2', label=('Localização do empreendimento/atividade?'), requires=IS_IN_SET(['IUC', 'ZPD2', 'FZPD2']))
    )
    if form.process().accepted:
        response.flash = 'Opção inserida com sucesso!'
        session.ucsza2 = form.vars.ucsza2
        redirect(URL('resultado'))
    return dict(form=form)

def UCNALIC():
    form = SQLFORM.factory(
        Field('ucnalic', label=('Localização do empreendimento/atividade?'), requires=IS_IN_SET(['IUC', 'FUC']))
    )
    if form.process(vars).accepted:
        response.flash = 'Opção inserida com sucesso!'
        session.ucnalic = form.vars.ucnalic
        redirect(URL('resultado'))
    return dict(form=form)


def UCNAZA():
    form = SQLFORM.factory(
        Field('ucnaza', label=('Localização do empreendimento/atividade?'), requires=IS_IN_SET(['IUC', 'FUC']))
    )
    if form.process().accepted:
        response.flash = 'Opção inserida com sucesso!'
        session.ucnaza = form.vars.ucnaza
        redirect(URL('resultado'))
    return dict(form=form)

def resultado():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
