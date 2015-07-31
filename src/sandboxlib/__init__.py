# -*- coding: utf-8 -*-
"""Init and utils."""
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module

# Whitelist pdf functions
allow_module('pretaweb.plomino2pdf.api')
pdf_api = ModuleSecurityInfo('pretaweb.plomino2pdf.api')
pdf_api.declarePublic('generate_pdf')

# Whitelist email functions
allow_module('email.mime.multipart')
multipart = ModuleSecurityInfo('email.mime.multipart')
multipart.declarePublic('MIMEMultipart')
allow_module('email.mime.text')
text = ModuleSecurityInfo('email.mime.text')
text.declarePublic('MIMEMultipart')
allow_module('email.mime.application')
application = ModuleSecurityInfo('email.mime.application')
application.declarePublic('MIMEApplication')

# Whitelist plone.api
allow_module('plone.api.portal')
portal = ModuleSecurityInfo('plone.api.portal')
portal.declarePublic('get_tool')


# Whitelist M2Crypto encrypting
try:
    import M2Crypto
except:
    M2Crypto = None

if M2Crypto is not None:
    allow_module('M2Crypto')
    allow_module('M2Crypto.Rand')
    ModuleSecurityInfo('M2Crypto.Rand').declarePrivate('load_file', 'save_file')

    allow_module('M2Crypto.BIO')
    allow_class(M2Crypto.BIO.MemoryBuffer)

    allow_module('M2Crypto.SMIME')
    ModuleSecurityInfo('M2Crypto.SMIME').declarePrivate('load_pkcs7', 'smime_load_pkcs7')

    M2Crypto.SMIME.SMIME._security = sec = ClassSecurityInfo()
    sec.declareObjectPublic()
    sec.declarePrivate('load_key')
    sec.setDefaultAccess(1)
    sec.apply(M2Crypto.SMIME.SMIME)
    InitializeClass(M2Crypto.SMIME.SMIME)

    allow_class(M2Crypto.SMIME.Cipher)

    allow_module('M2Crypto.X509')
    ModuleSecurityInfo('M2Crypto').declarePublic('X509')
    ModuleSecurityInfo('M2Crypto.X509').declarePrivate('load_cert', 'save_pem', 'save', 'load_request', 'load_crl')
    ModuleSecurityInfo('M2Crypto.X509').declarePublic('load_cert_string')


    allow_class(M2Crypto.X509.X509_Stack)



