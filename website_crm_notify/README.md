==============
Website CRM Notify
==============

This module provides the following functions:

* When someone sends an inquiry from `Contact us` page on website,
an email is sent to both the company and the querist for the purposes of notification and reminder respectively.

This module depends on `wbsite_crm` module.


Installation
============

To install this module, 

* Place this module in a directory included in addons_path, updates Apps list on Odoo, and install this module.


Configuration
============+

To configure this module:

* Go to `Settings > Technical > Email > Templates` and select `Contact Form Notify`,
* Edit the template of Email to be sent.

Make sure that outgoing email has been configured.

By default, email is sent to the following addresses:

* email address of the company (for the purpose of notification)
* the sender inputs (for the purpose of reminder)

and the body of email includes all the information the querist has input (Name, Phone, Company and so on).


Usage
============

To use this module,

* Go to `Contact us` page of website, input the contents of your question or inquiry and submit them
